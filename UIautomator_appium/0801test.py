# coding=utf-8

# from Base.BaseApk import ApkInfo


# exception test
# file_path = r'C:\Users\baobao.lu\Desktop\新建文本文档22.txt'
# try:
#     with open(file_path,'r') as f:
#         data = f.read()
# except IOError as e:
#     print(e)
# finally:
#     print('Never,最后都执行')

# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# i = 0
# for a in range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if a!=b and b!=c and c!=a:
#                 i+=1
#                 print(a,b,c)
# print(i)
# Answer2
# from itertools import permutations
#
# k = 0
# for i in permutations([1, 2, 3, 4], 3):
#     k += 1
#     print(i)
# print(k)

# 字符串切割
# s = 'adbcd24个字母'
# print(s[0:5])


# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
# 低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提
# 成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

# while True:
#     I = input(r'请输入金额： ')
#     if I.isdigit():
#         print('您输入的金额为：' + I)
#
#         break
#     else:
#         print('请输入正确的金额')


# i = int(input('净利润:'))
# arr = [1000000, 600000, 400000, 200000, 100000, 0]
# rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# r = 0
# for idx in range(0, 6):
#     if i > arr[idx]:
#         r += (i - arr[idx]) * rat[idx]
#         print((i - arr[idx]) * rat[idx])
#         i = arr[idx]
# print(r)

# import os, sys
#
#
# def load_file():
#     # 获取当前文件路径
#     current_path = os.path.abspath(__file__)
#     # 获取当前文件的父目录
#     father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
#     # print('当前目录:' + current_path)
#     # print('当前父目录:' + father_path)
#     return sys.path.append(father_path)
#
#
# print(sys.path)

#test url:  http://192.168.105.118/ccp-web/risk/allProjectList?pageIndex=1&pageSize=99999

import requests
import json
import math
import urllib3

http = urllib3.PoolManager()

# post
# def ceshi():
#     pm = {
#         'UserName': 'chzhah999',
#         'Page': 0,
#         'Pagesize': 21,
#         'Flag': 0,
#         'FingerPrint': 0,
#         'Imei': '99000774954945',
#         'Channel': 'qihoo',
#         'Vendor': 'pcgame',
#         'Version': '10'
#     }
#     url = 'http://pcgame.moban.com/api/GroupSale/GetGroupAttendList.aspx?'
#     r = requests.post(url, data=json.dumps(pm))
#     return r

# test
def ceshi():
    pm = {
        'pageIndex': 1,
        'pageSize': 99999
    }
    headers = {'Cookie': 'token=8a91e48f656add6c01656b8c335400ab'}
    url = 'http://192.168.105.118/ccp-web/common/i18values'
    r = requests.get(url, data=json.dumps(pm), headers=headers)
    # r = requests.get(url, data=json.dumps(pm))
    return r


if __name__ == "__main__":
    r = ceshi()
    re = r._content.decode('utf8')
    print(str(re))
