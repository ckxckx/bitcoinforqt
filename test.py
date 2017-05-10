from ourtools import *
account_in=[mypriv1,mypub1,myaddr1]
account_out=[myaddr2]
our_create_txt(account_in,account_out)
inputs = [{'address':account_in[2]}, ]
outputs = [{'address': account_out[0], 'value': 1}]
unsigned_tx = create_unsigned_tx(inputs=inputs,\
                                 outputs=outputs, \
                                 coin_symbol=flag,\
                                 api_key=mytoken)
num=len(get_input_addresses(unsigned_tx))


privkey_list=[account_in[0]]*num
pubkey_list=[account_in[1]]*num

tx_signatures = make_tx_signatures(txs_to_sign=unsigned_tx['tosign'],\
                                       privkey_list=privkey_list,\
                                       pubkey_list=pubkey_list)
  #  print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
  #  print tx_signatures
kk=broadcast_signed_transaction(unsigned_tx=unsigned_tx, \
                                    signatures=tx_signatures,\
                                    pubkeys=pubkey_list,\
                                    coin_symbol=flag,\
                                    api_key=mytoken)