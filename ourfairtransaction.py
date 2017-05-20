# -*- coding: utf-8 -*-
#A1PubKey=
#A2PubKey=
#A3PubKey=
#B1PubKey=
#B2PubKey=
#B3PubKey=
#hA=


fundingtransaction = {
        "version": 1,
		"lock_time": 0,
		"inputs": [
			{
				"txid_prev": " ",
				"out_prev": 0,
				"script_sig": " ",
				"sequence":
			},
            {
				"txid_prev": " ",
				"out_prev": 0,
				"script_sig": " ",
				"sequence":
			},
		],
		"outputs": [
			{
				"value": 1000000,
				"script_pub":'''
                    OP_DUPOP_HASH160 < HASH160(\
                        OP_HASH160 < HASH160(hA) > OP_EQUAL\
                        OP_IF
                            OP_2 < B1PubKey > < A1PubKey >OP_2OP_CHECKMULTISIG
                        OP_ELSE
                            < Ttime >OP_CHECKSQUENCEVERIFYOP_DROP < B2PubKey > OP_CHECKSIG
                        OP_ENDIF
                    ) > OP_EQUAL
                ''',
			},
		]
	}

commitmenttransaction = {
		"version": 1,
		"lock_time": 0,
		"inputs": [
			{
				"txid_prev": " ",
				"out_prev": 0,
				"script_sig": "OP_0 < SigB1 > < SigA1 > < hA > < RedeemScript > ",
				"sequence":
			},
		],
		"outputs": [
			{
				"value": 1000000,
				"script_pub":
                "
                      OP_DUPOP_HASH160 < HASH160(pkA) > OP_EQUALVERIFYOP_CHECKSIG
                ",
			},
            {
                "value": 1000000,
				"script_pub":
                "
                    OP_DUPOP_HASH160 < HASH160(
                    OP_HASH160 < HASH160(hB) > OP_EQUAL
                    OP_IF
                        OP_2 < A3PubKey > < B3PubKey >OP_2OP_CHECKMULTISIG
                    OP_ELSE
                        < Ttime >OP_CHECKSQUENCEVERIFYOP_DROP
                    < A2PubKey > OP_CHECKSIG
                    OP_ENDIF
                    ) > OP_EQUAL
                ",
            },
		]
	}

deliverytransaction = {
		"version": 1,
		"lock_time": 0,
		"inputs": [
			{
				"txid_prev": " ",
				"out_prev": 0,
				"script_sig": "OP_0 < SigA3 > < SigB3 > < hB > <"
                                    OP_HASH160 < HASH160(hB) > OP_EQUAL
                                    OP_IF
                                        OP_2 < A3PubKey > < B3PubKey >OP_2OP_CHECKMULTISIG
                                    OP_ELSE
                                        < Ttime >OP_CHECKSQUENCEVERIFYOP_DROP
                                    < A2PubKey > OP_CHECKSIG
                                    OP_ENDIF
                              ">",
				"sequence":
			},
		],
		"outputs": [
			{
				"value": 1000000,
				"script_pub":
                "
                      OP_DUPOP_HASH160 < HASH160(pkA) > OP_EQUALVERIFYOP_CHECKSIG
                ",
			},
            {
                "value": 1000000,
				"script_pub":" ",
            },
		]
	}

timeoutcommitmenttransaction = {
		"version": 1,
		"lock_time": 0,
		"inputs": [
			{
				"txid_prev": " ",
				"out_prev": 0,
				"script_sig": "< SigB2 > OP_0< "
                            OP_HASH160 < HASH160(hA) > OP_EQUAL
                            OP_IF
                                OP_2 < B1PubKey > < A1PubKey >OP_2OP_CHECKMULTISIG
                            OP_ELSE
                                < Ttime >OP_CHECKSQUENCEVERIFYOP_DROP < B2PubKey > OP_CHECKSIG
                            OP_ENDIF
                              ">",
				"sequence":
			},
		],
		"outputs": [
			{
				"value": 1000000,
				"script_pub":
                "
                      OP_DUPOP_HASH160 < HASH160(pkA) > OP_EQUALVERIFYOP_CHECKSIG
                ",
			},
            {
                "value": 1000000,
				"script_pub":" ",
            },
		]
	}

timeoutdeliverytransaction = {
		"version": 1,
		"lock_time": 0,
		"inputs": [
			{
				"txid_prev": " ",
				"out_prev": 0,
				"script_sig": "< SigB2 > OP_0< "
                            OP_HASH160 < HASH160(hB) > OP_EQUAL
                            OP_IF
                                OP_2 < A3PubKey > < B3PubKey >OP_2OP_CHECKMULTISIG
                            OP_ELSE
                                < Ttime >OP_CHECKSQUENCEVERIFYOP_DROP
                            < A2PubKey > OP_CHECKSIG
                            OP_ENDIF
                              ">",
				"sequence":
			},
		],
		"outputs": [
			{
				"value": 1000000,
				"script_pub":
                "
                      OP_DUPOP_HASH160 < HASH160(pkA) > OP_EQUALVERIFYOP_CHECKSIG
                ",
			},
            {
                "value": 1000000,
				"script_pub":" ",
            },
		]
	}



