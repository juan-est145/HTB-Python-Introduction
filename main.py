import requests
import sys
from bs4 import BeautifulSoup
import re

URL = "http://127.0.0.1"

def getHtml(url):
	res = requests.get(url)

	if res.status_code != 200:
		print(f'HTTP status code of {res.status_code} returned, but 200 was expected. Exiting...')
		exit(1)
	
	else:
		return res.content.decode()

if len(sys.argv) -1 > 0:
	URL = sys.argv[1]

def createMap(list: list):
	map = {}
	for item in list:
		map[item] = map.setdefault(item, 0) + 1
	return map

rawContent = getHtml(URL)
html = BeautifulSoup(rawContent, "html.parser")
text = html.getText()
allWords = re.findall(r'\w+', text)

map = createMap(allWords)

