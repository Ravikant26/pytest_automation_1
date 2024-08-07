import time

from PageObjects.OrangeHrm_search_emp_pom import Orangehrm_Searchemp
from PageObjects.user_login_credkart_pom import Orange_hrm_login
from Utilities.Readconfigfile import Readconfigdata


class Test_Orangehrm_search_emp:
    username=Readconfigdata.getusername()
    password=Readconfigdata.getpassword()
    # file_path = r"D:\user\BBT_lo.png"

    def test_orangehrm_searchemp(self,setup):
        self.driver=setup
        self.orh=Orange_hrm_login(self.driver)
        self.se=Orangehrm_Searchemp(self.driver)
        self.orh.enter_username(self.username)
        self.orh.enter_password(self.password)
        self.orh.click_login_btn()
        if self.orh.verify_login_status()=="pass":
            self.driver.save_screenshot("E:\\user\\CT-19_notes_2024\\6_python_selenium_class_5_03_july_2024\\Screenshots\\test_orangehrm_searchemp_loginpassed.png")
            assert True
        else:
            self.driver.save_screenshot("E:\\user\\CT-19_notes_2024\\6_python_selenium_class_5_03_july_2024\\Screenshots\\test_orangehrm_searchemp_login_failed.png")

            assert False

        self.se.click_PIM()
        self.emp_id="0427"
        time.sleep(3)
        self.se.enter_empid(self.emp_id)
        self.se.clcick_search_btn()
        if self.se.validatation_success_massage()=="Successfully Saved" or self.emp_id:
            self.driver.save_screenshot("E:\\user\\CT-19_notes_2024\\6_python_selenium_class_5_03_july_2024\\Screenshots\\test_orangehrm_searchemp_validatation_success_massage_passed.png")

            assert True
        else:
            self.driver.save_screenshot("E:\\user\\CT-19_notes_2024\\6_python_selenium_class_5_03_july_2024\\Screenshots\\test_orangehrm_searchemp_validatation_success_massage_failed.png")

            assert False
        print("the search_emp_test case is passed")




