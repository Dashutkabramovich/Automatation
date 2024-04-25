from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chromeservice
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))

#перейти на страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

#дождаться загрузки 4-й картинки
picture = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#landscape")))

# получить значение атрибута src у 3-й картинки
src = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src") 

# вывести в консоль
print(src) 

driver.quit()