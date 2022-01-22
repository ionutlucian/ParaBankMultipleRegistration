from selenium import webdriver
from faker import Faker
import string
import random

def fillIn(driver,id,value):
    element = driver.find_element_by_id(id)
    element.clear()
    element.send_keys(value)

def registration(driver,fake):
    
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/p[2]/a").click()
    driver.fullscreen_window()
    password = fake.password()
    letters = string.ascii_lowercase
    fillIn(driver,"customer.firstName",fake.name())
    fillIn(driver,"customer.lastName",fake.last_name())
    fillIn(driver,"customer.address.street",fake.street_address())
    fillIn(driver,"customer.address.city",fake.city())
    fillIn(driver,"customer.address.state",fake.country())
    fillIn(driver,"customer.address.zipCode",fake.postcode())
    fillIn(driver,"customer.phoneNumber",fake.phone_number())
    fillIn(driver,"customer.ssn",fake.ssn())
    fillIn(driver,"customer.username",( ''.join(random.choice(letters) for i in range(15))))
    fillIn(driver,"customer.password",password)
    fillIn(driver,"repeatedPassword",password)
    
    buttons = driver.find_elements_by_css_selector(".button")
    for button in buttons:
        value = button.get_attribute("value")
        if value == "Register":
            button.click()

    driver.fullscreen_window()
    driver.find_element_by_css_selector("#leftPanel > ul > li:nth-child(8) > a").click()