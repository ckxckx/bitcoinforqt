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

if __name__ == '__main__':
	# testjson is a sample of json transaction
	# testhex is the hex string of above transaction
	testjson = {
		"version": 1, 
		"lock_time": 0, 
		"inputs": [
			{
				# "txid_prev": "c8ea8b221580ebb2f1cabc8b40797bffec742b97c82a329df96d93121db43519",
				"txid_prev": "d6602dd740ffb455a84943fa38a202b669926bbbd572a801cc6d7174b2c18b30",

				"out_prev": 0, 
				"script_sig": "483045022100921fc36b911094280f07d8504a80fbab9b823a25f102e2bc69b14bcd369dfc7902200d07067d47f040e724b556e5bc3061af132d5a47bd96e901429d53c41e0f8cca012102152e2bb5b273561ece7bbe8b1df51a4c44f5ab0bc940c105045e2cc77e618044", 
				"sequence": 4294967295
			}, 
		], 
		"outputs": [
			{
				"value": 1000000, 
				"script_pub": "76a9145fb1af31edd2aa5a2bbaa24f6043d6ec31f7e63288ac", 
			}, 
			{
				"value": 3988000, 
				"script_pub": "76a914efec6de6c253e657a9d5506a78ee48d89762fb3188ac", 
			}, 
		]
	}

	tj={
		"version": 1,
		# "lock_time": 0,

		"vout_sz": 2,
		"received": "2017-05-10T13:20:23.860490658Z",
		"lock_time": 0,
		"hash": "405fdce67c0979769d14d85cc70590c3102db8d90c92fd928b0552ddd5dcc71a",
		"addresses": [
		"mgN94Z7hRWy4UfZHTj2T8hZd1BctusLkps",
		"mzPnKxCTMF3Dx9Nx9ktZ6n72LFheEX3MpQ"
		],
		"inputs": [
		{
		"addresses": [
		"mgN94Z7hRWy4UfZHTj2T8hZd1BctusLkps"
		],
		"script_sig": "",
		"sequence": 4294967295,
		"output_value": 155798,
		"output_index": 1,
		"out_prev": 0,
		# "txid_prev": "ef4351885fa3910d6654f1b4bda06033519f603460b7fa225c0659af994f4ec8",

		"txid_prev": "d6602dd740ffb455a84943fa38a202b669926bbbd572a801cc6d7174b2c18b30",
		"script_type":""
		}
		],
		"outputs": [
		{
		"script_type": "pay-to-pubkey-hash",
		"addresses": [
		"mzPnKxCTMF3Dx9Nx9ktZ6n72LFheEX3MpQ"
		],
		"value": 1,
		"script_pub": "76a914cf0f286c587aeef3dd0293c00dabb90c47da0a8388ac"
		},
		{
		"script_type": "pay-to-pubkey-hash",
		"addresses": [
		"mgN94Z7hRWy4UfZHTj2T8hZd1BctusLkps"
		],
		"value": 112697,
		"script_pub": "76a914094d5ec3d22b64175fcf316d6fd2940e2c4ae84688ac"
		}
		],	}



	testhex = "01000000011935b41d12936df99d322ac8972b74ecff7b79408bbccaf1b2eb8015228beac8000000006b483045022100921fc36b911094280f07d8504a80fbab9b823a25f102e2bc69b14bcd369dfc7902200d07067d47f040e724b556e5bc3061af132d5a47bd96e901429d53c41e0f8cca012102152e2bb5b273561ece7bbe8b1df51a4c44f5ab0bc940c105045e2cc77e618044ffffffff0240420f00000000001976a9145fb1af31edd2aa5a2bbaa24f6043d6ec31f7e63288ac20da3c00000000001976a914efec6de6c253e657a9d5506a78ee48d89762fb3188ac00000000"
	result = json2hex(testjson)
	# result = json2hex(tj)
	if result == testhex:
		print "Yes. The Function Works Well."
	else:
		print result
		print testhex