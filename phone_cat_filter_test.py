#Phone Cat Sorting.
#Tests the "Alphabetical" sorting filter function on
#the "Google Phone Gallery" page.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

#Opens Phone Cat.
driver = webdriver.Chrome()
driver.get("http://x13.se/~applet/app")
time.sleep (5)

#Selects the "Alphabetical" filter in the "Sort by" drop-down menu
filterselect = Select (driver.find_element_by_xpath("//select"))
filterselect.select_by_value("name")
time.sleep(5)

#Extracts the name of the first five items in the list into the Terminal.
itemone = driver.find_element_by_xpath("//phone-list/div/div/div[2]/ul/li[1]/a[2]")
print(itemone.text)
itemtwo = driver.find_element_by_xpath("//phone-list/div/div/div[2]/ul/li[2]/a[2]")
print(itemtwo.text)
itemthree = driver.find_element_by_xpath("//phone-list/div/div/div[2]/ul/li[3]/a[2]")
print(itemthree.text)
itemfour = driver.find_element_by_xpath("//phone-list/div/div/div[2]/ul/li[4]/a[2]")
print(itemfour.text)
itemfive = driver.find_element_by_xpath("//phone-list/div/div/div[2]/ul/li[5]/a[2]")
print(itemfive.text)
time.sleep(5)
driver.close()
