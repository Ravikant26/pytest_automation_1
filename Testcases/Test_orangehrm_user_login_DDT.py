import time

from PageObjects.user_login_credkart_pom import Orange_hrm_login
from Utilities import XLUtilies


class Test_UserLogin:
    path="E:\\user\\CT-19_notes_2024\\6_python_selenium_class_5_03_july_2024\\Testcases\\TestData\\User_Login_Data.xlsx"
    def test_user_login_ORH__001(self,setup):
        self.driver=setup
        self.orh=Orange_hrm_login(self.driver)
        self.Row_co=XLUtilies.row_count(self.path,"user_login_data")
        print("total no of the rowcount-->" +str(self.Row_co))
        list_status=[]
        for r in range(2,self.Row_co+1):
            self.username=XLUtilies.read_data(self.path,"user_login_data",r,1)
            # time.sleep(5)
            self.password=XLUtilies.read_data(self.path,"user_login_data",r,2)
            # time.sleep(5)
            self.Excel_Result=XLUtilies.read_data(self.path,"user_login_data",r,3)
            # time.sleep(5)
            self.orh.enter_username(self.username)
            self.orh.enter_password(self.password)
            time.sleep(3)
            self.orh.click_login_btn()
            time.sleep(3)
            if self.orh.verify_login_status()=="pass" and self.Excel_Result=="pass":
                # time.sleep(3)
                list_status.append("pass")
                # time.sleep(5)
                XLUtilies.write_data(self.path,"user_login_data",r,4,"pass")
                self.driver.save_screenshot(".\\Screenshots\\test_user_login_ORH__001_passed.png")
                # time.sleep(3)
                self.orh.click_manu_btn()
                time.sleep(3)
                self.orh.click_logout_btn()

            elif self.orh.verify_login_status()=="pass" and self.Excel_Result=="fail":
                # time.sleep(3)
                list_status.append("fail")
                # time.sleep(3)
                XLUtilies.write_data(self.path,"user_login_data",r,4,"fail")
                self.driver.save_screenshot(".\\Screenshots\\test_user_login_ORH__001_failed.png")
                self.orh.click_manu_btn()
                self.orh.click_logout_btn()
            elif self.orh.verify_login_status()=="fail" and  self.Excel_Result=="pass":
                list_status.append("fail")

                XLUtilies.write_data(self.path,"user_login_data",r,4,"fail")
                self.driver.save_screenshot(".\\Screenshots\\test_user_login_ORH__001_failed.png")

            elif self.orh.verify_login_status()=="fail" and self.Excel_Result=="fail":

                list_status.append("pass")
                XLUtilies.write_data(self.path, "user_login_data", r, 4, "pass")
                self.driver.save_screenshot(".\\Screenshots\\test_user_login_ORH__001_passed.png")
        print(list_status)
        if 'fail' not in list_status:
            assert True
        else:
            assert False
        print("test_user_login_ORH__001 is completed")
        self.driver.quit()





