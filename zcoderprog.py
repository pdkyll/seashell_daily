# import sys
# print(sys.path)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import re
import time

class SeashellCoderprog:
    def __init__(self, stoptitle):
        self.stoptitle = stoptitle
        self.done = False
        self.pt = 3
        self.pagesize = 5

    def process(self):

        options = webdriver.ChromeOptions()
        prefs = {'profile.managed_default_content_settings.images': 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        drv = webdriver.Chrome(options=options)

        driver.implicitly_wait(self.pt)
        drv.implicitly_wait(self.pt)

        fb = open('urls-Coderprog-books.txt', 'a', encoding="utf-8")
        fv = open('urls-Coderprog-videos.txt', 'a', encoding="utf-8")

        i = 1
        while not self.done:
            start_i = "https://coderprog.com/page/" + str(i)
            print("\n")
            print(start_i)
            driver.get(start_i)
            elems = driver.find_elements_by_id("featured-thumbnail")
            for elem in elems:
                title = elem.get_attribute("title")
                if title == self.stoptitle:
                    self.done = True
                    print("Meet last done")
                    break

                print(elem.get_attribute("href"))

                self.processitem(drv, elem, fb, fv)
                time.sleep( 0.5 )

            i += 1

        fb.close()
        fv.close()
        drv.close()
        driver.close()

    def processitem(self, driver, elem, fb, fv):

        itemurl = elem.get_attribute("href")
        driver.get(itemurl)
        f = fv
        try:
            driver.find_element_by_css_selector("a[title='View all posts in Video']")
        except:
            f = fb

        f.write('*' * 50 + '\n')
        f.write(elem.get_attribute("title"))
        f.write('\n' + '*' * 50 + '\n')

        elems = driver.find_elements_by_css_selector("div.thecontent a")

        for e in elems:
            e.click()
            # f.write(e.get_attribute("href"))
            # #self.processlink(driver,e.get_attribute("href"))
            # f.write('\n')
        furl = "";
        for h in driver.window_handles:
            if not furl:
                furl = h
                continue
            driver.switch_to.window(h)
            # print(driver.current_url)
            f.write(driver.current_url)
            f.write('\n')
            driver.close()
        driver.switch_to.window(furl)
        f.write('\n')

    # def processlink(self,driver,url):
    #     driver.get(url)
    #     print(driver.current_url)


mob = SeashellCoderprog("Computer Graphics Programming in OpenGL with JAVA, 2nd Edition")
mob.process()
