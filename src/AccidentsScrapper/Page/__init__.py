import requests
from bs4 import BeautifulSoup

SITE_URL = "http://transit.gencat.cat/"


class Page:
	def __init__(self, url):
		self.url = url

		self.page = None
		self.soup = None

		self.set_page(url)

	def set_page(self, url):
		self.page = requests.get(SITE_URL + url)
		self.soup = BeautifulSoup(self.page.content)
