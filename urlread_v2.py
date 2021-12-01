from selenium import webdriver
import codecs
import time

file1 = open('urlaa.csv', 'r')
Lines = file1.readlines()

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()

for line in Lines:
    if 'https' in line.strip():
        url = line.strip()
        print(url)
        split_url = url.split("postcodezip/", 1)
        print(split_url)
        substring = split_url[1]
        print(substring)
        tl_split_url = url.split("&tl=", 1)
        print(tl_split_url)
        tl = tl_split_url[1]
        print(tl)
        tl = tl[0:2]
        print(tl)
        driver.implicitly_wait(0.5)
        driver.get(url=url)
        time.sleep(8)
        location = "C:\\Users\\CyrusSmith\\Desktop\\tmp\\"+substring[:-7]+tl+'.html'
        print(location)
        with codecs.open(location, 'w', 'utf-8') as f:
            f.write(driver.page_source)
        driver.implicitly_wait(3)

driver.close()