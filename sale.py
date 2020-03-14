import unittest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.android import webdriver

class Momoko(unittest.TestCase):
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
    Login()
    def test_sale(self):

        dri = self.dri
        dri.maximize_window()
        dri.get('https://demo.momoko.care/admin/en/order/pos/62475')
        number = random.randrange(31, 40)
        dri.find_element_by_id('boxcategory_'+str(number)).click()
        time.sleep(.5)
        dri.find_element_by_id('ctrl_brand_id').click()
        brand = random.randrange(93, 200)
        dri.find_element_by_css_selector("option[value =]"+str(brand)).click()





if __name__ == '__main__':
    unittest.main()
