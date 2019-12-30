# import sys
# print(sys.path)

from selenium import webdriver
from datetime import datetime
import re


class SeashellBookflare:
    def __init__(self, lastdate):
        self.lastdate = self.toDate(lastdate)
        self.done = False

    def process(self):

        # driver = webdriver.PhantomJS(service_args=['--load-images=no'])
        # drv = webdriver.PhantomJS(service_args=['--load-images=no'])

        # from selenium.webdriver.firefox.options import Options
        # options = Options()
        # options.headless=True
        # driver = webdriver.Firefox(options=options)
        # drv = webdriver.Firefox(options)

        options = webdriver.ChromeOptions()
        prefs = {'profile.managed_default_content_settings.images': 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        drv = webdriver.Chrome(options=options)

        driver.implicitly_wait(10)
        drv.implicitly_wait(10)

        f = open('urls-Bookflare.txt', 'a', encoding="utf-8")

        i = 1
        while not self.done:
            self.done = True
            start_i = "https://bookflare.org/page/" + str(i) + "/"
            print(start_i)
            driver.get(start_i)
            elems = driver.find_elements_by_xpath('//a[@rel="bookmark"]')
            j = 0
            for elem in elems:
                # print(elem.get_attribute("href"))
                # self.processitem(drv, elem)
                j = j + 1

                if self.isnew(driver.find_element_by_xpath("(//time)[" + str(j) + "]").get_attribute("datetime")):
                    print(elem.text)
                    f.write('*' * 50 + '\n')
                    f.write('Todo ')
                    f.write(elem.text)
                    f.write('\n')
                    f.write(elem.get_attribute("href"))
                    f.write('\n' + '*' * 50 + '\n')
                    self.processitem(drv, elem, f)
                    self.done = False
                else:
                    self.done = True
                    break
            i += 1
            if i==226:
                self.done = True

        f.close()
        drv.close()
        driver.close()

    def processitem(self, driver, elem, f):
        itemurl = elem.get_attribute("href")
        driver.get(itemurl)
        # elems = driver.find_elements_by_xpath('//*[@id="content"]/div[2]/article/div/div[2]/div[1]/p[2]/a')
        # elems = driver.find_elements_by_xpath('//a[@rel="noopener"]')
        elems = driver.find_elements_by_css_selector("a[rel^='noopener']")

        if len(elems)==0:
            f.write("###"+itemurl)
            f.write('\n')
            print("###"+itemurl)
        else:
            for e in elems:
                # print(e.text)
                if e.tag_name == "a":
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
        # timetxt = timetxt.replace("th", "").replace("nd", "").replace("rd", "").replace("st", "")
        return datetime.strptime(timetxt, '%Y-%m-%d %H:%M:%S')

    def isnew(self, timetxt):
        strs = timetxt.split(',')
        # if "Yesterday" in timetxt or "Today" in timetxt or "ago" in timetxt:
        #     return True
        pdatetime = self.toDate(timetxt)
        return pdatetime >= self.lastdate


z = SeashellBookflare("2019-12-29 19:13:40")
z.process()
