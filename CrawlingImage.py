from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome() 

class Crawlling :
    def openWebsite(site_url) :
        driver.get(site_url)
        time.sleep(3)
        
        xpath="//*[text()='사업개요')]//"
        title_text = driver.find_element(By.XPATH, xpath).click()
        time.sleep(3)
        
                