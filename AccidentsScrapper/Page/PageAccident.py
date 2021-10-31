# -*- coding: utf-8 -*-

import re

from AccidentsScrapper.Page import Page


class PageAccident(Page):
	def __init__(self, url):
		super().__init__(url)

	def get_data(self):

		data = {
			"titol_accident": self.find_titol(),
			"data_publicacio": self.find_data_publicacio(),
			"hora_publicacio": self.find_hora_publicacio(),
			"total_victimes": self.find_regex(r"(.*)víctim(.*?) (?P<data>\d+) (.*)", "persones que han mort"),
			"data_accident": self.find_regex(r"((.|\w|\S|\s)*?)DIA((\D)*)(?P<data>([0-3]?[0-9])(.*)((201[1-9])|(202[0-1])))(.*)", "DIA"),
			"hora_avis": self.find_regex(r"((.|\w|\S|\s)*?)HORA((\D)*)(?P<data>([0-2]?[0-9])(\.|\:)([0-6]?[0-9]))\D(.*)", "HORA"),
			"via": self.find_regex(r"((.|\w|\S|\s)*?)VIA(: )?(?P<data>.*)\s(.*)", "VIA"),
			"descripcio_accident": self.find_regex(r"((\w|\S|\s)*?)VIA(.*)\s(?P<data>(.|\w|\s|\S)*)").replace("\n", ""),
			"enllac": self.url
		}

		return data

	def find_titol(self):
		titol = self.soup.find("h1", {"class": "NG-menu__title"}).text
		return re.sub(r"(^(\n|\t|\s)*)|(((\n|\t|\s)*)$)", "", titol)

	def find_data_publicacio(self):
		return self.soup.find("div", {"class": "noticia_detalls_cont"}).findAll("span")[0].text

	def find_hora_publicacio(self):
		return self.soup.find("div", {"class": "noticia_detalls_cont"}).findAll("span")[1].text

	def find_regex(self, regex, keyword=None):
		text = self.soup.find("div", {"class": "basic_text_peq"}).text

		if (keyword is not None) and (keyword not in text):
			return "N/A"

		try:
			match = re.match(regex, text)

			return match.group("data")

		except:
			return "N/A"