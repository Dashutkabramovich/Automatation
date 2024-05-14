from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as Chromeservice
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))

#открыть страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")
 
#в модальном окне нажмите на кнопку Сlose
sleep(5)
button=driver.find_element(By.CSS_SELECTOR, ".modal-footer").click()

