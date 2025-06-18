import requests
import sys

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