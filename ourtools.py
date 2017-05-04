# -*- coding: utf-8 -*-
import oursql
from requests import post
from json import loads,dumps
class Get_Account:
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
        pass

# def test():
#     myaccount=Get_Account()
#     res=myaccount.get_account()
#     print type(res)
def sayhello():
    print "hello"




if __name__=='__main__':
    myaccount=Get_Account()
    res=myaccount.get_account()
    print type(res)
    myaccount.save2sql()


# myaccount=Get_Account()
# res=myaccount.get_account()
# print type(res)