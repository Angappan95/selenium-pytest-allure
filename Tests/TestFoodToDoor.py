from random import randint

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FNAME = 'John'
LNAME = 'Sam'
EMAIL = f'john{randint(1, 1000)}@xyz.com'
MOBILE = '999999999'
PWD = 'P@ssword'

driver = Chrome(executable_path='../drivers/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(20)
driver.get('https://sleepy-brook-65250.herokuapp.com/')

wait = WebDriverWait(driver, 15)

ele_register = driver.find_element_by_link_text('Register')
wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'overlay')))
ele_register.click()

wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'overlay')))
ele_firstname = driver.find_element_by_xpath('//input[@formcontrolname="firstName"]')
ele_lastname = driver.find_element_by_xpath('//input[@formcontrolname="lastName"]')
ele_email = driver.find_element_by_xpath('//input[@formcontrolname="email"]')
ele_mobile = driver.find_element_by_xpath('//input[@formcontrolname="mobileNumber"]')
ele_pwd = driver.find_element_by_xpath('//input[@formcontrolname="password"]')
ele_cnf_pwd = driver.find_element_by_xpath('//input[@formcontrolname="confirmPassword"]')
ele_attachment = driver.find_element_by_xpath('//input[@formcontrolname="customFile"]')

ele_firstname.send_keys(FNAME)
ele_lastname.send_keys(LNAME)
ele_email.send_keys(EMAIL)
ele_mobile.send_keys(MOBILE)
ele_pwd.send_keys(PWD)
ele_cnf_pwd.send_keys(PWD)
ele_attachment.send_keys('C:/Angappan/Automation/Practice/FoodToDoor/data/data.txt')

ele_terms = driver.find_element_by_link_text('terms of service')
ele_terms.click()

handles = driver.window_handles
driver.switch_to.window(handles[-1])

ele_accept = driver.find_element_by_xpath('//button[text()=" I Accept & Close "]')
ele_accept.click()

driver.switch_to.window(handles[0])

ele_submit = driver.find_element_by_xpath('//button[text()="Register"]')
ele_submit.click()

ele_confirmation = driver.find_element_by_xpath('//h2[text()=" You are registered please Login!! "]')
assert ele_confirmation.text == 'You are registered please Login!!', "Something went wrong"

ele_login = driver.find_element_by_link_text('login')
ele_login.click()

ele_username = driver.find_element_by_xpath('//input[@formcontrolname="userName"]')
ele_password = driver.find_element_by_xpath('//input[@formcontrolname="password"]')
btn_signin = driver.find_element_by_link_text('Sign in')

ele_username.send_keys(EMAIL)
ele_password.send_keys(PWD)
btn_signin.click()

ele_restaurant = driver.find_element_by_xpath('//h5[text()=" Saravuana Bhauan "]')
ele_veg_biryani = driver.find_element_by_xpath('//span[text()="Veg Briayani"]/ancestor::table')
ele_add_qty = ele_veg_biryani.find_element_by_xpath('//button[contains(text(),"+")]')
driver.switch_to.alert.accept()





