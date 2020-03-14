import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

def Login(user):
    global dri
    dri = webdriver.Chrome()
    dri.get('https://demo.momoko.care/admin/')
    time.sleep(.5)
    dri.find_element_by_name('ctrl_email').send_keys('test')
    x = dri.find_element_by_id('ctrl_password')
    x.send_keys('test123')
    x.submit()
    dri.get('https://demo.momoko.care/admin/en/order/pos/62475')

Login("y")
#dri = webdriver.Chrome()
number = random.randrange(31, 40)
dri.find_element_by_id('boxcategory_' + str(number)).click()
time.sleep(.5)
dri.find_element_by_id('ctrl_brand_id_chosen').click()
pro = dri.find_element_by_id('ctrl_brand_id_chosen').find_element_by_css_selector('div:nth-child(2) > div:nth-child(1) > input:nth-child(1)')
pro.send_keys('gucci')
pro.send_keys(Keys.ENTER)
dri.find_element_by_id('ctrl_model').send_keys('TestModel')
num = random.randrange(0, 99)
dri.find_element_by_id('ctrl_serialno').send_keys('TestNo.'+str(num))
c = dri.find_element_by_class_name('chosen-choices')
c.click()
dri.find_element_by_xpath("//div[@id='ctrl_color_chosen'/ul[1]/li[1]/input").send_keys('ทอง')
'''time.sleep(.3)
c.send_keys(Keys.ARROW_DOWN)
c.send_keys(Keys.ARROW_DOWN)
c.send_keys(Keys.ENTER)
'''
print("passed")

print('boxcategory_' + str(number))
print('gucci')
print('TestModel')
print('TestNo.'+str(num))
print('')