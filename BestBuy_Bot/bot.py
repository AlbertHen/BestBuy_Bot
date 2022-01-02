from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DIY:

    def __init__(self, url):
        self.url = url
        self.create()

    def create(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def refresh(self):
        self.driver.close()
        self.driver.quit()
        self.create()

    def check(self):
        cart_button = self.driver.find_elements(By.CLASS_NAME, "add-to-cart-button")
        if 'SOLD_OUT' in cart_button:
            return False
        else:
            return True

    def add_to_cart(self):
        if self.check():
            cart_button = self.driver.find_elements(By.CLASS_NAME, "add-to-cart-button")
            cart_button[-1].click()
            print('Successfully added to cart')
        else:
            print('Sorry, this item is sold out :)')

