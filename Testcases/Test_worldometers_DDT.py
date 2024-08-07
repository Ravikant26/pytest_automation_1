from selenium.webdriver.common.by import By

from Utilities import ExcelUtilies, XLUtilies


class Test_worldometer:
    path="E:\\user\\CT-19_notes_2024\\6_python_selenium_class_5_03_july_2024\\Testcases\\TestData\\Worldomete_Data.xlsx"
    def test_worldometer_DDT(self,setup):
        self.driver=setup
        self.driver.get("https://www.worldometers.info/world-population/population-by-country/")
        self.driver.maximize_window()
        # l=len(self.driver.find_elements(By.XPATH,"//tbody/tr/td[1]"))
        col = len(self.driver.find_elements(By.XPATH, "//tbody/tr/td[1]"))
        ro=len(self.driver.find_elements(By.XPATH,"//tbody/tr[1]/td"))
        # list=[]
        print(ro)
        print(col)

        for i in range(1,ro+1):
            for j in range(1,col+1):
                # self.driver.implicitly_wait(2)
                self.s = self.driver.find_element(By.XPATH, "//tbody/tr[" + str(j) + "]/td[" +str(i) + "]").text
                ExcelUtilies.write_data(self.path, "data_sheet", j, i, str(self.s))
                # print("-0------",i,j)
        print("The test case test_worldometer_DDT is completed")
        self.driver.quit()






