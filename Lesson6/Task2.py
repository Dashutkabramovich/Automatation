
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chromeservice
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))

#перейти на страницу
driver.get(" http://uitestingplayground.com/textinput")

#указать в поле ввода текст SkyPro
input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

# нажать на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

#получить текст кнопки
button_text = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary"))).text

#вывести в консоль (SkyPro)
print(button_text) 

driver.quit()
