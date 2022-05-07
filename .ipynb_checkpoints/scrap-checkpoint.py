from selenium import webdriver
from selenium.webdriver.common.by import By


PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(PATH, options=options)


driver.get('https://www.bookdepository.com/es/account/wishlist')
