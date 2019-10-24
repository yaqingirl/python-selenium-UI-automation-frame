#coding=utf-8
import re

from config.server_info import api_my_books
import requests

def getData(pin):

    data={
        't':'1',
        'p':'1',
        'app':'jdread-m',
        'tm':'156073870884',
        'search_type':'1',
        'search_key':'',
        'index':'0',
        'size':'20',
        'os':'web',
        'client':'ios',
        'uuid':'ade6b834ea54428680e9cc8441415d8a1',
        'sign':'1613f0371e27f2cc0b1cd906925a4c531'
    }

    data['pin']=pin
    header={
        'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36'
    }
    url=api_my_books
    response=requests.get(url,params=data,headers=header)
    # print(response.request.headers)
    book_list=re.findall(r'"ebook_id":(\d+)',response.text)
    return book_list
if __name__=="__main__":

    print(getData('yaqingirl'))