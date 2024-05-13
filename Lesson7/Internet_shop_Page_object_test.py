from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

from pages.InternetshopPage import InternetshopPage


def test_form_internet_shop():
    driver = webdriver.Chrome(service=ChromeService
                              (ChromeDriverManager().install()))
    internet_shop_page = InternetshopPage(driver)
    internet_shop_page.authorization("standard_user", "secret_sauce")
    to_be = internet_shop_page.add_products()
    internet_shop_page.go_to_cart()
    internet_shop_page.personal_data("Daria", "Abramovich", "127081")
    as_is = internet_shop_page.total_cost()
    assert as_is == to_be
    internet_shop_page.close()