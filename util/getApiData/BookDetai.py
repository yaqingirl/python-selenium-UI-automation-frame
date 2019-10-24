#coding=utf-8
import json
import re

from config.server_info import api_bookdetail
import requests

def getData(ebookid):

    data={
        't':'1',
        'app':'jdread-m',
        'tm':'156073870884',
        'index':'0',
        'size':'20',
        'os':'web',
        'client':'android',
        'uuid':'ade6b834ea54428680e9cc8441415d8a1',
        'sign':'1613f0371e27f2cc0b1cd906925a4c531'
    }

    header={
        'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36'
    }
    url=api_bookdetail%(ebookid)
    response=requests.get(url,params=data,headers=header)
    # print(response.request.headers)
    # book_list=re.findall(r'"ebook_id":(\d+)',response.text)
    result=json.loads(response.text)['data']

    return result
if __name__=="__main__":

    print(getData('30481326')['file_size'])
    print(getData('30481326')['isbn'])
    print(getData('30481326')['publish_time'])
    print(getData('30481326')['word_count'])
    print(getData('30481326')['format'])
    print(getData('30481326')['edition'])

