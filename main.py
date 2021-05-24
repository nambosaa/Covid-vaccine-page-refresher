from selenium import webdriver
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://selfregistration.cowin.gov.in/appointment")
time.sleep(10)
print("10 seconds")
time.sleep(30)
print("40 seconds")
time.sleep(30)
print("70 seconds")

search_btn = driver.find_element_by_class_name("pin-search-btn")
search_btn.click()

for _ in range(100):
    time.sleep(5)
    search_btn.click()

driver.quit()


