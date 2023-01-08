from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www2.hm.com/hu_hu/productpage.1044156002.html")
button = driver.find_element(By.CLASS_NAME, "trigger-button")
button.click()

size_options = driver.find_elements(By.CSS_SELECTOR, ".option span")

for option in size_options:
    value = option.text
    classes = option.get_attribute("class")
    if value == "32" and "oos" not in classes:
        print('The selected size is available.')


driver.quit()
