
# -*- coding: utf-8 -*-
__author__ = 'Baob'
import os
import re
import math
from math import ceil
import subprocess


# 得到手机信息
def getPhoneInfo(devices):
    cmd = "adb -s " + devices +" shell cat /system/build.prop "
    print(cmd)
    # phone_info = os.popen(cmd).readlines()
    phone_info = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.readlines()
    result = {"release": "5.0", "model": "model2", "brand": "brand1", "device": "device1"}
    # Android版本号
    release = "ro.build.version.release="
    # 设备型号
    model = "ro.product.model="
    # 设备品牌
    brand = "ro.product.brand="
    # 设备名称
    device = "ro.product.device="
    for line in phone_info:
        # 切割phone_info字符串
         for i in line.split():
            # print(i)
            # 注意编码转换
            temp = i.decode()
            # print('222' + str(type(temp)))
            # print(1111111111111111)
            # print(temp.find(release))
            # find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1
            if int(temp.find(release)) >= 0:
                result["release"] = temp[len(release):]
                break
            if temp.find(model) >= 0:
                result["model"] = temp[len(model):]
                break
            if temp.find(brand) >= 0:
                result["brand"] = temp[len(brand):]
                break
            if temp.find(device) >= 0:
                result["device"] = temp[len(device) :]
                break
    print(result)
    return result

# 得到最大运行内存
def get_men_total(devices):
    cmd = "adb -s "+devices+ " shell cat /proc/meminfo"
    get_cmd = os.popen(cmd).readlines()
    men_total = 0
    men_total_str = "MemTotal"
    for line in get_cmd:
        if line.find(men_total_str) >= 0:
            men_total = line[len(men_total_str) +1:].replace("kB", "").strip()
            break
    return int(men_total)
# 得到几核cpu
def get_cpu_kel(devices):
    cmd = "adb -s " +devices +" shell cat /proc/cpuinfo"
    get_cmd = os.popen(cmd).readlines()
    find_str = "processor"
    int_cpu = 0
    for line in get_cmd:
        if line.find(find_str) >= 0:
            int_cpu += 1
    return str(int_cpu) + "核"

# 得到手机分辨率
def get_app_pix(devices):
    result = os.popen("adb -s " + devices+ " shell wm size", "r")
    return result.readline().split("Physical size:")[1]

if __name__=="__main__":
    getPhoneInfo("127.0.0.1:62001")
    print('BaseAndroidPhone errrrrrrrrrrrrrrrrrrrrrrrrrrr')
