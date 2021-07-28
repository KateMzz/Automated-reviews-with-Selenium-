from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


class Comment_Students:
    option = webdriver.ChromeOptions()
    #option.add_argument('--disable-blink-features=AutomationControlled')
    #option.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome("C:\Development\chromedriver")  

    def log_in(self):

        self.browser.maximize_window()  
        self.browser.get("http://iyes.vnresource.org/TeacherPortal/HomePage.aspx")
        username = self.browser.find_element_by_name("txtUserName")
        username.clear()
        time.sleep(1)
        username.send_keys("katerina")
        time.sleep(1)
        password = self.browser.find_element_by_name("txtPass")
        password.send_keys("123")
        time.sleep(1)
        log_in = self.browser.find_element_by_name("btnLogin")
        time.sleep(1)
        log_in.click()
        print("log in")

    def open_attendance_page(self):
        page = self.browser.find_element_by_id("liStudentAttendance")
        time.sleep(1)
        page.click()
        


    def comment_or_not(self):
        #group = self.browser.find_element_by_xpath("//div[@class='col-lg-2 col-md-2 col-sm-2 col-xs-12 ebm-control-info'][1]")
        time.sleep(1)
        # self.browser.implicitly_wait(10)
        self.browser.execute_script("window.scrollTo(1000,document.head.scrollHeight);")
        time.sleep(1)
        # group = self.browser.find_element_by_xpath("//div[@class='col-lg-2 col-md-2 col-sm-2 col-xs-12 ebm-control-info'][1]")
        # group = self.browser.find_element(By.XPATH,"//select[@id='ctl13_ddlClass']")
        # group.click()
        # group_sunday = self.browser.find_element_by_xpath("//select[@id='ctl13$ddlClass']")
        iframe = self.browser.find_element_by_xpath('//*[@id="DailyRecord"]/iframe')
        ##DailyRecord > iframe
        #//*[@id="DailyRecord"]/iframe  
        self.browser.switch_to.frame(iframe)
        dropdown = self.browser.find_element_by_id('ctl13_ddlClass').click()
        KD_ONE = self.browser.find_element(By.XPATH, '//*[text()="KD1.3-0321"]')
        SK_ONE = self.browser.find_element(By.XPATH, '//*[text()="SK1.4-0321"]')
        SK_O_ONE = self.browser.find_element(By.XPATH, '//*[text()="SK0.1-0121"]')
        SK_ONE = self.browser.find_element(By.XPATH, '//*[text()="SK1.2-0121"]')
        SK_0_TWO = self.browser.find_element(By.XPATH, '//*[text()="SK0.2-1120"]')
        SK_FOR_THREE = self.browser.find_element(By.XPATH, '//*[text()="SK4.3-1020"]')
        SK_FOR_TWO = self.browser.find_element(By.XPATH, '//*[text()="SK4.2-1020"]')
        MINDSET_A = self.browser.find_element(By.XPATH, '//*[text()="MINDSET A-0121"]')
        SK_ONE_ONE = self.browser.find_element(By.XPATH, '//*[text()="SK1.1-1.8"]')
        SK_THREE = self.browser.find_element(By.XPATH, '//*[text()="SK3.1-0121"]')
        KD_TWO = self.browser.find_element(By.XPATH, '//*[text()="KD2.4-1220"]')
        ELE_TWO = self.browser.find_element(By.XPATH, '//*[text()="ELE2.1-0121"]')

        my_classes = [KD_ONE, SK_ONE, SK_O_ONE, SK_ONE, SK_0_TWO, SK_FOR_THREE, SK_FOR_TWO, MINDSET_A, SK_ONE_ONE, SK_THREE, KD_TWO, ELE_TWO]
        my_classes = self.browser.find_elements_by_xpath('//select[@name="ctl13$ddlClass"]/option')
       

        learning_diary = self.browser.find_element(By.XPATH, "//td/input[@class='btn btn-sm btn-warning']")
        contents = ['Matter has three forms: solid, liquid, and gas.',
                       'Draw and identify lines and angles, and classify shapes by properties of their lines and angles.',
                        'Write arguments to support claims in an analysis of substantive topics or texts, using valid reasoning and relevant and sufficient evidence. Provide a concluding statement or section that follows from and supports the argument presented.',
               ]
        
        homework=['Page 24, ex 5. Be able orally describe characteristics of liquids, solids, and gases to a partner.',
                'Page 56, ex 1. Learn descriptions of triangles and their angles',
                'Page 78, ex 9.  Use transitional phrases (e.g., as a result) in writing']
                    
        count = 0

        for each_class in my_classes:
            # try:
            #     iframe = self.browser.find_element_by_xpath('//*[@id="DailyRecord"]/iframe')
            # ##DailyRecord > iframe
            # #//*[@id="DailyRecord"]/iframe
            #     print("Boobs")
            #     self.browser.switch_to.frame(iframe)
            # except:
            #     pass
            dropdown = self.browser.find_element_by_id('ctl13_ddlClass')
            time.sleep(2)
            dropdown.click()
            print("clicked dropdown")
            time.sleep(2)
            self.browser.execute_script("window.scrollBy(0,1000)","")
            time.sleep(3)
            lesson_content = self.browser.find_element_by_xpath('//div[@id="ctl13_UpdatePanel1"]/textarea')
            lesson_content.clear()
            lesson_content.send_keys(contents[count])           
            homework_but = self.browser.find_element_by_xpath('//div/textarea[@id="ctl13_txtHomeWork"]')
            homework_but.clear()
            homework_but.send_keys(homework[count])
            count+=1
            time.sleep(1)
            teach_comment = self.browser.find_element_by_xpath('//div/textarea[@id="ctl13_txtTeacherComment"]')
            teach_comment.clear()
            teach_comment.send_keys("Good class, worked well")
            time.sleep(1)
            note = self.browser.find_element_by_xpath('//div/textarea[@id="ctl13_txtNote"]')
            note.clear()
            note.send_keys("Don't forget your workbook")
            time.sleep(1)
            # save_but = self.browser.find_element_by_name('//div/input[@name="ctl13$btnSave"]')
            time.sleep(2)
            self.browser.execute_script("window.scrollBy(1000,0)","")
            time.sleep(1)
            try:
                dropdown.send_keys(Keys.ARROW_DOWN)
                print("clicked class")
                time.sleep(2)
            except Exception as e:
                print(e)
                 
            # if learning_diary:
            #     learning_diary.click()
            #     print("clicked learning diary")
            #     continue
            # else:
            #     print("learning diary not available")
                
            time.sleep(2)
                  

comments = Comment_Students()
comments.log_in()
comments.open_attendance_page()
comments.comment_or_not()



# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.second_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
