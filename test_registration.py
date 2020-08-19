from selenium import webdriver
from faker import Faker
import time

link = "https://planoplan.com"
browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(3)

fake = Faker()
login = fake.email()
password = fake.password()

def test_planoplan_reg():
    try:
        browser.get(link)

        CabinetLinkButton = browser.find_element_by_id("cabinet-widget").find_element_by_xpath(".//span")
        CabinetLinkButton.click()

        RegistrationLinkButton = browser.find_element_by_xpath('//button[@data-test="button_signup"]')
        RegistrationLinkButton.click()

        InputLogin = browser.find_element_by_id("form-entry").find_element_by_xpath(".//input[@name='username']")
        InputLogin.send_keys(login)

        InputPassword = browser.find_element_by_id("form-entry").find_element_by_xpath(".//input[@name='password']")
        InputPassword.send_keys(password)

        RegisterButton = browser.find_element_by_id("form-entry").find_element_by_xpath(".//button[@type='submit']")
        RegisterButton.click()
        

    finally:
        time.sleep(5)
        browser.quit()
