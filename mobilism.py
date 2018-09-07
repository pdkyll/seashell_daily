# import sys
# print(sys.path)

from selenium import webdriver
from datetime import datetime
import re


class SeashellMobilism:
    def __init__(self, lastdate):
        self.lastdate = self.toDate(lastdate)
        self.done = False
        self.kws = ['x86', 'icon pack', 'KLWP', 'WhatsApp', 'facebook', 'Substratum', 'GO Launcher', 'Hindi',
                    'Dictionary', 'Learn English', 'Smart Launcher', 'P Launcher', 'Twitter', 'Spanish', 'French',
                    'Netflix', 'Gboard', 'Microsoft Launcher', 'Turbo Launcher', 'OO Launcher', 'Chrooma', 'Fleksy',
                    'Launcher Oreo', 'Google Drive', 'MosaLingua', 'ATV Launcher', 'Total Launcher', 'Drivemode',
                    'German', 'Dropbox', 'Memrise', 'EMUI', 'Nougat Launcher', 'icons', 'X Launcher', 'Arc Launcher',
                    'CM Launcher', 'KWGT', 'Pie Launcher', 'POCO Launcher', 'Portuguese', 'Indonesian', 'Chinese',
                    'Italian', 'Swedish', 'Dutch', 'Danish', 'Catalan', 'Russian', 'Arabic',
                    'Romanian', 'Latin', 'Filipino', 'Korean', 'S8 Launcher']
        self.lkws = ('http://www.opera.com', 'https://www.facebook.com', 'https://twitter.com', 'https://t.me',
                     'https://plus.google.com', 'http://www.audiomack.com', 'https://instagram.com',
                     'https://docs.google.com', 'https://www.youtube.com', 'http://twitter.com', 'http://www.bbc.co.uk',
                     'http://www.machapp.net', 'http://machapp.net')

    def process(self):
        driver = webdriver.Firefox()
        drv = webdriver.Firefox()
        driver.implicitly_wait(30)
        drv.implicitly_wait(30)

        f = open('urls1.txt', 'a', encoding="utf-8")

        i = 0
        while not self.done:
            self.done = True
            start_i = "https://forum.mobilism.org/viewforum.php?f=399&start=" + str(i)
            print(start_i)
            driver.get(start_i)
            elems = driver.find_elements_by_class_name("topictitle")
            for elem in elems:
                # print(elem.get_attribute("href"))
                ##self.processitem(drv, elem)
                if self.isProcess(elem.text) and self.isnew(
                        elem.find_element_by_xpath("..").find_element_by_xpath("./small").text):
                    print(elem.text)
                    f.write('*' * 50 + '\n')
                    f.write('Todo ')
                    f.write(elem.text)
                    f.write('\n' + '*' * 50 + '\n')
                    self.processitem(drv, elem, f)
                    self.done = False
            i += 40

        f.close()
        drv.close()
        driver.close()

    def processitem(self, driver, elem, f):
        itemurl = elem.get_attribute("href")
        driver.get(itemurl)
        elems = driver.find_elements_by_class_name("postlink")
        for e in elems:
            # print(e.text)
            if e.tag_name == "a" and self.isLink(e.get_attribute("href")):
                f.write(e.get_attribute("href"))
                f.write('\n')

    #     def processitem(self, driver, elem):
    #
    #         itemurl = elem.get_attribute("href")
    #         driver.get(itemurl)
    #         elem = driver.find_element_by_class_name("icon-time")
    #         par = elem.find_element_by_xpath("..")
    # #        if self.isnew(par.text):
    #         print(par.text)

    def toDate(self, timetxt):
        timetxt = timetxt.replace("th", "").replace("nd", "").replace("rd", "").replace("st", "")
        return datetime.strptime(timetxt, '%b %d, %Y, %I:%M %p')

    def isnew(self, timetxt):
        strs = timetxt.split(',')
        if "Yesterday" in timetxt or "Today" in timetxt or "ago" in timetxt:
            return True
        pdatetime = self.toDate(timetxt)
        return pdatetime >= self.lastdate

    def isProcess(self, title):
        for kw in self.kws:
            if re.search(kw, title, re.IGNORECASE):
                return False
        return True

    #         return any(re.search(kw, title, re.IGNORECASE) for kw in self.kws)

    def isLink(self, linkhref):
        # for kw in self.lkws:
        #     if linkhref.startswith(kw):
        #         return False
        # return True
        return not linkhref.startswith(self.lkws)


mob = SeashellMobilism("Sep 4th, 2018, 7:32 pm")
mob.process()
