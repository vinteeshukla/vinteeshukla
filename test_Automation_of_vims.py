import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class TestTest1():
    def setup_method(self, method):
        # self.driver = webdriver.Chrome()

        # self.options = Options()
        # self.options.headless = True
        # self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # self.options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        # self.s = Service(r"C:\Users\mvintee\project_for_selenium\chromedriver_win32\chromedriver.exe")
        # self.driver = webdriver.Chrome(service=self.s)
        # self.actions = ActionChains(self.driver)
        # self.vars = {}
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_login(self):
        # Test name: login_logout
        # Step # | name | target | value
        # 1 | open | http://piswamp:81/vmis.in/ |
        self.driver.get("http://piswamp:81/vmis.in/")
        # 2 | setWindowSize | 1280x680 |
        self.driver.set_window_size(1280, 680)
        # 3 | click | linkText=LOGIN |
        self.driver.find_element(By.LINK_TEXT, "LOGIN").click()
        # 4 | click | name=data[Membershipformdetail][username] |
        self.driver.find_element(By.NAME, "data[Membershipformdetail][username]").click()
        # 5 | type | name=data[Membershipformdetail][username] | vinteeshukla@gmail.com
        self.driver.find_element(By.NAME, "data[Membershipformdetail][username]").send_keys("vinteeshukla@gmail.com")
        # 6 | click | name=data[Membershipformdetail][password] |
        self.driver.find_element(By.NAME, "data[Membershipformdetail][password]").click()
        # 7 | type | name=data[Membershipformdetail][password] | rwKJGQ
        self.driver.find_element(By.NAME, "data[Membershipformdetail][password]").send_keys("rwKJGQ")
        # 8 | click | css=.largebtn |
        self.driver.find_element(By.CSS_SELECTOR, ".largebtn").click()
        # 9 | click | css=.largebtn |

    def test_registration(self):
        self.driver.get("http://piswamp:81/vmis.in/")
        self.driver.get("chrome://settings/")
        self.driver.execute_script("chrome.settingsPrivate.setDefaultZoom(.67)")
        # self.driver.get( "http://192.168.20.60/NorthStarWMS/login.aspx?ReturnUrl=%2fNorthStarWMS%2fDashboard%2fDashboardNew.aspx")
        # 2 | setWindowSize | 1024x728 |
        #self.driver.set_window_size(1024, 728)
        self.driver.get("http://piswamp:81/vmis.in/")
        # 2 | setWindowSize | 1052x660 |
        #self.driver.set_window_size(1052, 660)
        # 3 | click | linkText=CAA |
        self.driver.find_element(By.LINK_TEXT, "CAA").click()
        # 4 | click | id=m_1 |
        self.driver.find_element(By.ID, "m_1").click()
        # 5 | click | css=.col-md-12:nth-child(1) > .gridfullrow h3 |
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-12:nth-child(1) > .gridfullrow h3").click()
        # 6 | click | css=.col-md-12:nth-child(1) > .gridfullrow h3 |
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-12:nth-child(1) > .gridfullrow h3").click()
        # 7 | click | id=102 |
        self.driver.find_element(By.ID, "102").click()
        # 8 | click | linkText=Galleries |
        self.driver.find_element(By.LINK_TEXT, "Galleries").click()
        # 9 | click | css=.col-md-4:nth-child(1) .fullimageresponsive1 |
        self.vars["window_handles"] = self.driver.window_handles
        # 10 | selectWindow | handle=${win2802} |
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-4:nth-child(1) .fullimageresponsive1").click()
        # 11 | runScript | window.scrollTo(0,17.33333396911621) |
        self.vars["win2802"] = self.wait_for_window(2000)
        # 12 | click | css=.image-supply li:nth-child(3) > a |
        self.driver.switch_to.window(self.vars["win2802"])
        # 13 | click | linkText=Register Now |
        self.driver.execute_script("window.scrollTo(0,17.33333396911621)")
        # 14 | click | name=cl_FirstName |
        self.driver.find_element(By.CSS_SELECTOR, ".image-supply li:nth-child(3) > a").click()
        # 15 | type | name=cl_FirstName | Vintee1
        self.driver.find_element(By.LINK_TEXT, "Register Now").click()
        # 16 | click | name=cl_LastName |
        self.driver.find_element(By.NAME, "cl_FirstName").click()
        # 17 | type | name=cl_LastName | Mishraa
        self.driver.find_element(By.NAME, "cl_FirstName").send_keys("Vintee1")
        # 18 | click | name=cl_FirstName |
        self.driver.find_element(By.NAME, "cl_LastName").click()
        # 19 | type | name=cl_FirstName | Vinteee
        self.driver.find_element(By.NAME, "cl_LastName").send_keys("Mishraa")
        # 20 | click | name=cl_Qualifications |
        self.driver.find_element(By.NAME, "cl_FirstName").click()
        # 21 | type | name=cl_Qualifications | MCA
        self.driver.find_element(By.NAME, "cl_FirstName").send_keys("Vinteee")
        # 22 | click | name=cl_Occupation |
        self.driver.find_element(By.NAME, "cl_Qualifications").click()
        # 23 | click | name=cl_Occupation |
        self.driver.find_element(By.NAME, "cl_Qualifications").send_keys("MCA")
        # 24 | type | name=cl_Occupation | Python Developer
        self.driver.find_element(By.NAME, "cl_Occupation").click()
        # 25 | click | name=cl_Nationality |
        self.driver.find_element(By.NAME, "cl_Occupation").click()
        # 26 | type | name=cl_Nationality | Indian
        self.driver.find_element(By.NAME, "cl_Occupation").send_keys("Python Developer")
        # 27 | click | name=cl_ResearchTopic |
        self.driver.find_element(By.NAME, "cl_Nationality").click()
        # 28 | type | name=cl_ResearchTopic | Art
        self.driver.find_element(By.NAME, "cl_Nationality").send_keys("Indian")
        # 29 | click | name=cl_Address |
        self.driver.find_element(By.NAME, "cl_ResearchTopic").click()
        # 30 | type | name=cl_Address | Noida
        self.driver.find_element(By.NAME, "cl_ResearchTopic").send_keys("Art")
        # 31 | click | name=cl_Institute |
        self.driver.find_element(By.NAME, "cl_Address").click()
        # 32 | type | name=cl_Institute | Pisoftek
        self.driver.find_element(By.NAME, "cl_Address").send_keys("Noida")
        # 33 | click | id=email_address |
        self.driver.find_element(By.NAME, "cl_Institute").click()
        # 34 | type | id=email_address | vinteeshukla@gmail.com
        self.driver.find_element(By.NAME, "cl_Institute").send_keys("Pisoftek")
        # 35 | type | name=cl_Phone | +9811509416
        self.driver.find_element(By.ID, "email_address").click()
        # 36 | click | name=cl_Phone |
        self.driver.find_element(By.ID, "email_address").send_keys("vinteeshukla@gmail.com")
        # 37 | type | name=cl_Phone | 9811509416
        self.driver.find_element(By.NAME, "cl_Phone").send_keys("+9811509416")
        # 38 | click | name=cl_Fax |
        self.driver.find_element(By.NAME, "cl_Phone").click()
        # 39 | type | name=cl_Fax | 123456
        self.driver.find_element(By.NAME, "cl_Phone").send_keys("9811509416")
        # 40 | click | name=cl_Publications |
        self.driver.find_element(By.NAME, "cl_Fax").click()
        # 41 | type | name=cl_Publications | NO
        self.driver.find_element(By.NAME, "cl_Fax").send_keys("123456")
        # 42 | click | name=cl_OtherInformation |
        self.driver.find_element(By.NAME, "cl_Publications").click()
        # 43 | type | name=cl_OtherInformation | No
        self.driver.find_element(By.NAME, "cl_Publications").send_keys("NO")
        # 44 | click | css=.largebtn |
        self.driver.find_element(By.NAME, "cl_OtherInformation").click()
        # 45 | click | css=.largebtn |
        self.driver.find_element(By.NAME, "cl_OtherInformation").send_keys("No")
        self.driver.find_element(By.CSS_SELECTOR, ".largebtn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".largebtn").click()

    def test_content(self):
        # Test name: vims1
        # Step # | name | target | value
        # 1 | open | http://piswamp:81/vmis.in/ |
        self.driver.get("http://piswamp:81/vmis.in/")
        # 2 | setWindowSize | 1050x660 |
        self.driver.set_window_size(1050, 660)
        # 3 | click | linkText=ARCE |
        self.driver.find_element(By.LINK_TEXT, "ARCE").click()
        time.sleep(5)
        # 4 | click | css=.panel:nth-child(7) .accordion-toggle |
        self.driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(7) .accordion-toggle").click()
        time.sleep(5)
        # 5 | click | linkText=MORE |
        self.driver.find_element(By.LINK_TEXT, "MORE").click()
        time.sleep(5)
        # 6 | click | id=13 |
        self.driver.find_element(By.ID, "13").click()
        time.sleep(5)
        # 7 | click | id=17 |
        self.driver.find_element(By.ID, "17").click()
        time.sleep(5)
        # 8 | click | id=351 |
        self.driver.find_element(By.ID, "351").click()
        time.sleep(5)
        # 9 | click | id=350 |
        self.driver.find_element(By.ID, "350").click()
        time.sleep(5)
        # 10 | click | id=350 |
        self.driver.find_element(By.ID, "350").click()
        time.sleep(5)
        # 11 | doubleClick | id=350 |
        element = self.driver.find_element(By.ID, "350")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 12 | click | id=348 |
        self.driver.find_element(By.ID, "348").click()
        time.sleep(5)
        # 13 | click | id=348 |
        self.driver.find_element(By.ID, "348").click()
        time.sleep(5)
        # 14 | doubleClick | id=348 |
        element = self.driver.find_element(By.ID, "348")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 15 | click | id=19 |
        self.driver.find_element(By.ID, "19").click()
        time.sleep(5)
        # 16 | click | id=14 |
        self.driver.find_element(By.ID, "14").click()
        time.sleep(5)
        # 17 | click | id=14 |
        self.driver.find_element(By.ID, "14").click()
        time.sleep(5)
        # 18 | doubleClick | id=14 |
        element = self.driver.find_element(By.ID, "14")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        # 19 | click | id=104 |
        self.driver.find_element(By.ID, "104").click()
        time.sleep(5)
        # 20 | click | id=307 |
        self.driver.find_element(By.ID, "307").click()
        time.sleep(5)
        # 21 | click | id=104 |
        self.driver.find_element(By.ID, "104").click()
        time.sleep(5)

    def test_videos(self):
        # Test name: test3
        # Step # | name | target | value
        # 1 | open | http://piswamp:81/vmis.in/ |
        self.driver.get("http://piswamp:81/vmis.in/")
        # 2 | setWindowSize | 1052x660 |
        self.driver.set_window_size(1052, 660)
        # 3 | click | linkText=CAA |
        self.driver.find_element(By.LINK_TEXT, "CAA").click()
        # 4 | click | css=li:nth-child(4) li:nth-child(3) > a |
        self.vars["window_handles"] = self.driver.window_handles
        # 5 | selectWindow | handle=${win5405} |
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(4) li:nth-child(3) > a").click()
        # 6 | click | css=.ytp-play-button |
        self.vars["win5405"] = self.wait_for_window(2000)
        # 7 | mouseOver | css=.style-scope:nth-child(1) > #dismissible .yt-core-image--fill-parent-height |
        self.driver.switch_to.window(self.vars["win5405"])
        # 8 | mouseOut | css=.style-scope:nth-child(1) > #dismissible .yt-core-image--fill-parent-height |
        self.driver.find_element(By.CSS_SELECTOR, ".ytp-play-button").click()
        element = self.driver.find_element(By.CSS_SELECTOR,".style-scope:nth-child(1) > #dismissible .yt-core-image--fill-parent-height")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def test_aboutus(self):
        # Test name: test7
        # Step # | name | target | value
        # 1 | open | http://piswamp:81/vmis.in/ |
        self.driver.get("http://piswamp:81/vmis.in/")
        # 2 | setWindowSize | 1050x660 |
        self.driver.set_window_size(1050, 660)
        # 3 | click | linkText=ABOUT |
        self.driver.find_element(By.LINK_TEXT, "ABOUT").click()
        # 4 | click | linkText=MISSION STATEMENT |
        self.driver.find_element(By.LINK_TEXT, "MISSION STATEMENT").click()
        # 5 | click | linkText=VMIS RESOURCES |
        self.driver.find_element(By.LINK_TEXT, "VMIS RESOURCES").click()
        # 6 | click | linkText=OUR TEAM |
        self.driver.find_element(By.LINK_TEXT, "OUR TEAM").click()

    # def test_logout(self):
    # self.driver.find_element(By.LINK_TEXT, "LOGOUT").click()


if __name__=="__main__":
    pytest.main()
# t = TestTest1()
#
# t.setup_method("")
# t.test_login()
# t.test_test1()
# t.test_test2()
# t.test_test3()
# t.test_test4()
#
# t.teardown_method("")
