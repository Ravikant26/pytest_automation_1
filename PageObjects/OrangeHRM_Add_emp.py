from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Orangehrm_Addemp:
    text_click_pim_XPATH="/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[2]/a[1]/span[1]"
    click_Add_EMP_XPATH="//button[normalize-space()='Add']"
    text_first_name="//input[@placeholder='First Name']"
    text_Middle_name="//input[@placeholder='Middle Name']"
    text_Last_name="//input[@placeholder='Last Name']"
    # file_upload_XPATH="//input[@type='file']"
    File_Upload_XPATH = "//input[@type='file']"
    clcik_save_btn_XPATH="//button[@type='submit']"
    success_msg_XPATH = "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']"

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    def click_PIM(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.text_click_pim_XPATH)))
        self.driver.find_element(By.XPATH,self.text_click_pim_XPATH).click()
    def click_Add_emp(self):
        self.driver.find_element(By.XPATH,self.click_Add_EMP_XPATH).click()

    def enter_firstname(self,firstname):
        self.driver.find_element(By.XPATH,self.text_first_name).send_keys(firstname)

    def enter_middlename(self,midname):
        self.driver.find_element(By.XPATH,self.text_Middle_name).send_keys(midname)

    def enter_lastname(self,lastname):
        self.driver.find_element(By.XPATH,self.text_Last_name).send_keys(lastname)

    def upload_photo_file(self,file_path):
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.File_Upload_XPATH)))
        self.driver.find_element(By.XPATH,self.File_Upload_XPATH).send_keys(file_path)

    def clcik_save_btn(self):
        self.driver.find_element(By.XPATH,self.clcik_save_btn_XPATH).click()

    def validate_Addemp_success_message(self):
        try:
            self.driver.find_element(By.XPATH,self.success_msg_XPATH)
            success_mess=self.driver.find_element(By.XPATH,self.success_msg_XPATH).text
            return success_mess
        except:
            pass
