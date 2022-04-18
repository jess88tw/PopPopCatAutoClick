from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

driver_path ='/Users/jess88tw/webdriver/chromedriver'
driver = webdriver.Chrome(driver_path)
url = 'https://popcat.click'
driver.get(url)

while True:
    driver.find_element_by_xpath('//*[@id="app"]/div').click()
    time.sleep(0.055)
    driver.find_element_by_xpath('//*[@id="app"]/div').click()
    time.sleep(0.055)
    driver.find_element_by_xpath('//*[@id="app"]/div').click()
    time.sleep(0.055)
    driver.find_element_by_xpath('//*[@id="app"]/div').click()
    time.sleep(0.055)
    driver.find_element_by_xpath('//*[@id="app"]/div').click()
    time.sleep(0.055)