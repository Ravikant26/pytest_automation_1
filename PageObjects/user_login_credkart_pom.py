import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Orange_hrm_login():
    text_username_XPATH=(By.XPATH,"//input[@placeholder='Username']")
    text_password_XPATH=(By.XPATH,"//input[@placeholder='Password']")
    click_login_button_XPATH=(By.XPATH,"//button[@type='submit']")
    verify_username_XPATH=(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
    click_manu_btn_XPATH=(By.XPATH,"//p[@class='oxd-userdropdown-name']")
    click_logout_btn_XPATH=(By.XPATH,"//a[normalize-space()='Logout']")
    # URL="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    total_element_xpath="//tbody/tr/td"





    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)

    def element(self):
        text_1=self.driver.find_element(By.XPATH(self.total_element_xpath).text)


    def enter_username(self,username):
        # self.wait.until(EC.visibility_of_element_located(self.text_username_XPATH))
        self.driver.find_element(*Orange_hrm_login.text_username_XPATH).send_keys(username)
    def enter_password(self,password):
        self.driver.find_element(*Orange_hrm_login.text_password_XPATH).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element(*Orange_hrm_login.click_login_button_XPATH).click()

    def verify_login_status(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.verify_username_XPATH))
            self.driver.find_element(*Orange_hrm_login.verify_username_XPATH)
            # time.sleep(1)
            return "pass"
        except:
            return "fail"
    def click_manu_btn(self):
        self.wait.until(EC.visibility_of_element_located(self.click_manu_btn_XPATH))
        self.driver.find_element(*Orange_hrm_login.click_manu_btn_XPATH).click()

    def click_logout_btn(self):
        self.driver.find_element(*Orange_hrm_login.click_logout_btn_XPATH).click()

