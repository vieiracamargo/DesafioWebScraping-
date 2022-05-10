from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.zoom.com.br/")
time.sleep(1)
#barra = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div/div[3]/div/div/div[1]/input").send_keys('RX 6600')
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/header/div[1]/div/div/div[3]/div/div/div[1]/button").click()
