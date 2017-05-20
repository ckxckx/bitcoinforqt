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
		# result.append('ffffffff')
#################################################
		# squence can be int
		if isinstance(perin['sequence'], long):
			print 'pppppppppppppppppppp'
			result.append(dec2byte(perin['sequence'], 4))
		elif isinstance(perin['sequence'], int):
			print '\nxxxxxxxxxxxxxxxxxxxxxxxxxx\n'
			result.append(dec2byte(perin['sequence'], 4))
		# or be normal hex-str
		elif isinstance(perin['sequence'], str):
			print '\nuuuuuuuuuuuuuuuuuuuuuu\n'
			result.append(big2little(perin['sequence']))

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
