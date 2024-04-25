from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as Chromeservice
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))

#открыть страницу 

driver.get("http://the-internet.herokuapp.com/login")

#в поле username ввести значение tomsmith
username_field = "#username"
username_input = driver.find_element(By.CSS_SELECTOR, username_field)
sleep(2)
username_input.send_keys("tomsmith")
sleep(2)

#в поле password ввести значение SuperSecretPassword!
password_field = "#password"
password_input = driver.find_element(By.CSS_SELECTOR, password_field)
sleep(2)
password_input.send_keys("SuperSecretPassword!")
sleep(2)

#нажать кнопку Login
button=driver.find_element(By.CSS_SELECTOR, ".radius").click()

sleep(5)

