fun_unspent_txid1=''
fun_unspent_txid2=''
fun_sig1=''
fun_sig2=''
fun_seq1=4294967295
fun_seq2=4294967295
fun_value=10000   #pay attetion：两单交易的输入和要约等于这个输出
fun_sato=fun_value*100000000
fun_opcode='''\
{OP_DUP}{OP_HASH160}{hashed_Redeem}{OP_EQUAL}\
'''

Redeem='''\
{OP_HASH160}{HASH160(hA)}{OP_EQUAL}\
{OP_IF}{OP_2}{B1PubKey}{A1PubKey}{OP_2}{OP_CHECKMULTISIG}{OP_ELSE}\
{Ttime}{OP_CHECKSQUENCEVERIFY}{OP_DROP}{B2PubKey}{OP_CHECKSIG}\
{OP_ENDIF}\
'''
hashed_Redeem=hash160(Redeem)



fundingtransaction = {
        "version": 1,
		"lock_time": 0,
		"inputs": [
			{
				"txid_prev": fun_unspent_txid1,
				"script_sig":fun_sig1,
				"sequence": fun_seq1,
			},
            {
				"txid_prev": fun_unspent_txid2,
				"script_sig": fun_sig2,
				"sequence": fun_seq2
			},
		],
		"outputs": [
			{
				"value": fun_value,
				"script_pub": fun_opcode,
			},
		]
	}