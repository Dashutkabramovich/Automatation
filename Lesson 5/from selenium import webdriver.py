from selenium import webdriver
from selenium.webdriver.firefox.service import Service
firefox_service=Service()
driver=webdriver.Firefox(service=firefox_service)

