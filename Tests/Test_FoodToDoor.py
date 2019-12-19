import os
import sys
import pytest
import allure
from allure_commons.types import AttachmentType
from random import randint
from selenium.webdriver import Chrome

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
print(os.getcwd())
from pages.Page import *


@pytest.fixture(scope='session')
def driver():
    driver = Chrome(executable_path='../drivers/chromedriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get('https://sleepy-brook-65250.herokuapp.com/')
    yield driver
    driver.close()


@allure.story('Registration')
@pytest.mark.parametrize('fname,lname,email,mobile,pwd,attachment',
                         [('John', 'Sam', f'john{randint(1, 1000)}@xyz.com', '999999999', 'P@ssword',
                           'C:/Angappan/Automation/Practice/FoodToDoor/data/data.txt')])
def test_signup(driver, fname, lname, email, mobile, pwd, attachment):
    allure.dynamic.description('Validate Registration')
    home_page = HomePage(driver)
    home_page.click_register()
    register_page = RegisterPage(driver)
    register_page.fill_info(fname, lname, email, mobile, pwd, attachment)
    register_page.accept_terms()
    assert register_page.get_confirmation_msg() == 'You are registered please Login!!'
