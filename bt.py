from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import random

from selenium.webdriver.common.proxy import Proxy, ProxyType

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = "ip_addr:port"
prox.socks_proxy = "ip_addr:port"
prox.socks_version = 5
prox.ssl_proxy = "ip_addr:port"

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)

driver = webdriver.Chrome(desired_capabilities=capabilities)
driver.get('https://www.instagram.com/accounts/emailsignup/')

sleep(10)

emailOrNumber = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[1]/div/label/input').send_keys('09188687133') # باید شماره خودتون باشه
sleep(2)
FullName = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[2]/div/label/input').send_keys('hosseinazimi')
sleep(1)

y = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 0, ]

RandomWord = 'abcdefghijklomnpqrstuvwxyz'

UserName = driver.find_element(By.CSS_SELECTOR, '#react-root > section > main > div > div > div:nth-child(1) > div.P8adC > form > div:nth-child(4) > div > label > input').send_keys(f"none.{random.choice(y)}{random.choice(RandomWord)}{random.choice(y)}")
sleep(2)
Password = driver.find_element(By.CSS_SELECTOR, '#react-root > section > main > div > div > div:nth-child(1) > div.P8adC > form > div:nth-child(5) > div > label > input').send_keys(f"nonepass.{random.choice(y)}{random.choice(RandomWord)}{random.choice(y)}")

sleep(10)
signBTN = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[5]/div/button').click()

sleep(7)

yearselect = driver.find_element(By.CSS_SELECTOR, '#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm.bkEs3.DhRcB > div > div > span > span:nth-child(3) > select').click()
sleep(1)
year = driver.find_element(By.CSS_SELECTOR, '#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm.bkEs3.DhRcB > div > div > span > span:nth-child(3) > select > option:nth-child(34)').click()
sleep(4)
NextBtn = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div/div[6]/button').click()
sleep(15)
inp = int(input('enter your number:  '))

sleep(15)
code = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div/div/div/form/div[1]/div/label/input').send_keys(inp)

codeBTN = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div/div/div/form/div[2]/button').click()
