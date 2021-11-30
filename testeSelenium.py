from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import bs4 as bs


driver=webdriver.Edge(executable_path="C:\\Users\\Rafael Pietro\\OneDrive\\Cursos\\DNC\\VSCode\\msedgedriver.exe")
driver.get("http://alfa.monkey.exchange/")

# elem = driver.find_element_by_xpath("//input[@placeholder='email...']")

elem = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='email...']")))
print("Dale")