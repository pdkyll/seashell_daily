import os
import sys
import zipfile
import re


def getAppBaseInfo(apkpath):
    # 检查版本号等信息
    output = os.popen("/opt/android-sdk/build-tools/28.0.0/aapt d badging %s" % apkpath).read()
    match = re.compile(
        "package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)' platformBuildVersionName='\S+'").match(output)
    if not match:
        raise Exception("can't get packageinfo")

    packagename = match.group(1)
    versionCode = match.group(2)
    versionName = match.group(3)

    print('packagename:' + packagename)
    print('versionCode:' + versionCode)
    print('versionName:' + versionName)

    # 获得所有的权限
    outList = output.split('\n')
    for line in outList:
        if line.startswith('uses-permission:'):
            print(line.split('=')[1])


def getCurrentDirApk():
    for dir in os.walk(os.curdir):
        for filename in dir[2]:
            if os.path.splitext(filename)[1] == '.apk':
                print('find apk:', filename)
                return filename


def insertFile(apkName, f):
    output = os.popen("./aapt a %s %s" % (apkName, f)).read()


def getApk():
    for dir in os.walk('/download/00000jd/000ph/1_3.apk'):
        for filename in dir[2]:
            if os.path.splitext(filename)[1] == '.apk':
                print('find apk:', filename)
                return filename


getAppBaseInfo("/download/00000jd/000ph/3D_Photo_Effect_0.2.apk")


# mypath = '/download/00000jd/000ph/11111/'
#
# for (dirpath, dirnames, filenames) in os.walk(mypath):
#     for x in filenames:
#         os.rename(mypath + x, mypath + re.sub(r' +', '_', x))
#     break
#
#
# for dir in os.walk(mypath):
#     for filename in dir[2]:
#         if os.path.splitext(filename)[1] == '.apk':
#             print('find apk:', filename)
#             # return filename
#             print(dir[0] + filename)
#             getAppBaseInfo(dir[0]+ filename)

# if __name__ == "__main__":
#     # 获得apk名
#     if len(sys.argv) == 1:
#         apkName = getCurrentDirApk()
#     else:
#         apkName = sys.argv[1]
#     if not apkName:
#         print('can not find apk!!!')
#         exit()
#     getAppBaseInfo(apkName)
#
#     # 向apk中插入文件
#     insertfile = 'insertfile.txt'
#     f = open(insertfile, "w+")
#     f.write('hello android')
#     f.close()
#     insertFile(apkName, insertfile)
#     print('======================')
#     # 检查是否包含某个文件
#     z = zipfile.ZipFile(apkName)
#     for file in z.namelist():
#         if file == insertfile:
#             print('find ', insertfile, " in apk ", apkName)
