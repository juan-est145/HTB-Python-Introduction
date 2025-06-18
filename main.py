import requests
import sys
from bs4 import BeautifulSoup
import re

def getHtml(url):
	res = requests.get(url)

	if res.status_code != 200:
		print(f'HTTP status code of {res.status_code} returned, but 200 was expected. Exiting...')
		exit(1)
	
	else:
		return res.content.decode()

def createMap(list: list):
	map = {}
	for item in list:
		map[item] = map.setdefault(item, 0) + 1
	return map

def printResults(list: list, length = 10):
	if length > len(list):
		length = len(list)
	for x in range(length):
		print(f"The word {list[x][0]} appears {list[x][1]} times")

if __name__ == "__main__":
	URL = "http://127.0.0.1"
	
	if len(sys.argv) -1 > 0:
		URL = sys.argv[1]
	rawContent = getHtml(URL)
	html = BeautifulSoup(rawContent, "html.parser")
	text = html.getText()
	allWords = re.findall(r'\w+', text)

	map = sorted(createMap(allWords).items(), key=lambda item: item[1], reverse=True)
	printResults(map)


