# -*- coding: utf-8 -*-

import re

from AccidentsScrapper.Page import Page


class PageAccident(Page):
	def __init__(self, url):
		super().__init__(url)

	def get_data(self):
		# S'obtenen les dades de l'accident de la pàgina semiestructurada
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
		# Es troba el títol de l'accident, eliminant els espais en blanc i els salts de línia que hi puguin haver al principi i al final
		titol = self.soup.find("h1", {"class": "NG-menu__title"}).text
		return re.sub(r"(^(\n|\t|\s)*)|(((\n|\t|\s)*)$)", "", titol)

	def find_data_publicacio(self):
		# Es troba la data de publicació de la nota de premsa
		return self.soup.find("div", {"class": "noticia_detalls_cont"}).findAll("span")[0].text

	def find_hora_publicacio(self):
		# Es troba l'hora de publicació de la nota de premsa
		return self.soup.find("div", {"class": "noticia_detalls_cont"}).findAll("span")[1].text

	# Funció per a trobar continguts usant expressions regulars
	def find_regex(self, regex, keyword=None):

		# S'obte el contingut textual de l'accident
		text = self.soup.find("div", {"class": "basic_text_peq"}).text

		# Es comprova la presència d'una paraula clau (opcional per a camps que no estan sempre presents)
		if (keyword is not None) and (keyword not in text):
			return "N/A"

		try:
			# Es busca el contingut mitjançant l'expressió regular
			match = re.match(regex, text)

			# Es retorna el resultat del grup coincident amb nom data (ha d'estar present a l'expressió regular)
			return match.group("data")

		except:
			return "N/A"
