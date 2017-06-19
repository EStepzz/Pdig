#coding = utf-8
'''
@author:QINWAANG
'''
import dns.resolver

class Pdig:
    def __init__(self,domain, type):
        self.type = type
        self.domain = domain
        self.nameserver = '114.114.114.114'

    def dig(self):
        query = dns.message.make_query(self.domain, self.type)
        response = dns.query.udp(query, self.nameserver, timeout=4)
        print('***************')
        print (response)
        print ("nameserver:{}".format(self.nameserver))
       # print (query)




if __name__ =='__main__':
    dig = Pdig('www.baidu.com.','A')
    dig.dig()