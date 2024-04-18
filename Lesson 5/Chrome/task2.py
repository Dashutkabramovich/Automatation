from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as Chromeservice
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))

#открыть страницу
driver.get("http://uitestingplayground.com/dynamicid")

#кликнуть на синюю кнопку и ждать, пока кнопка синего цвета станет кликабельной
blue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))

#запустить скрипт три раза подряд. Убедитесь, что он отработает одинаково
for i in range(3):
    driver.get("http://uitestingplayground.com/dynamicid")
    blue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary")))
    print(blue_button)
