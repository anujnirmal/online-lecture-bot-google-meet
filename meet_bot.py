from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import datetime
import time
import keyboard

# rum kar

class google_meet:
    def join (self,meeting_link):
        self.bot = webdriver.Chrome("chromedriver.exe")
        self.bot.get("https://accounts.google.com/login")
        time.sleep(3)
        # self.bot.find_element_by_name("identifier").send_keys("madhukumarpaka-inft@atharvacoe.ac.in")
        emailField =  self.bot.find_element_by_name("identifier")
        emailField.send_keys("madhukumarpaka-inft@atharvacoe.ac.in")
        # self.bot.findElement(By.id("identifierNext")).c‌​lick()
        nextButtonEmail = self.bot.find_element_by_id("identifierNext")
        nextButtonEmail.click()
        time.sleep(5)
        pass_field = self.bot.find_element_by_name("password")
        pass_field.send_keys("superDELUXE1108")
        nextButtonPassword = self.bot.find_element_by_id("passwordNext")
        nextButtonPassword.click()
        time.sleep(5)
        self.bot.get(meeting_link)
        time.sleep(10)
        #keyboard.send("tab", do_press= True, do_release = True)
        #keyboard.send("tab", do_press= True, do_release = True)
        #keyboard.send("tab", do_press= True, do_release = True)  
        """keyboard.send("enter",do_press =True, do_release = True)
        time.sleep(5)
        keyboard.send("tab", do_press= True, do_release = True)
        keyboard.send("tab", do_press= True, do_release = True)
        keyboard.send("tab", do_press= True, do_release = True)  
        keyboard.send("enter",do_press =True, do_release = True)
        time.sleep(5)
        self.bot.quit()""" 



link = open("meeting_link.txt",'r').read()
#print(link)
jarvis = google_meet()
jarvis.join(link)


