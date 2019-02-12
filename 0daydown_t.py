# import sys
# print(sys.path)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import re


class Seashell0daydownT:
    def __init__(self, stopurl):
        self.stopurl = stopurl
        self.done = False
        self.pt = 3


    def process(self):

        options = webdriver.ChromeOptions()
        prefs = {'profile.managed_default_content_settings.images': 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        drv = webdriver.Chrome(options=options)

        driver.implicitly_wait(self.pt)
        drv.implicitly_wait(self.pt)

        f = open('urls0daydown-Tutorials.txt', 'a', encoding="utf-8")

        i = 1
        while not self.done:
            start_i = "https://www.0daydown.com/category/tutorials/page/" + str(i)
            print("\n")
            print(start_i)
            driver.get(start_i)
            elems = driver.find_elements_by_class_name("thumbnail")
            for elem in elems:

                url = elem.get_attribute('href')
                if url == self.stopurl:
                    self.done = True
                    break

                #print(elem.get_attribute("href"))

                self.processitem(drv, elem, f)

            i += 1

        f.close()
        drv.close()
        driver.close()

    def processitem(self, driver, elem, f):

        itemurl = elem.get_attribute("href")
        driver.get(itemurl)

        title = elem.find_element_by_css_selector('img').get_attribute('alt')
        f.write('*' * 50 + '\n')
        f.write(title)
        f.write('\n')
        f.write(itemurl)
        f.write('\n' + '*' * 50 + '\n')

        elems = driver.find_elements_by_class_name("external")

        for e in elems:
            f.write(e.get_attribute("href"))
            f.write('\n')
        f.write('\n')


mob = Seashell0daydownT("https://www.0daydown.com/11/961646.html")
#mob = Seashell0daydownT("https://www.0daydown.com/02/996438.html")

mob.process()
