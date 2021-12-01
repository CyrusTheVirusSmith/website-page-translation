from selenium import webdriver
import codecs

file1 = open('url2.csv', 'r')
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
        tl = tl[0:5]
        print(tl)
        driver.implicitly_wait(0.5)
        driver.get(url=url)
        location = "C:\\Users\\CyrusSmith\\Desktop\\postcodezip\\"+substring[:-7]+tl+'.html'
        print(location)
        with codecs.open(location, 'w', 'utf-8') as f:
            f.write(driver.page_source)
        driver.implicitly_wait(2.0)

driver.close()