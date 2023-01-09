from selenium import webdriver
from selenium.webdriver.common.by import By


class AvailabilityChecker:
    def __init__(self, articlenumber, size):
        self.size = size
        self.articlenumber = articlenumber
        self.driver = webdriver.Chrome()
        self.driver_init()

        self.button_clicker()
        self.checker_print_to_console(self.checker())

        self.driver.quit()

    def driver_init(self):
        self.driver.get(f"https://www2.hm.com/hu_hu/productpage.{self.articlenumber}.html")

    def button_clicker(self):
        button = self.driver.find_element(By.CLASS_NAME, "trigger-button")
        button.click()

    def checker(self):
        size_options = self.driver.find_elements(By.CSS_SELECTOR, ".option span")
        for option in size_options:
            value = option.text
            classes = option.get_attribute("class")
            if value == self.size and "oos" not in classes:
                return True
        return False

    def checker_print_to_console(self, available):
        if available:
            print(f'The selected size ({self.size}) is available.')
        else:
            print(f'The selected size ({self.size}) is not available.')


check = AvailabilityChecker("1044156002", "32")
check2 = AvailabilityChecker("1044156002", "38")
check3 = AvailabilityChecker("1140505001", "XS")
