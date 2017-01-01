#Phone Cat Sorting.
#Tests the search function on the "Google Phone Gallery" page
#by searching for "Dell Venue" in the search bar.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Opens Phone Cat.
driver = webdriver.Chrome()
driver.get("http://x13.se/~applet/app")
driver.maximize_window()
time.sleep (5)

#Searches for "Dell Venue" in the search bar.
search = driver.find_element_by_xpath("//input")
search.click()
time.sleep(2)
#Searches in all lower caps and prints out the result into the Terminal.
search.send_keys("dell venue")
time.sleep(2)
searchverify = driver.find_element_by_xpath("//div/div[2]/ul/li/a[2]")
time.sleep(3)
print (searchverify.text)
time.sleep(3)
search.clear()
time.sleep(5)

#Enters the search term in all caps in the search bar.
search.click()
time.sleep(2)
search.send_keys("DELL VENUE")
time.sleep(2)
print (searchverify.text)
time.sleep(3)
search.clear()
time.sleep(5)

#Enters the search term in both upper and lower case.
search.click()
time.sleep(2)
search.send_keys("Dell Venue")
time.sleep(2)
print(searchverify.text)
time.sleep(3)
search.clear()
time.sleep(5)
driver.close()
