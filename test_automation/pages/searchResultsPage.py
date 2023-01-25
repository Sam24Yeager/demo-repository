from selenium.webdriver.common.by import By

from test_automation.base.basepage import BaseDriver


class SearchResults(BaseDriver):
    def __int__(self,driver):
        super().__int__(driver)
        self.driver=driver



    def filter(self):
        self.driver.find_element(By.XPATH, "(//p[@class='font-lightgrey bold'])[2]").click()
