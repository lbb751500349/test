::解决adb端口5037被占用问题,参考地址：https://www.cnblogs.com/handaxing/p/7017776.html

@echo off
color a
title ReleaseAdbPort
echo ======================
echo *** Baob 2018-08-13***
echo ***     v1.0.0     ***
echo ======================
echo ---------------------------
echo Checking adb port...
for /F "usebackq tokens=5" %%a in (`"netstat -ano | findstr "5037""`) do (   
if not "%%a" =="0" call :ReleasePort %%a
)
echo ---------------------------
echo adb port has been released!
echo ---------------------------


exit

:ReleasePort
TASKKILL /f /PID %1