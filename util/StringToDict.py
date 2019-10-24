
# -*- encoding:utf-8 -*-
import re


def string_to_dict(str_d):
    """
    :param str_d: 格式'a=1;b=2;c=3'
    :return: dict {'a':'1','b':'2','c':'3'}
    """
    try:
        str_l=str_d.split(';')
        result={}
        for i in str_l:
            try:
                key=re.match(r'([\s\S]+)=([\s\S]+)',i).group(1)
                value=re.match(r'([\s\S]+)=([\s\S]+)',i).group(2)
                result[key]=value
            except Exception as e:
                print("没有匹配到")
    except Exception as e:
        print("入参格式不对")
    return result
print(string_to_dict('a=1;b=2;c=3'))