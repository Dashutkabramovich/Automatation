from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as Chromeservice
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))

#открыть страницу 

driver.get("http://the-internet.herokuapp.com/inputs")

#ввести в поле текст 1000

search_field = "input[type='number']"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
sleep(2)
search_input.send_keys("1000")
sleep(2)
#очистить это поле (метод clear)
search_input.clear()
sleep(2)
#ввести в это же поле текст 999
search_input.send_keys("999")
sleep(2)