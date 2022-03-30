from datetime import time

from selenium import webdriver
from selenium.webdriver.common import keys
from webdriver_manager.chrome import ChromeDriverManager


driver=webdriver.Chrome(ChromeDriverManager().install())
print("Test cases started")
driver.maximize_window()
driver.get("https.//www.w3schools.com/")
driver.find_element_by_link_text("Tutorials").click()
time.sleep(5)
driver.find_element_by_link_text("Learn Python").click()
time.sleep(5)
driver.close()
print("test case completed")

