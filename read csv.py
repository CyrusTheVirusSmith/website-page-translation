from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import csv
import codecs

file = open('url.csv')
type(file)
csvreader = csv.reader(file)
url = []
url = next(csvreader)
url = next(csvreader)
print(url)
file = open('saveas.csv')
type(file)
csvreader = csv.reader(file)
saveas = []
saveas = next(csvreader)
saveas = next(csvreader)
print(saveas)

url = next(csvreader)
saveas = next(csvreader)
print(url)
print(saveas)