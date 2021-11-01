# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:30:10 2021

@author: whdyd
"""

from selenium import webdriver
import schedule
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('chromedriver.exe', chrome_options=options) 

def visitWeb(options):
    if driver.current_url is not None:
        driver.close()
    driver.implicitly_wait(3) 
    driver.get('http://3.37.53.134:3005/')
    driver.implicitly_wait(3)
    driver.get_screenshot_as_file('main_headless.png')
    
schedule.every(10).second.do(visitWeb())

while True:
    schedule.run_pending()
    time.sleep(1)