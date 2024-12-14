from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObject.registration import *

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()
x = By.XPATH

def test_create_user():
    driver.find_element(x, click_registration_tab_xpath).click()
    driver.find_element(x, first_name_xpath).send_keys("Ashish")
    driver.find_element(x , last_name_xpath).send_keys("khobragde")
    driver.find_element(x , address_xpath).send_keys("lohara yavatmal")
    driver.find_element(x , email_xpath).send_keys("khobragde2001@gmail.com")
    driver.find_element(x, phon_number_xpath).send_keys("9673040564")
    driver.find_element(x , gender_xpath).click()
    # ele_language = Select(driver.find_element(x, language_DD_xpath))
    # ele_language.select_by_index("2")

    # ele_skill = Select(driver.find_element(x, skill_DD_xpath))
    # ele_skill.select_by_visible_text("AutoCAD")
    #
    # ele_country = Select(driver.find_element(x, select_country_DD_xpath))
    # ele_country.select_by_visible_text("India")
    #
    # year = Select(driver.find_element(x, DOB_year_DD_xpath))
    # year.select_by_value(1994)
    #
    # month = Select(driver.find_element(x, DOB_month_DD_xpath))
    # month.select_by_index(4)
    #
    # date = Select(driver.find_element(x, DOB_date_DD_xpath))
    # date.select_by_value(6)

    driver.find_element(x, password_xpath).send_keys("Ashish@001")
    driver.find_element(x , confirm_password_xpath).send_keys("Ashish@001")
    driver.save_screenshot("C:\\jenkins\\Screenshots\\registration.png")

    driver.find_element(x, submit_button_xpath).click()