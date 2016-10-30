import urllib2
from bs4 import BeautifulSoup
url = "http://www.twitch.tv/"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
#print soup.prettify()
print soup.p

all_Items=soup.find_all()
for item in all_Items:
	#if "game" in item:
		print item
	#if item.get("title") != None:
	#	print item.get("title")
#all_tables=soup.find_all('table')
#right_table=soup.find('table', class_='wikitable sortable plainrowheaders')
