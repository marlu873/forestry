from bs4 import BeautifulSoup
import requests

def parse_page(url):
	# Get the page content and set up a new parser.
	response = requests.get(url)
	content = response.content
	return BeautifulSoup(content, 'html.parser')
