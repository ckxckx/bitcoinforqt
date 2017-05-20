# -*- coding: utf-8 -*-


from bitcoin import *
i=0    #i为0时候表示只有一个输入,注意这和我们认为1不太一样
hashcode=1


######################################以下是个例子#################
tx="0100000001c838044a55e46aeb90ba1ec000668365\
5dab84f43bf2c91f001830f4a55b538c0000000000ffffffff02002f68590\
00000001976a914d166d4ac217f0d51b7ab7a7919f273ac880eabc388ac73f\
7993b000000001976a914466d50fb3570699486ad8c9ee363ccf275abfa7f88ac00000000"

addr_ckx1="mmwLYuyQAByvECp7FKnMWH5R1ZdeeBhFnL"
priv="cRLEkT5nko6DjSRQSe9jk8xmuK7DVhtLREcdS51uR1FKhfkQJFCd"

true_sig="0100000001c838044a55e46aeb90ba1ec0006683655dab84f43bf2c91f00183\
0f4a55b538c000000006a47304402205b316c1c800f858894ef3a31a0a23b0b71a\
dffe2da9b3ffcf08ef3873eaa984102207ee2045a740c30f7826\
5d676b14e5cab627f3a35e93efba378749dea7a2b0d820121024353283ff978ca37a35e6a06\
25666094c43a94810092bcbec98d82440f381e5effffffff02002f6859000000001976a914d166d4ac217f0d51b7ab7a7919f273ac880eabc388ac73f7993b000000001976a914466d50fb3570699486ad8c9ee363ccf275abfa7f88ac00000000"
###################################################################
# i = int(i)
# if len(priv) <= 33:
# 	priv = safe_hexlify(priv)
# print 'priv is :'
# print priv
# pub = privkey_to_pubkey(priv)
# print 'pub is:'
# print pub
# address = pubkey_to_address(pub,111)
# print 'address is :'
# print address
#
# signing_tx = signature_form(tx, i, mk_pubkey_script(address), hashcode)
# sig = ecdsa_tx_sign(signing_tx, priv, hashcode)
# txobj = deserialize(tx)
# txobj["ins"][i]["script"] = serialize_script([sig, pub])
# re=serialize(txobj



def oursign(tx, i, priv, hashcode=1):
    i = int(i)
    if (not is_python2 and isinstance(re, bytes)) or not re.match('^[0-9a-fA-F]*$', tx):
        return binascii.unhexlify(sign(safe_hexlify(tx), i, priv))
    if len(priv) <= 33:
        priv = safe_hexlify(priv)
    pub = privkey_to_pubkey(priv)
    address = pubkey_to_address(pub,111)
    signing_tx = signature_form(tx, i, mk_pubkey_script(address), hashcode)
    sig = ecdsa_tx_sign(signing_tx, priv, hashcode)
    txobj = deserialize(tx)
    txobj["ins"][i]["script"] = serialize_script([sig, pub])
    return serialize(txobj)


re=oursign(tx,i,priv)

if re==true_sig:
	print 'ssss'
else:
	print len(re)
	print len(true_sig)
	print 'ffff'
	print true_sig
	print re
