# for i in range(21, 35):
#     print("http://xunleib.zuida360.com/1805/逆缘国语-"+str(i).zfill(2)+".mp4")


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.binary_location = "C:/Users/seashell/Desktop/cr-stable/bin/chrome.exe"
driver = webdriver.Chrome(options=options)

driver.get(url='https://www.google.com/recaptcha/api2/demo')

# find iframe
captcha_iframe = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located(
        (
            By.TAG_NAME, 'iframe'
        )
    )
)

ActionChains(driver).move_to_element(captcha_iframe).click().perform()

# click im not robot
captcha_box = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located(
        (
            By.ID, 'g-recaptcha-response'
        )
    )
)

driver.execute_script("arguments[0].click()", captcha_box)