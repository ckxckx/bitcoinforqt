# -*- coding: utf-8 -*-
from requests import post
class Get_Account:

    url="https://api.blockcypher.com/v1/btc/test3/addrs"
    def __init__(self):
        self.pri_key="xxx"
        self.pub_key="xxx"
        self.addr="xxx"
        self.wif="xxx"
    def get_account(self):
        res=post(self.url)

        return res.content


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


# myaccount=Get_Account()
# res=myaccount.get_account()
# print type(res)