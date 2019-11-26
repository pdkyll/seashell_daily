# import sys
# print(sys.path)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import re
import time
import json
import os


class Seashell0daydownW:
    def __init__(self, stopurl):
        self.stopurl = stopurl
        self.done = False
        self.pt = 3
        self.ditems = []

    def obj_dict(obj):
        return obj.__dict__

    def process(self):

        options = webdriver.ChromeOptions()
        prefs = {'profile.managed_default_content_settings.images': 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--headless")
        # options.binary_location = "C:/Users/seashell/Desktop/cr-stable/bin/chrome.exe"
        driver = webdriver.Chrome(options=options)
        drv = webdriver.Chrome(options=options)

        driver.implicitly_wait(self.pt)
        drv.implicitly_wait(self.pt)

        f = open('urls-0daydown-Windows.txt', 'a', encoding="utf-8")
        fb = open('urls-0daydown-Windows1.txt', 'a', encoding="utf-8")

        i = 1
        while not self.done:
            start_i = "https://www.0daydown.com/category/software/windows/page/" + str(i)
            print("\n")
            print(start_i)
            driver.get(start_i)
            elems = driver.find_elements_by_class_name("thumbnail")

            if len(elems) == 0:
                break

            for elem in elems:

                url = elem.get_attribute('href')
                if url == self.stopurl:
                    self.done = True
                    print("Meet last done")
                    break

                # print(elem.get_attribute("href"))

                self.processitem(drv, elem, f, fb)
                time.sleep(0.5)
            i += 1

        f.close()
        drv.close()
        driver.close()

        fb = open('urls-0daydown-Windows.json', 'a', encoding="utf-8")
        fb.write(json.dumps([ob.__dict__ for ob in self.ditems], ensure_ascii=False))
        fb.close()

    def processitem(self, driver, elem, f, fb):
        ditem = Ditem()

        itemurl = elem.get_attribute("href")
        driver.get(itemurl)

        title = elem.find_element_by_css_selector('img').get_attribute('alt')
        f.write('*' * 50 + '\n')
        f.write(title)
        f.write('\n')
        f.write(itemurl)
        f.write('\n' + '*' * 50 + '\n')

        ditem.title = title
        ditem.url = itemurl

        print(title)

        elems = driver.find_elements_by_class_name("external")

        for e in elems:
            dlink = e.get_attribute("href")

            if "pan.baidu.com" in dlink:
                f.write('###\n\n')
                # rstr = e.find_element_by_xpath('..').text \
                #     .replace("Download 百度云", "\n") \
                #     .replace("链接: ", "\n") \
                #     .replace(" 密码: ", "\n")\
                #     .replace(" 提取码: ", "\n")
                rstr = e.find_element_by_xpath('..').text \
                    .replace("Download 百度云", "")
                f.write(rstr.strip())
                f.write('\n\n###')
                if ditem.bdurl == "":
                    ditem.bdurl = rstr.strip()
                    fb.write(rstr.strip())
                    fb.write("\n")
            else:
                f.write(dlink)
                if ("nitroflare.com" in dlink) and (ditem.bdurl == ""):
                    ditem.filenames.append(dlink.split('/')[-1])
            f.write('\n')
        f.write('\n')
        self.ditems.append(ditem)


class Ditem:
    DEST = "/download/@@@@@@MMMMMM/batch/111/"

    def __init__(self):
        self.title = ""
        self.url = ""
        self.bdurl = ""
        self.filenames = []

    def folderfiles(self, mypath):
        with open('urls-0daydown-Windows.json', 'rb') as json_file:
            data = json.load(json_file)
            for i in data:
                if (len(i['filenames']) > 0) and (len(i['bdurl'])>0):
                    directory = mypath + i['title'].replace("/"," ")
                    for j in i['filenames']:
                        if os.path.exists(mypath + j):
                            if not os.path.exists(directory):
                                os.makedirs(directory)
                            os.rename(mypath + j, directory + "/" + j)
                        j = j.replace("_"," ")
                        if os.path.exists(mypath + j):
                            if not os.path.exists(directory):
                                os.makedirs(directory)
                            os.rename(mypath + j, directory + "/" + j)

    def folderUnFolderFiles(self, mypath):
        for (dirpath, dirnames, filenames) in os.walk(mypath):
            for x in filenames:
                # print(x)
                # print(os.path.splitext(x)[0])
                directory = mypath + os.path.splitext(x)[0]
                directory = directory.replace("_"," ").replace("Downloadly.ir","").replace("[FileCR]","").strip()

                if not os.path.exists(directory):
                    os.makedirs(directory)
                os.rename(mypath + x, directory + "/" + x)
            break

    def replaceinFolder(self, mypath,oldstr,newstr):
        for subdir, dirs, files in os.walk(mypath):
            for dir in dirs:
                newname = dir.replace(oldstr,newstr).strip()
                if dir!=newname:
                    os.rename(mypath + dir, mypath + newname)



# mob = Seashell0daydownW("https://www.0daydown.com/02/1001971.html")
# mob.process()
ff = Ditem()
#ff.folderfiles("/download/@@@@@@MMMMMM/batch/")
#ff.folderUnFolderFiles('/download/0days/')
# ff.replaceinFolder('/download/00000jd/000day/@@@@@SSSSSSSSS/',' [FileCR]','')
ff.folderUnFolderFiles('/download/00000jd/000day/@@@@@SSSSSSSSS/')


