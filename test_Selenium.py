from selenium import webdriver
from selenium.webdriver.common import keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
print("Testcase started")

driver=webdriver.Chrome(ChromeDriverManager().install())
print("Testcase started")

driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("HARMAN")
time.sleep(2)
driver.find_elements_by_name("btnk").send_keys(keys.ENTER)
time.sleep(10)
driver.close()
print("Testcase completed.....")