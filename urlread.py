from selenium import webdriver
import os
import codecs

file1 = open('url.csv', 'r')
Lines = file1.readlines()

for line in Lines:
    if 'https' in line.strip():
        url = line.strip()
        url = url.replace('"','')
        print(url)
        split_url = url.split("postcodezip/", 1)
        substring = split_url[1]
        print(substring)
        driver = webdriver.Chrome('./chromedriver')
        driver.implicitly_wait(0.5)
        driver.maximize_window()
        driver.get(url)
        pageSource = driver.page_source
        # get file path to save page
        completeName = os.path.join("C:\\Users\\CyrusSmith\\Desktop\\postcodezip", substring)
        driver.implicitly_wait(2.0)
        file_object = codecs.open(completeName, "w", "utf-8")
        html = driver.page_source
        file_object.write(html)
        driver.implicitly_wait(0.5)
driver.close()