# -*- coding: utf-8 -*-
import json


# dec to byte in little-endian or big-endian
def dec2byte(num, byte=None, format="little-endian"):
	if byte == None:
		tmp = "%x" %num
		if len(tmp) % 2 == 1:
			tmp = "0" + tmp
	else:
		tmp = ("%0"+"%s" % (2*byte) +"x") %num
	if format == "little-endian":
		tmp = big2little(tmp)
	return tmp

# format the byte data in little-endian
def big2little(bigstr):
	return "".join([bigstr[2*i:2*i+2] for i in xrange(len(bigstr)/2)][::-1])

# transform json tx to raw tx in hex
def json2hex(in_json):
	# in_json must have keys showing as below: ['version', 'inputs', 'outputs', 'lock_time']
	# inputs of in_json must have keys showing as below: ['txid_prev', 'out_prev', 'script_sig', 'squence']
	# outputs of in_json must have keys showing as below: ['value', 'script_pub', 'adress', 'script_type']

	result = []
	# add version to hex
	result.append(dec2byte(in_json['version'], 4))
	# add input_num to hex
	result.append(dec2byte(len(in_json['inputs'])))
	# add inputs to hex
	for _, perin in enumerate(in_json['inputs']):
		result.append(big2little(perin['txid_prev']))
		result.append(dec2byte(perin['out_prev'], 4))

		# add script_pubkey to hex
		result.append(dec2byte(len(perin['script_sig'])/2))
		result.append(perin['script_sig'])


################add by ckx#####################
#暂时先用这个
		result.append('ffffffff')
#################################################
		# squence can be int
#		if isinstance(perin['sequence'], int):
#			result.append(dec2byte(perin['sequence'], 4))
		# or be normal hex-str
#		elif isinstance(perin['sequence'], str):
#			result.append(big2little(perin['sequence']))

	# add output_num to hex
	result.append(dec2byte(len(in_json['outputs'])))
	# add output to hex
	for _, perout in enumerate(in_json['outputs']):
		result.append(dec2byte(perout['value'], 8))

		# add script_pubkey to hex
		result.append(dec2byte(len(perout['script_pub'])/2))
		result.append(perout['script_pub'])

	# add lock_time to hex
	result.append(dec2byte(in_json['lock_time'], 4))
	return "".join(result)

if __name__ == '__main__':
	# testjson is a sample of json transaction
	# testhex is the hex string of above transaction
	testjson_unsigned = {
		"version": 1, 
		"lock_time": 0, 
		"inputs": [
			{
				# "txid_prev": "c8ea8b221580ebb2f1cabc8b40797bffec742b97c82a329df96d93121db43519",
				"txid_prev":"8c535ba5f43018001fc9f23bf484ab5d65836600c01eba90eb6ae4554a0438c8",
				"out_prev": 0, 
				#"script_sig": "483045022100921fc36b911094280f07d8504a80fbab9b823a25f102e2bc69b14bcd369dfc7902200d07067d47f040e724b556e5bc3061af132d5a47bd96e901429d53c41e0f8cca012102152e2bb5b273561ece7bbe8b1df51a4c44f5ab0bc940c105045e2cc77e618044", 
				"script_sig":'',

				"sequence": 4294967295
#sequence 的hex化为ffffffff
			}, 
		], 
		"outputs": [
			{

				"value": 1500000000,#这个地址是收款ckx_r的 
				"script_pub": "76a914d166d4ac217f0d51b7ab7a7919f273ac880eabc388ac", 
					#对于普通交易76a9.....88ac中间的是hash160以后的公钥
			}, 
			{
				"value": 999946099.9964, 
						#这个地址是ckx1的找钱
				"script_pub":  "76a914466d50fb3570699486ad8c9ee363ccf275abfa7f88ac", 
			}, 
		]
	}




	result = json2hex(testjson_unsigned)
	# result = json2hex(tj)
	print result
	#print testhex
