# import sys
# print(sys.path)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import re
import time


class Seashell0daydownW:
    def __init__(self, stopurl):
        self.stopurl = stopurl
        self.done = False
        self.pt = 3

    def process(self):

        options = webdriver.ChromeOptions()
        prefs = {'profile.managed_default_content_settings.images': 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--headless")
        options.binary_location = "C:/Users/seashell/Desktop/cr-stable/bin/chrome.exe"
        driver = webdriver.Chrome(options=options)
        drv = webdriver.Chrome(options=options)

        driver.implicitly_wait(self.pt)
        drv.implicitly_wait(self.pt)

        f = open('urls-0daydown-Windows.txt', 'a', encoding="utf-8")
        fb = open('urls-0daydown-Windows-b.txt', 'a', encoding="utf-8")

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
        fb.close()
        drv.close()
        driver.close()

    def processitem(self, driver, elem, f, fb):

        itemurl = elem.get_attribute("href")
        driver.get(itemurl)

        title = elem.find_element_by_css_selector('img').get_attribute('alt')
        f.write('*' * 50 + '\n')
        f.write(title)
        f.write('\n')
        f.write(itemurl)
        f.write('\n' + '*' * 50 + '\n')

        print(title)

        elems = driver.find_elements_by_class_name("external")

        count = 0
        for e in elems:
            count = count + 1
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
                if count==1:
                    fb.write(rstr.strip())
                    fb.write('\n')
            else:
                f.write(dlink)
            f.write('\n')
        f.write('\n')

# mob = Seashell0daydownW("https://www.0daydown.com/02/1001971.html")
# mob.process()
