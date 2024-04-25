from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.firefox.service import Service
firefox_service=Service()
driver=webdriver.Firefox(service=firefox_service)

#открыть страницу
driver.get("http://uitestingplayground.com/classattr")

#кликнуть на синюю кнопку
button=driver.find_element(By.CSS_SELECTOR, ".btn-primary")
button.click()

#обработка всплывающего окна
alert=driver.switch_to.alert
alert.accept()

#запустить скрипт три раза подряд. Убедиться, что он отработает одинаково.

for i in range(3):
    driver.get("http://uitestingplayground.com/classattr")
    button=driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()
    sleep(2)
    alert=driver.switch_to.alert
    alert.accept()
