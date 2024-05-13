from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.firefox.service import Service
firefox_service=Service()
driver=webdriver.Firefox(service=firefox_service)

#открыть страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

#5 раз кликнуть на кнопку Add Element
for i in range(5):
    add_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
    add_button.click()

#собрать со страницы список кнопок Delete
sleep(3)
driver.minimize_window()
add_button = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')

#вывести на экран размер списка
print(len(add_button))

sleep(5)