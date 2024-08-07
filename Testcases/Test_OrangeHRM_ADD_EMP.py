import time

from PageObjects.OrangeHRM_Add_emp import Orangehrm_Addemp
from PageObjects.user_login_credkart_pom import Orange_hrm_login
from Utilities.Readconfigfile import Readconfigdata


class Test_Orangehrm_add_emp:
    username=Readconfigdata.getusername()
    password=Readconfigdata.getpassword()
    file_path = r"D:\user\BBT_lo.png"

    def test_orangehrm_addemp(self,setup):
        self.driver=setup
        self.oradd=Orangehrm_Addemp(self.driver)
        self.orh=Orange_hrm_login(self.driver)
        self.orh.enter_username(self.username)
        self.orh.enter_password(self.password)
        self.orh.click_login_btn()
        if self.orh.verify_login_status()=="pass":
            assert True
        else:
            assert False
        time.sleep(5)
        self.oradd.click_PIM()
        time.sleep(3)
        self.oradd.click_Add_emp()
        self.oradd.enter_firstname("suraj")
        self.oradd.enter_middlename("suresh")
        self.oradd.enter_lastname("patil")
        time.sleep(5)
        self.oradd.upload_photo_file(self.file_path)
        time.sleep(3)
        self.oradd.clcik_save_btn()
        if self.oradd.validate_Addemp_success_message()=="Successfully Saved":
            self.driver.get_screenshot_as_file("E:\\user\\CT-19_notes_2024\\6_python_selenium_class_5_03_july_2024\\Screenshots\\test_orangehrm_addemp_passed.png")
            assert True
        else:
            self.driver.get_screenshot_as_file("E:\\user\\CT-19_notes_2024\\6_python_selenium_class_5_03_july_2024\\Screenshots\\test_orangehrm_addemp_failed.png")
            assert False
        print("The Test_orangehrm_search_testcase is passed")
        self.driver.quit()




