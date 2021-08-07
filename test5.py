import os
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



link = "http://suninjuly.github.io/redirect_accept.html"

try:
    from selenium import webdriver
    browser = webdriver.Chrome()
    
    browser.get(link)
    window_before = browser.window_handles[0]
    
    
    button=browser.find_element_by_xpath("//button[@type='submit']").click()
    window_after = browser.window_handles[1]
    browser.switch_to_window(window_after)
    value=browser.find_element_by_id('input_value').text
    print(value)
    ivalue=calc(value)
    print(ivalue)
    input=browser.find_element_by_id("answer").send_keys(str(ivalue))
    button=browser.find_element_by_xpath("//button[@type='submit']").click()
    


   


finally:
    time.sleep(5)
    browser.quit()

