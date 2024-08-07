from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Orangehrm_Searchemp:
    text_click_pim_XPATH = "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[2]/a[1]/span[1]"
    text_EMP_ID_XPATH="/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/div[1]/div[2]/input[1]"
    # text_EMP_NAME_XPATH="//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--focus']//input[@placeholder='Type for hints...']"
    success_msg_XPATH = "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']"
    text_click_search_button_XPATH="//button[@type='submit']"

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    def click_PIM(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.text_click_pim_XPATH)))
        self.driver.find_element(By.XPATH,self.text_click_pim_XPATH).click()

    def enter_empid(self,empid):
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.text_EMP_ID_XPATH)))
        self.driver.find_element(By.XPATH,self.text_EMP_ID_XPATH).send_keys(empid)

    def clcick_search_btn(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.text_click_search_button_XPATH)))
        self.driver.find_element(By.XPATH,self.text_click_search_button_XPATH).click()

    def validatation_success_massage(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH,self.success_msg_XPATH)))
            self.driver.find_element(By.XPATH,self.success_msg_XPATH)
            success_message=self.driver.find_element(By.XPATH,self.success_msg_XPATH).text
            return success_message
        except TimeoutError:
            pass

