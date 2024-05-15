from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chromeservice
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
