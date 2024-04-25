
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chromeservice
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))

#перейти на страницу

driver.implicitly_wait(16)
driver.get("http://uitestingplayground.com/ajax")

#нажать на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

#получить текст из зеленой плашки
txt=driver.find_element(By.CSS_SELECTOR, "p.bg-success").text

#вывести его в консоль (Data loaded with AJAX get request)
print(txt)


driver.quit()
