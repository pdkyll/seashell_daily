# import sys
# print(sys.path)

from selenium import webdriver
from datetime import datetime
import re


class SeashellMobilism:
    def __init__(self, lastdate):
        self.lastdate = self.toDate(lastdate)
        self.done = False
        self.kws = ['x86', 'iconpack', 'icon pack', 'KLWP', 'WhatsApp', 'facebook', 'Substratum', 'GO Launcher', 'Hindi',
                    'Dictionary', 'Learn English', 'Smart Launcher', 'P Launcher', 'Twitter', 'Spanish', 'French',
                    'Netflix', 'Gboard', 'Microsoft Launcher', 'Turbo Launcher', 'Chrooma', 'Fleksy',
                    'Launcher Oreo', 'Google Drive', 'MosaLingua', 'ATV Launcher', 'Total Launcher', 'Drivemode',
                    'German', 'Dropbox', 'Memrise', 'EMUI', 'Nougat Launcher', 'icons', 'X Launcher', 'Arc Launcher',
                    'CM Launcher', 'KWGT', 'Pie Launcher', 'POCO Launcher', 'Portuguese', 'Indonesian', 'Chinese',
                    'Italian', 'Swedish', 'Dutch', 'Danish', 'Catalan', 'Russian', 'Arabic',
                    'Romanian', 'Latin', 'Filipino', 'Korean', 'S8 Launcher', 'Language Learning', 'Prayer']
        self.lkws = ('http://www.opera.com', 'https://www.facebook.com', 'https://twitter.com', 'https://t.me',
                     'https://plus.google.com', 'http://www.audiomack.com', 'https://instagram.com',
                     'https://www.instagram.com', 'http://instagram.com', 'https://docs.google.com',
                     'https://www.youtube.com', 'http://twitter.com', 'http://www.bbc.co.uk', 'http://www.fotmob.com',
                     'http://www.facebook.com', 'http://www.machapp.net', 'http://machapp.net',
                     'http://www.reactle.com', 'http://developer.samsung.com', 'https://icons8.com',
                     'http://www.camscanner.com', 'http://www.elephantsdream.org', 'http://www.bigbuckbunny.org',
                     'http://forum.xda-developers.com', 'http://tubemate.net', 'https://books.fbreader.org',
                     'http://truecaller.com/', 'http://iconhandbook.co.uk', 'http://talk.sonymobile.com',
                     'https://powerbrowserapp.com', 'http://wordswag.co', 'https://travel.sygic.com',
                     'http://www.mycarly.com', 'http://support.mycarly.com', 'http://yatse.tv', 'http://kodi.tv',
                     'http://creativecommons.org', 'https://www.boutiqueobdfacile.com',
                     'http://www.outilsobdfacile.com', 'http://bit.ly', 'http://ugl.flashlight.de',
                     'http://www.adobe.com', 'http://www.fstopapp.com', 'http://gromaudio.com', 'http://tubemate.net',
                     'https://youtu.be', 'https://paranoiaworks.mobi', 'https://pteo.paranoiaworks.mobi',
                     'http://www.caristaapp.com', 'http://www.caristaapp.com', 'http://www.ipndata.sk',
                     'https://play.google.com', 'https://morecast.com', 'http://www.morecast.com',
                     'http://www.polarisoffice.com', 'https://getsatisfaction.com', 'http://neutronmp.com',
                     'http://forum.bsplayer.com', 'http://www.waze.com', 'http://www.fstopapp.com',
                     'https://github.com', 'http://tasks.org', 'http://www.flaticon', 'http://www.garmin.com',
                     'http://www.navigon.com', 'https://zenmate.com', 'https://facebook.com', 'https://vk.com',
                     'http://youtu.be', 'http://code.google.com', 'https://market.android.com',
                     'https://support.google.com', 'https://chrome.google.com', 'https://www.twitter.com',
                     'http://www.qobuz.com', 'http://goo.gl', 'http://forum.mobilism.org', 'http://youtube.com',
                     'http://sleep.urbandroid.org')

    def process(self):

        # driver = webdriver.PhantomJS(service_args=['--load-images=no'])
        # drv = webdriver.PhantomJS(service_args=['--load-images=no'])

        # firefox_profile = webdriver.FirefoxProfile()
        # firefox_profile.set_preference('permissions.default.image', 2)
        # firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
        # options = webdriver.FirefoxOptions()
        # options.add_argument("--headless")
        # driver = webdriver.Firefox(firefox_profile=firefox_profile,firefox_options=options)
        # drv = webdriver.Firefox(firefox_profile=firefox_profile,firefox_options=options)

        options = webdriver.ChromeOptions()
        prefs = {'profile.managed_default_content_settings.images': 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        drv = webdriver.Chrome(options=options)

        driver.implicitly_wait(10)
        drv.implicitly_wait(10)

        f = open('urls-Mobilism.txt', 'a', encoding="utf-8")

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


mob = SeashellMobilism("Aug 20th, 2019, 6:17 pm")
mob.process()
# https://forum.mobilism.org/viewforum.php?f=399
# https://forum.mobilism.org/viewtopic.php?f=427&t=3271918