from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome('./chromedriver', chrome_options = chrome_options)

def func():
    driver.get('http://3.37.53.134:3005/')
    driver.execute_script('window.open("http://3.37.53.134:3005/");')

    i=0
    while True:
        i=i+1
        if i%10==0:
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.execute_script('window.open("http://3.37.53.134:3005/");')
        time.sleep(60)
            

try:
    func()
except Exception:
    for i in len(driver.window_handles):
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
    driver.quit()
