"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
Replace this with more appropriate tests for your application.
"""

import time
from django.test import TestCase
from django.test import LiveServerTestCase
#from selenium.webdriver.firefox.webdriver import WebDriver
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from unittest import skip




#binary = FirefoxBinary("C:\'Program Files (x86)'\'Mozilla Firefox'\firefox.exe") 
#browser = WebDriver.Firefox(firefox_binary=binary)


class CreateContactIntegrationTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        #cls.selenium = WebDriver()
        cls.driver = webdriver.Chrome(r'C:\Project\chromedriver.exe')
        cls.driver.get('http://52.49.129.95:8088/')
        super(CreateContactIntegrationTest,cls).setUpClass()
        
    @classmethod
    def tearDownClass(cls):
        #cls.selenium.quit()
        super(CreateContactIntegrationTest,cls).tearDownClass()
     
    @skip("My wish to skip the test")
    def test_login(self):
        
        search_box = self.driver.find_element_by_name('username')
        search_box.send_keys('gelya')
        search_box = self.driver.find_element_by_id('id_password').send_keys("qwerty1234%")
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
                
        #self.assertEqual(Contact.objects.all()[0].login_form, 'admin')
        
        
        
    def test_create_project(self):
        
        search_box = self.driver.find_element_by_name('username')
        search_box.send_keys('gelya')
        search_box = self.driver.find_element_by_id('id_password').send_keys("Qwerty123")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        
        
        time.sleep(2)
        search_box = self.driver.find_element_by_xpath('//i[@class="pe-7s-global"]').click()
        search_box = self.driver.find_element_by_id('id_Search_user__username__icontains').send_keys("Tesco")
        search_box = self.driver.find_element_by_id('id_Search_contact__icontains').send_keys("+395546768933")
        search_box = self.driver.find_element_by_id('id_Search_name__icontains').send_keys("Katya")
        search_box = self.driver.find_element_by_id('id_Search_vat_number__icontains').send_keys("644509589022")
        time.sleep(2)
        search_box = self.driver.find_element_by_xpath('//i[@class="pe-7s-id"]').click()
        search_box = self.driver.find_element_by_id('id_Search_code__icontains').send_keys("window")
        search_box = self.driver.find_element_by_id('id_Search_vat_number__icontains').send_keys("844559589332")
        search_box = self.driver.find_element_by_id('id_Search_business_name__icontains').send_keys("clarowin11@gmail.com")
        search_box = self.driver.find_element_by_id('id_Search_email__icontains').send_keys("jade@gmail.com")
        search_box = self.driver.find_element_by_id('id_Search_contact_name__icontains').send_keys("Jade")
        search_box = self.driver.find_element_by_id('id_Search_contact_email__icontains').send_keys("jade44@gmail.com")
        search_box = self.driver.find_element_by_xpath('//button[@class="btn btn-info"]').click()
        time.sleep(2)
        search_box = self.driver.find_element_by_xpath('//i[@class="pe-7s-note2"]').click()
        time.sleep(2)
        search_box = self.driver.find_element_by_xpath('//i[@class="pe-7s-culture"]').click()
        search_box = self.driver.find_element_by_id('id_Search_creator__username__icontains').send_keys("Factory")
        search_box = self.driver.find_element_by_id('id_Search_client__username__icontains').send_keys("ClaroFlex")
        search_box = self.driver.find_element_by_id('id_Search_name__icontains').send_keys("Denis")
        search_box = self.driver.find_element_by_xpath('//select[@name="Search_product"]/option[text()="Pivot Balcony"]').click()
        search_box = self.driver.find_element_by_xpath('//select[@name="Search_glass_thickness"]/option[text()="12 мм"]').click()
        search_box = self.driver.find_element_by_xpath('//select[@name="Search_bars_length"]/option[text()="6300 мм"]').click()
        search_box = self.driver.find_element_by_xpath("//input[@id='id_Search_date_modification__gte']").send_keys("2021-05-07")
        search_box = self.driver.find_element_by_xpath("//input[@id='id_Search_date_modification__lte']").send_keys("2021-05-09")
        search_box = self.driver.find_element_by_xpath('//button[@class="btn btn-info"]').click()
        time.sleep(2)
        search_box = self.driver.find_element_by_xpath('//i[@class="pe-7s-note"]').click()
        search_box = self.driver.find_element_by_xpath("//input[@id='id_Search_reference__icontains']").send_keys("54")
        search_box = self.driver.find_element_by_xpath("//input[@id='id_Search_creator__username__icontains']").send_keys("factory")
        search_box = self.driver.find_element_by_xpath("//input[@id='id_Search_client__username__icontains']").send_keys("claroflex")
        search_box = self.driver.find_element_by_xpath('//select[@name="Search_kind"]/option[text()="Pivot Balcony System"]').click()
        search_box = self.driver.find_element_by_xpath("//input[@id='id_Search_date_creation__gte']").send_keys("2021-05-15")
        search_box = self.driver.find_element_by_xpath("//input[@id='id_Search_date_creation__lte']").send_keys("2021-05-20")
        search_box = self.driver.find_element_by_xpath('//div[@class="col-xs-12 col-lg-3 text-right"]').click()
        search_box = self.driver.find_element_by_xpath('//button[@class="btn btn-info"]').click()
        time.sleep(2)
        search_box = self.driver.find_element_by_xpath('//i[@class="pe-7s-tools"]').click()
        time.sleep(2)
        search_box = self.driver.find_element_by_xpath('//i[@class="pe-7s-portfolio"]').click()
        search_box = self.driver.find_element_by_id('id_Search_quote__reference__icontains').send_keys("selenclaro")
        search_box = self.driver.find_element_by_id('id_Search_quote__client__company__name__icontains').send_keys("CLAROFLEX")
        search_box = self.driver.find_element_by_xpath('//select[@name="Search_shipping_kind"]/option[text()="Отправляется CLAROFLEX"]').click()
        search_box = self.driver.find_element_by_xpath("//input[@id='id_Search_shipping_order__date_departure__gte']").send_keys("2021-05-22")
        search_box = self.driver.find_element_by_xpath("//input[@id='id_Search_shipping_order__date_departure__lte']").send_keys("2021-05-24")
        search_box = self.driver.find_element_by_xpath("//input[@id='id_Search_shipping_order__date_arrival__gte']").send_keys("2021-05-25")
        search_box = self.driver.find_element_by_xpath("//input[@id='id_Search_shipping_order__date_arrival__lte']").send_keys("2021-05-27")
        search_box = self.driver.find_element_by_xpath('//button[@class="btn btn-info"]').click()
        time.sleep(2)
        search_box = self.driver.find_element_by_xpath('//i[@class="pe-7s-users"]').click()
        search_box = self.driver.find_element_by_id('id_Search_username__icontains').send_keys("Silvia")
        search_box = self.driver.find_element_by_id('id_Search_email__icontains').send_keys("silvia321@gmail.com")
        search_box = self.driver.find_element_by_id('id_Search_first_name__icontains').send_keys("Silv")
        search_box = self.driver.find_element_by_id('id_Search_last_name__icontains').send_keys("Ivanovna")
        search_box = self.driver.find_element_by_xpath('//select[@name="Search_groups"]/option[text()="Administrador"]').click()
        search_box = self.driver.find_element_by_xpath('//button[@class="btn btn-info"]').click()
        time.sleep(2)
        search_box = self.driver.find_element_by_xpath('//i[@class="pe-7s-ticket"]').click()
        search_box = self.driver.quit
        self.driver.get('http://52.49.129.95:8080/')
        
        
    
        search_box = self.driver.find_element_by_name('username')
        search_box.send_keys('gelya')
        search_box = self.driver.find_element_by_name('password')
        search_box.send_keys("qwerty1234%")
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        
        search_box = self.driver.find_element_by_link_text("+ Agregar proyecto").click()
        search_box = self.driver.quit
        
        time.sleep(3)
        search_box = self.driver.find_element_by_xpath('//a[@href="/projects/11/"]').click()
        search_box = self.driver.find_element_by_id('add_more_project_task_btn').click()
        search_box = self.driver.find_element_by_link_text("Seleccione un empleado").click()
        search_box = self.driver.find_element_by_xpath('//div[@class="ea_main_result"]')

        search_box = self.driver.find_elements_by_tag_name("option")
        for option in search_box:
            print ("Value is: %s" % option.get_attribute("value"))
        option.click()
        search_box = self.driver.find_element_by_xpath("//textarea[@class='task_desc input_text']").send_keys("first project")
        
#class SimpleTest(TestCase):
    #def test_basic_addition(self):
       # """
        #Tests that 1 + 1 always equals 2.
        #"""
        #self.assertEqual("Это поле не может быть пустым.", message)