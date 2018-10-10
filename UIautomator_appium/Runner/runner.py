# -*- coding: utf-8 -*-

__author__ = 'Baob'

import sys
sys.path.append(r"C:\Users\baobao.lu\Downloads\UIautomator_appium")

import platform
from Base.BaseAndroidPhone import *
from Base.BaseAdb import *
from Base.BaseRunner import ParametrizedTestCase
from TestCase.HomeTest import HomeTest
from Base.BaseAppiumServer import AppiumServer
from multiprocessing import Pool
import unittest
from Base.BaseInit import init, mk_file
from Base.BaseStatistics import countDate, writeExcel, countSumDevices
from Base.BasePickle import *
from datetime import datetime
from Base.BaseApk import ApkInfo
from Base.BaseEmail2 import send_mail


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def load_file():
    # 获取当前文件路径
    current_path = os.path.abspath(__file__)
    # 获取当前文件的父目录
    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
    print('当前目录:' + current_path)
    print('当前父目录:' + father_path)


def kill_adb():
    if platform.system() == "Windows":
        # os.popen("taskkill /f /im adb.exe")
        os.system(PATH("../app/kill5037.bat"))
        # 针对杀掉adb进程同时夜神模拟器进程也被杀掉问题，所以需要重新连接夜神模拟器，不是模拟器时此行代码注释掉，待调试
        os.popen("adb connect 127.0.0.1:62001")
    else:
        os.popen("adb kill-server")
        # 此命令无效
        # os.popen("killall adb")
        # 针对杀掉adb进程同时夜神模拟器进程也被杀掉问题，所以需要重新连接夜神模拟器，不是模拟器时此行代码注释掉，待调试
        os.popen("adb connect 127.0.0.1:62001")
    os.system("adb start-server")

def runnerPool(getDevices):
    devices_Pool = []

    for i in range(0, len(getDevices)):
        _pool = []
        _initApp = {}
        _initApp["deviceName"] = getDevices[i]["devices"]
        _initApp["platformVersion"] = getPhoneInfo(devices=_initApp["deviceName"])["release"]
        _initApp["platformName"] = "android"
        _initApp["port"] = getDevices[i]["port"]
        # 解决uiautomator2报错问题
        _initApp["automationName"] = "uiautomator2"
        _initApp["systemPort"] = getDevices[i]["systemPort"]

        _initApp["app"] = getDevices[i]["app"]
        apkInfo = ApkInfo(_initApp["app"])
        _initApp["appPackage"] = apkInfo.getApkBaseInfo()[0]
        _initApp["appActivity"] = apkInfo.getApkActivity()

        # 解决selenium.WebDriverException: Unable to launch the app: Error: Trying to start logcat capture but it's already started!
        _initApp["autoLaunch"] = False


        _pool.append(_initApp)
        devices_Pool.append(_initApp)

    pool = Pool(len(devices_Pool))
    pool.map(runnerCaseApp, devices_Pool)
    pool.close()
    pool.join()


def runnerCaseApp(devices):
    starttime = datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(HomeTest, param=devices))
    # suite.addTest(ParametrizedTestCase.parametrize(HomeTest, param=devices)) #加入测试类
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((endtime - starttime).seconds) + "秒")

if __name__ == '__main__':

    # kill_adb()

    devicess = AndroidDebugBridge().attached_devices()
    if len(devicess) > 0:
        mk_file()
        l_devices = []
        for dev in devicess:
            app = {}
            app["devices"] = dev
            init(dev)
            app["port"] = str(random.randint(4700, 4900))
            app["bport"] = str(random.randint(4700, 4900))
            app["systemPort"] = str(random.randint(4700, 4900))
            # 需要测试的app路径
            app["app"] = r"C:\Users\baobao.lu\Downloads\com.tencent.qqmusic_866.apk"
            print('1111111111111111111111')
            l_devices.append(app)

        appium_server = AppiumServer(l_devices)
        appium_server.start_server()
        runnerPool(l_devices)
        writeExcel()
        appium_server.stop_server(l_devices)

        # to_addr = ["lubaobao_v@didichuxing.com",'751500349@qq.com']
        # mail_host = "mail.didichuxing.com"
        # mail_user = "lubaobao_v@didichuxing.com"
        # mail_pass = '!Ni8zhidao!'
        #
        # port = "587"
        # header_msg = "接口测试"
        # attach = "接口测试"
        # report = PATH("../Report/report.xlsx")
        # send_mail(to_addr=to_addr, mail_host=mail_host, mail_user=mail_user, port=port, mail_pass=mail_pass,
        #           header_msg=header_msg, report=report, attach=attach, report_name="接口测试报告.xlsx")

    else:
        print("没有可用的安卓设备")


