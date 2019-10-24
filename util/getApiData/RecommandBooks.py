#coding=utf-8
import json
import re

from config.server_info import api_bookdetail, api_recommandbooks
import requests

def getData(ebookid):

    data={
        't':'1',
        'app':'jdread-m',
        'tm':'156073870884',
        'amount':'20',
        'os':'web',
        'client':'android',
        'uuid':'ade6b834ea54428680e9cc8441415d8a1',
        'sign':'1613f0371e27f2cc0b1cd906925a4c531'
    }

    header={
        'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36'
    }
    url=api_recommandbooks%(ebookid)
    response=requests.get(url,params=data,headers=header)
    # print(response.request.headers)
    # book_list=re.findall(r'"ebook_id":(\d+)',response.text)
    result=json.loads(response.text)['data']

    return result
if __name__=="__main__":

    print(getData('30481326'))

    #https://jdread.jd.com/jdread/api/ebook/30145158?
    # app=jdread-m&tm=1564472580235&os=web&client=android&uuid=h5f7fe876b33e20f3e6c86f6101002ebf5&sign=e8250f6d2e57d59a72eb5fae48c7a51c