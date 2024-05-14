from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
firefox_service=Service()
driver=webdriver.Firefox(service=firefox_service)

#открыть страницу
driver.get("http://uitestingplayground.com/dynamicid")

#кликнуть на синюю кнопку и ждать, пока кнопка синего цвета станет кликабельной
blue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))

#запустить скрипт три раза подряд. Убедиться, что он отработает одинаково
for i in range(3):
    driver.get("http://uitestingplayground.com/dynamicid")
    blue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    print(blue_button)
driver.quit()