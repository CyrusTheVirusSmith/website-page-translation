from selenium import webdriver


file1 = open('urlaa.csv', 'r')
Lines = file1.readlines()

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()

for line in Lines:
    if 'https' in line.strip():
        url = line.strip()
        with driver.get(url=url):

            driver.implicitly_wait(3)

        driver.close()