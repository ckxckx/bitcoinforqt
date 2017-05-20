# -*- coding: utf-8 -*-
from bitcoin import *

fun_unspent_txid1='e7ed45bf641ebb9eed3e1e233ace260b79670a8d9005438ce1418203439551ca'
fun_unspent_txid2='590ae623a4b651a906a8ed6e0c887ab1874f463e82fe08567dc5d56de2112b22'
fun_sig1=''
fun_sig2=''
fun_seq1=4294967295
fun_seq2=4294967295
fun_value=50   #pay attetion：两单交易的输入和要约等于这个输出
fun_sato=fun_value*100000000



A1address='n3XGPwejYFTt4LRpyKa9qozyNnyWvpzg7w'
A2address='mstxxaEx8gEy3t9xhhkdyNy7Aod3pPiYZf'
A3address='mz3kmf7qm6ULtKsLC3wTkmZLrY8wuEXuvg'
B1address='mwbSyGxkkizDZy6fVPrBVLLsck2GUMtfzH'
B2address='mzgPt78dZkJb9pS7onvquqn6WAJL9VfPKd'
B3address='mj5Rz6BsKhJ9BMcewVUeXjNn5iwSMLuJUo'


A1priv='cQ53FHqaaUtUy4ttxVxgGbRGqgGYYMuzk3VEX8XWoa5bnTt61j8Y'
A2priv='cUsbE86a5JgghUyXoxWidKBZ4TUNeDcK51b6X4Wt1TceaRDxXG2r'
A3priv='cPf1yyCzwTr6jSwLf9CZBgVmpX4NnDNJTeLRxxJ7nDpYUUt7Sfry'
B1priv='cW9FQfuyN2x6UTWrf6oPnbQced1LzUEMxdh4KV8oM7BJXmJbEVDx'
B2priv='cUDDH4Ad3wYj4WarenriSB742PqtgsN74kaFEqPrwk772hkdMckf'
B3priv='cNTHD3giBjPA6Fmw7xJrnM5PeDbmwHMs4TBccSzhzRYwUvB1cmYS'

A1pub='02adc5da5ec1d0bcc31ae1527ba763745fe319516469ebe521d5151274db4fc846'
A2pub='0263bb95171e2b66312e00672dcd6aab019c9ab18e64080b3a38d240d0d4350f90'
A3pub='02d4e5b00e6bfd240ba10cffe564176d46b8de2ab6691a47afa40ad4fc31ab27df'
B1pub='03eba92797d6cdd63c15ee3e2fa397b585fee73a13e8d9e2a690dc29c831e526d5'
B2pub='021af82d8ae7e4dd2aac8917d438afbb480aaad327b98183b8475b39ed187f93ed'
B3pub='02239538309dd6097dead78ae1ea6a579684d9ef1119be4d59ed65b84789faaf43'

Ttime='2bf20' #3min转换成毫秒
hA=sha256('wo shi sui ji shu !!!')
hashedhA=hash160(hA)
#
# print privtopub(A2priv)
# print privtopub(A3priv)
# print privtopub(B1priv)
# print privtopub(B2priv)
# print privtopub(B3priv)


def hash160(input):
    return ripemd160(sha256(input))



OP_HASH160='a9'
OP_EQUAL='87'
OP_IF='63',
OP_2='52',
OP_CHECKMULTISIG='ae',
OP_ELSE='67',
OP_CHECKSQUENCEVERIFY='b2',
OP_DROP='75',
OP_CHEKHSIG='ac',
OP_ENDIF='68'



#这个字典放入变动的参数
parms={\
\
'A1PubKey':A1pub,
'A2PubKey':A2pub,
'A3PubKey':A3pub,
'B1PubKey':B1pub,
'B2PubKey':B2pub,
'B3PubKey':B3pub,
'hA':hA,
'Ttime':Ttime,
'HASH160(hA)':hashedhA,
\
}
#这个字典放入OPCODE
d={\
'OP_HASH160':'a9',\
'OP_EQUAL':'87',\
'OP_IF':'63',\
'OP_2':'52',
'OP_CHECKMULTISIG':'ae',\
'OP_ELSE':'67',\
'OP_CHECKSQUENCEVERIFY':'b2',\
'OP_DROP':'75',\
'OP_CHECKSIG':'ac',\
'OP_ENDIF':'68',\
'OP_DUP':'76',
}
#合并两个字典
all_parms=dict(d,**parms)

Redeem='''\
{OP_HASH160}{HASH160(hA)}{OP_EQUAL}\
{OP_IF}{OP_2}{B1PubKey}{A1PubKey}{OP_2}{OP_CHECKMULTISIG}{OP_ELSE}\
{Ttime}{OP_CHECKSQUENCEVERIFY}{OP_DROP}{B2PubKey}{OP_CHECKSIG}\
{OP_ENDIF}\
'''.format(**all_parms)

# Redeem="522103310188e911026cf18c3ce274e0ebb5f95b00\
#     7f230d8cb7d09879d96dbeab1aff210243930746e6ed6552e03359db521b\
#     088134652905bd2d1541fa9124303a41e95621029e03a901b85534ff1e92\
#     c43c74431f7ce72046060fcf7a95c37e148f78c7725553ae"


hashed_Redeem=hash160(Redeem)


# testme="149af61346ce0aa2dffcf697352b4b704c84dcbaff"
# addtodict={'hashed_Redeem':testme}
addtodict={'hashed_Redeem':hashed_Redeem}
all_parms=dict(all_parms,**addtodict)

fun_opcode='''\
{OP_DUP}{OP_HASH160}{hashed_Redeem}{OP_EQUAL}\
'''.format(**all_parms)
# fun_opcode='''\
# {OP_HASH160}{hashed_Redeem}{OP_EQUAL}\
# '''.format(**all_parms)



# Redeem='''\
# {OP_HASH160}{OP_EQUAL}\
# {OP_IF}{OP_2}{OP_2}{OP_CHECKMULTISIG}{OP_ELSE}\
# {OP_CHECKSQUENCEVERIFY}{OP_DROP}{OP_CHECKSIG}\
# {OP_ENDIF}\
# '''.format(**all_parms)

# print Redeem
# print fun_opcode

################################3









fundingtransaction = {
        "version": 1,
		"lock_time": 0,
		"inputs": [
			{
				"txid_prev": fun_unspent_txid1,
				"script_sig":fun_sig1,
                "out_prev":0,
				"sequence": fun_seq1,
			},
            {
				"txid_prev": fun_unspent_txid2,
				"script_sig": fun_sig2,
                "out_prev":0,
				"sequence": fun_seq2
			},
		],
		"outputs": [
			{
				"value": fun_sato,
				"script_pub": fun_opcode,
			},
		]
	}


print fundingtransaction
