import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller_fix

class TestAppE2E(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chromedriver_autoinstaller_fix.install()  
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://localhost:5000')

    def wait_for_element(self, by, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))

    def test_add_and_delete_item(self):
        # Test adding an item
        self.wait_for_element(By.NAME, "item")
        item_input = self.driver.find_element(By.NAME, "item")
        item_input.send_keys("Test Item")
        self.driver.find_element(By.CSS_SELECTOR, "button").click()

        # Modify the item
        self.wait_for_element(By.NAME, "new_item")
        modify_input = self.driver.find_element(By.NAME, "new_item")
        modify_input.send_keys("Modified Item")
        self.driver.find_element(By.CSS_SELECTOR, "li button").click()

        # Add another item
        self.wait_for_element(By.NAME, "item")
        another_item_input = self.driver.find_element(By.NAME, "item")
        another_item_input.send_keys("A new Item")
        self.driver.find_element(By.CSS_SELECTOR, ".container > form > button").click()

        # Delete items
        delete_buttons = self.driver.find_elements(By.LINK_TEXT, "Delete")
        for button in delete_buttons:
            button.click()
            self.wait_for_element(By.LINK_TEXT, "Delete")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()