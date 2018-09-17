""" This code gets XML files of all bacterial CRISPRs found on the CRISPRdb,
    http://crispr.i2bc.paris-saclay.fr/crispr/
    The data at the db is arranged by confirmed CRISPRS and questonable structures. As this data is being used
    to construct a training set for a HMM based classifier, it will scrape only confirmed CRISPRs."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
from pprint import pprint
import xml.etree.ElementTree as ET

os.getcwd()
print("Running: ")
#Configure webdriver, this script uses Google Chrome. Does not use headless as the end result is download of a file.
option = webdriver.ChromeOptions()
#option.add_argument("--headless")

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')#, chrome_options=option)
driver.get("http://crispr.i2bc.paris-saclay.fr/crispr/")
driver.implicitly_wait(10)

#driver variables

#This driver selected all elements in the bacterial table without questionable structures on 09/16/2018
bacterialCRISPRsXPath = driver.find_elements_by_xpath(
    "/html/body/div[6]/form/div/table[1]/tbody/tr/td[text()[contains(., 'CRISPRs)')]]/parent::tr/td//input "
    "| /html/body/div[6]/form/div/table[1]/tbody/tr/td[text()[contains(., 'CRISPR)')]]/parent::tr/td/input")
submitButton = driver.find_element_by_xpath("/html/body/div[6]/form/div/input[1]")

#driver actions
#iterate through the list of bacterial crisprs and select them.
for box in bacterialCRISPRsXPath:
    box.click()
#click the submit button
submitButton.click()




pprint(bacterialCRISPRsXPath)


