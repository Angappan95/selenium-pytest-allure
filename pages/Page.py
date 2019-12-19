from helpers.HelperFunctions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.ele_register_link_text = 'Register'
        self.wait = WebDriverWait(self.driver, 15)

    @allure.step('Click Register button')
    def click_register(self):
        driver = self.driver
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'overlay')))
        locate(driver, self.ele_register_link_text, locator='link').click()


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.ele_overlay_class = 'overlay'
        self.ele_firstname = '//input[@formcontrolname="firstName"]'
        self.ele_lastname = '//input[@formcontrolname="lastName"]'
        self.ele_email = '//input[@formcontrolname="email"]'
        self.ele_mobile = '//input[@formcontrolname="mobileNumber"]'
        self.ele_pwd = '//input[@formcontrolname="password"]'
        self.ele_cnf_pwd = '//input[@formcontrolname="confirmPassword"]'
        self.ele_attachment = '//input[@formcontrolname="customFile"]'
        self.ele_terms_link = 'terms of service'
        self.ele_accept = '//button[text()=" I Accept & Close "]'
        self.wait = WebDriverWait(self.driver, 15)

    @allure.step('Fill user information')
    def fill_info(self, fname, lname, email, mobile, pwd, attachment):
        driver = self.driver
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'overlay')))
        locate(driver, self.ele_firstname).send_keys(fname)
        locate(driver, self.ele_lastname).send_keys(lname)
        locate(driver, self.ele_email).send_keys(email)
        locate(driver, self.ele_mobile).send_keys(mobile)
        locate(driver, self.ele_pwd).send_keys(pwd)
        locate(driver, self.ele_cnf_pwd).send_keys(pwd)
        locate(driver, self.ele_attachment).send_keys(attachment)

    @allure.step('Accept Terms and Conditions')
    def accept_terms(self):
        driver = self.driver
        locate(driver, self.ele_terms_link, locator='LINK').click()
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        locate(driver, self.ele_accept).click()
        driver.switch_to.window(handles[0])

    @allure.step('Get Confirmation message')
    def get_confirmation_msg(self):
        driver = self.driver
        locate(driver, '//button[text()="Register"]').click()
        return locate(driver, '//h2[text()=" You are registered please Login!! "]').text
