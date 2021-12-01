import urllib.request, urllib.error, urllib.parse
import codecs
url = 'http://www.catzen.co.za/listreet/about(listreet)-en.html'

response = urllib.request.urlopen(url=url)
html = response.read()


f = codecs.open('about(listreet)-en.html', 'w', 'utf-8')
f.write(response.read)
f.close