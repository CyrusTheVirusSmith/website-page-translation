#---------------------------------------
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "https://www.catzen.co.za/listreet/home-page(listreet)-en.html"
html = urlopen(url).readlines()
soup = BeautifulSoup(html, features="html.parser")

reg_str = "<(.*?)>"
res = re.findall(reg_str, html)
print(res)

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out
# get text
#text = soup.get_text()

# break into lines and remove leading and trailing space on each
#lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
#chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
#text = '\n'.join(chunk for chunk in chunks if chunk)

#print(text)
#from bs4 import BeautifulSoup
#from urllib.request import Request, urlopen
#import re
#import html2text
#import codecs

#with codecs.open("C:\\Users\\CyrusSmith\\Desktop\\files\\home-page(listreet)-en.html",'r', 'utf-8') as file:
#    html_page = file.read()
#    soup = BeautifulSoup(html_page, "html.parser")

# soup is a BeautifulSoup object Type which contains HTML

#h = html2text.HTML2Text()
#h.ignore_links = True

#f = codecs.open("C:\\Users\\CyrusSmith\\Desktop\\files\\html_text.txt", "w", 'utf-8')         # Creating html_text.txt File

#for line in h.handle(str(soup)):       # handle() Function only accepts string as parameter
#	f.write(line)                      # That's why converted soup object to string str(soup)

#f.close()
#--------------------------------