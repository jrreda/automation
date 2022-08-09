from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime as DT
import time
import smtplib, ssl

def send_email(message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "mahmoudreda457@gmail.com"
    receiver_email = ["mahmoudreda457@gmail.com", "belal1997medhat@gmail.com"]
    # https://stackoverflow.com/questions/46445269/gmail-blocks-login-attempt-from-python-with-app-specific-password
    password = "****************" # "your email id's password"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        try:
            server.login(sender_email, password)
            res = server.sendmail(sender_email, receiver_email, message.encode('utf-8'))
            print('email sent!')
        except:
            raise
            print("could not login or send the mail.")

# load the driver
driver = webdriver.Chrome(r"C:\Users\mahmo\chromedriver.exe")
# driver.maximize_window()
driver.minimize_window()
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
try:
    driver.find_element(by=By.XPATH, value='//*[@id="PersonCount"]/option').click()
except:
    driver.find_element(by=By.XPATH, value='//*[@id="PersonCount"]/option[1]').click()
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
date = driver.find_element(by=By.XPATH, value='//*[@id="main"]/form/table[1]/tbody/tr/td[1]').text
from_week = date.split(' ')[1]

month = DT.datetime.strptime(from_week, "%m/%d/%Y").month

# the CONDITION
if month <= 8:
    print(f"The appoinment is in August in {date}")

    message = "Subject: Austrian Cairo embassy appointment [Automated]!\n\n"
    message += (f"Appointments available for \"Aufenthaltstitel Studierender (residency permit student)\", 2 Person(s): {date}.")
    # send the message
    send_email(message)
else:
    print(f"There is no appoinments in August!\nThe nearest on in {date}")

driver.close()
