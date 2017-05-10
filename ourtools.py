# -*- coding: utf-8 -*-
import oursql
from requests import post
from json import loads,dumps
from blockcypher import get_address_overview, send_faucet_coins
from blockcypher import create_unsigned_tx, make_tx_signatures,get_input_addresses
from blockcypher import broadcast_signed_transaction
import sqlite3
from ouretc import *
#you can use help(class) to get deep understanding of our tools

class Get_Account:
    '''
    Get_Account has several function to help us establish our accounts in testnet
    after 创建一个实例
    1. you should use get_account() to gain several tips of messages
    2. save2sql()
    3. use printourparas() you can print all the items after you get some information from remote api
    '''
    res=''
    res_dict={}
    saveunit=()
    id=0

    url="https://api.blockcypher.com/v1/btc/test3/addrs"
    def __init__(self):
        self.priv_key="xxx"
        self.pub_key="xxx"
        self.addr="xxx"
        self.wif="xxx"

    def get_account(self):
        self.res=post(self.url)

        self.res_dict=loads(self.res.content)
        ####一定要将utf-8解码成assic，在insert过程中
        self.priv_key=self.res_dict["private"].encode('raw_unicode_escape')
        self.addr=self.res_dict["address"].encode('raw_unicode_escape')
        self.pub_key=self.res_dict["public"].encode('raw_unicode_escape')
        self.wif=self.res_dict["wif"].encode('raw_unicode_escape')



     #   self.wif=self.wif.encode('raw_unicode_escape')
        self.saveunit=(self.priv_key,self.pub_key,self.addr,self.wif)
        self.id=abs(hash(str(self.saveunit)))
        self.saveunit=(self.id,self.priv_key,self.pub_key,self.addr,self.wif)
        #print self.saveunit
        return self.res.content

    def save2sql(self):
        key = str(self.saveunit)
        oursql.insert_one_ckx(key)
        #print flag

    def printourparas(self):
        try:
            print self.res.content
        except:
            print 'no paras got!'
def query_address_assets(address):
    '''
    :param address: input address
    :return: assets below this address
    '''
    res = get_address_overview(address,'btc-testnet')
    print res
    return res
def query_address_in_sql(n):
    '''

    :param n: the number of address to display
    :return: temporarily is none
    '''


    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()

    # 第一种：retrieve one record
    try:
        c.execute('select * from account order by id desc')
        for i in range(n):
            print(c.fetchone()[3])  #第1条记录
    except:
        print 'n is too large to display all!!' #第2条记录


    conn.commit()
    conn.close()
def show_me_the_money(money=400000,addr=myaddr1):
    '''
    :param money: everytime < 500,000, total < 100,000,000
    :return:
    '''
    # addr="mgN94Z7hRWy4UfZHTj2T8hZd1BctusLkps"
   # addr="mzPnKxCTMF3Dx9Nx9ktZ6n72LFheEX3MpQ"
    token=mytoken
    send_faucet_coins(address_to_fund=addr,\
                  api_key=token,\
                  coin_symbol='btc-testnet',\
                  satoshis=money)
    print 'money is done !'
def our_create_txt(account_in,account_out):
    '''
    :param account_in,数组:
    :param account_out:
    :example:       account_in=[mypriv1,mypub1,myaddr1]
                    account_out=[myaddr2]
    '''
    inputs = [{'address':account_in[2]}, ]
    outputs = [{'address': account_out[0], 'value': 1}]
    unsigned_tx = create_unsigned_tx(inputs=inputs,\
                                     outputs=outputs, \
                                     coin_symbol=flag,\
                                     api_key=mytoken)
    num=len(get_input_addresses(unsigned_tx))
 #   print unsigned_tx
#    print unsigned_tx
  #  return unsigned_tx

    privkey_list=[account_in[0]]*num
    pubkey_list=[account_in[1]]*num
    #签名
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
    #print kk
    print "successed!"
  #  return kk


# class our_Transaction:
#     def __init__(self):
#         pass



####this area is for testing code###
def test_Get_Account():
    myaccount=Get_Account()
   # myaccount.printourparas()
    res=myaccount.get_account()
    print type(res)
    myaccount.save2sql()
    myaccount.printourparas()



def test_our_create_txt():
    account_in=[mypriv1,mypub1,myaddr1]
    account_out=[myaddr2]
    our_create_txt(account_in,account_out)
#############testing code #########ru



if __name__=='__main__':
    pass

