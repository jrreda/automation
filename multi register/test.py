from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # import KEYS
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import random
import string


def register():
    # Define variables
    first_name = 'Mahmoud'
    last_name = 'Reda'
    phone = '01069907582'
    email = f'mahmoudreda_{random.randint(0,100)}@test.com'
    password = '*************'
    store_name = f'mahmoudreda_test_{random.randint(0,100000)}'
    store_url = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    email = f'mahmoudreda_{random.randint(0,100000)}@test.com'

    # load the driver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10) # gives an implicit wait for 10 seconds
    driver.delete_all_cookies()

    driver.get('https://staging.markatty.com/company/register')

    time.sleep(10)

    # first name
    driver.find_element(by=By.NAME, value='first_name').send_keys(first_name)
    # last name
    driver.find_element(by=By.NAME, value='last_name').send_keys(last_name)
    # email
    driver.find_element(by=By.NAME, value='email').send_keys(email)
    # password
    driver.find_element(by=By.NAME, value='password').send_keys(password)
    # phone
    driver.find_element(by=By.NAME, value='phone_no').send_keys(phone)
    # get started
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div[1]/div[1]/div[2]/form[1]/div/div[6]/div/div[3]/div/div/button'))).click()

    time.sleep(10)

    # verification code
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="n0"]'))).send_keys(9)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="n1"]'))).send_keys(6)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="n2"]'))).send_keys(3)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="n3"]'))).send_keys(8)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="n4"]'))).send_keys(5)
    # verify email
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div[1]/div[1]/div[2]/form[1]/div/div[2]/div/div[1]/button'))).click()

    time.sleep(10)

    # Store Name
    driver.find_element(by=By.NAME, value='name').send_keys(store_name)
    # store url
    driver.find_element(by=By.NAME, value='username').send_keys(store_url)
    # industry
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div/div/div/div[1]/div[1]/div[2]/form[2]/div/div[4]/div/select/option[1]').click()
    # create
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div[1]/div[1]/div[2]/form[2]/div/div[6]/div/div[1]/button'))).click()

    print(f'User {email} regestered successfully!')
        # driver.close()
