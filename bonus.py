from main import getHtml
import sys
from bs4 import BeautifulSoup
import re

def main():
	URL = "http://127.0.0.1"
	if len(sys.argv) -1 > 0:
		URL = sys.argv[1]
	rawContent = getHtml(URL)
	html = BeautifulSoup(rawContent, "html.parser")
	text = html.get_text()

	lines = re.findall(r'^.*free trial.*$', text, re.IGNORECASE | re.MULTILINE)
	print(lines)

if __name__ == "__main__":
	main()
