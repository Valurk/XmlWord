from click import style
import requests 

from cairo import Status
from termcolor import colored



BLUE = '\033[94m'

print(BLUE + '''
                                                                             
                                                                             
____      ___              ___ ____              ___                     ___ 
`MM(      )M'              `MM `Mb(      db      )d'                     `MM 
 `MM.     d'                MM  YM.     ,PM.     ,P                       MM 
  `MM.   d' ___  __    __   MM  `Mb     d'Mb     d'  _____  ___  __   ____MM 
   `MM. d'  `MM 6MMb  6MMb  MM   YM.   ,P YM.   ,P  6MMMMMb `MM 6MM  6MMMMMM 
    `MMd     MM69 `MM69 `Mb MM   `Mb   d' `Mb   d' 6M'   `Mb MM69 " 6M'  `MM 
     dMM.    MM'   MM'   MM MM    YM. ,P   YM. ,P  MM     MM MM'    MM    MM 
    d'`MM.   MM    MM    MM MM    `Mb d'   `Mb d'  MM     MM MM     MM    MM 
   d'  `MM.  MM    MM    MM MM     YM,P     YM,P   MM     MM MM     MM    MM 
  d'    `MM. MM    MM    MM MM     `MM'     `MM'   YM.   ,M9 MM     YM.  ,MM 
_M(_    _)MM_MM_  _MM_  _MM_MM_     YP       YP     YMMMMM9 _MM_     YMMMMMM_
                                                                             
                                                                             
                                                                             
''') 
url = str(input("Please type a URL: "))
print("")

request1 = {
    'Host': (url),
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"-Not.A/Brand";v="8", "Chromium";v="102"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
}

response = requests.get(url, headers=request1, verify=True)

if response.status_code == 405:

    import requests

    request2 = {
        'Host': (url),
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"-Not.A/Brand";v="8", "Chromium";v="102"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Linux"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Content-Length': '127',
    }

    data = '<?xml version="1.0"encoding="Ã¼tf-8"?>\r\n<methodCall>\r\n<methodName>demo.sayHello</methodName>\r\n<params></params>\r\n</methodCall> '

    response = requests.post(url, headers=request2, data=data, verify=True)

    print("vulnerable!\n")

else:
    print("Not vulnerable!\n")