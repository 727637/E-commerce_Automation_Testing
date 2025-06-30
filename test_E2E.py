import pytest
from selenium import webdriver

from utilities.BaseClass import BaseClass
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



# @pytest.mark.usefixtures("setup")
class Testone(BaseClass):  # inheritence

    def test_e2e(self):
        # xpath===>> //a[contains(@href,'shop')]
        self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()  # for css partial value of that text
        print("1")
        result = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        for i in result:
            productName = i.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                i.find_element(By.XPATH, "div/button").click()

        print("2")
        self.driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()
        print("3")

        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        success = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in success
        # driver.close()
