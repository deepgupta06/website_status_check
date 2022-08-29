from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import datetime


chrome_driver_path = "../chromedriver.exe"
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("useAutomationExtension", False)

#chromeOptions.add_argument("headless")
driver = webdriver.Chrome(chrome_driver_path, chrome_options=chromeOptions, 
                        desired_capabilities=chromeOptions.to_capabilities())
driver.minimize_window()
def get_element_by_xpath(driver, xpath):
    counter = 0
    while True:
        try:
            webelement = driver.find_element(by=By.XPATH, value=xpath)
            return webelement
        except:
            time.sleep(1)
            counter+=1
            if counter==15:
                raise Exception(f"Element not found")

while True:
    url = "https://www.isitdownrightnow.com/cx.cnca.cn.html"
    website_link = driver.get(url)
    
    status_xpath = '//*[@id="serverdata"]/div[5]/span'
    while True:
        status_element = get_element_by_xpath(driver, status_xpath)
        status_text = status_element.text
        if status_text=="":
            time.sleep(1)
        else:
            data = []
            present_time = datetime.datetime.now()
            present_time = present_time.strftime("%Y/%m/%d %H:%M:%S")
            data.append(present_time)
            for i in range(2,6):
                element_xpath = f'//*[@id="serverdata"]/div[{i}]/span'
                web_element = get_element_by_xpath(driver, element_xpath)
                text = web_element.text
                data.append(web_element.text)
            print("    ".join(data))
            data.append("\n")
            with open("../output/DOWN_UP.txt", "a+", newline='') as outputFile:
                outputFile.write(",".join(data))
            break
    time.sleep(5)
            
            

