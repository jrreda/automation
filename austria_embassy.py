from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime as DT
import time


# load the driver
driver = webdriver.Chrome(r"C:\Users\mahmo\chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()

driver.get("https://appointment.bmeia.gv.at/")
# wait 5 
time.sleep(5)

## Page 1
# Representation
driver.find_element(by=By.XPATH, value='//*[@id="Office"]/option[37]').click()
# next
driver.find_element(by=By.XPATH, value='//*[@id="main"]/form/table[2]/tbody/tr[2]/td[2]/input').click()
# wait 5 
time.sleep(5)

## Page 2
# Reservation for	
driver.find_element(by=By.XPATH, value='//*[@id="CalendarId"]/option[4]').click()
# next
driver.find_element(by=By.XPATH, value='//*[@id="main"]/form/table[2]/tbody/tr[3]/td[2]/input[2]').click()
# wait 5 
time.sleep(5)

## Page 3
# Number of persons	
driver.find_element(by=By.XPATH, value='//*[@id="PersonCount"]/option[2]').click()
# next
driver.find_element(by=By.XPATH, value='//*[@id="main"]/form/table[2]/tbody/tr[4]/td[2]/input[2]').click()
# wait 5 
time.sleep(5)

## Page 4
# next
driver.find_element(by=By.XPATH, value='//*[@id="main"]/form/input[6]').click()
# wait 5 
time.sleep(5)

## Page 5
# Appointments available for
data = driver.find_element(by=By.XPATH, value='//*[@id="main"]/form/table[1]/tbody/tr/td[1]').text
week_1 = data.split(' ')[1]

month = DT.datetime.strptime(week_1, "%m/%d/%Y").month

# the CONDITION
if month <= 9:
    print(f"The appoinment is in Septemper in {week_1}")