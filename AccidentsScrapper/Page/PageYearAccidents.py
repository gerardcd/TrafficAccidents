from AccidentsScrapper.Page import Page


class PageYearAccidents(Page):
	def __init__(self, url):
		super().__init__(url)

	def get_year_accidents_urls(self):

		# Obtenir els enllaços d'accidents visibles a la primera pàgina
		accidents_urls = self.get_visible_year_accidents_urls()

		# Mentre es pugui paginar
		while self.paginate():

			# S'afageixen els enllaços d'accidents visibles a la pàgina actual
			accidents_urls += self.get_visible_year_accidents_urls()

		# Es filtren els enllaços a documents PDF
		return list(filter(lambda url: ".pdf" not in url, accidents_urls))

	def get_visible_year_accidents_urls(self):

		# Es troben els enllaços als accidents
		accidents_div = self.soup.find("div", {"class": "llistat_destacat_noticies"})
		accidents_urls = accidents_div.findChildren("a")

		# S'extreu l'atribut href de tots els elements de tipus enllaç que s'han trobat
		return list(map(lambda a: a.attrs["href"], accidents_urls))

	def paginate(self):

		# S'obté el botó a la pàgina següent
		next_button = self.soup.find("a", {"class": "seguent"})

		# Si està desactivat es retorna False indicant que no s'ha pogut paginar
		if "desactivat" in next_button.attrs["class"]:
			return False

		# S'actualitza amb el contingut de la següent pàgina
		self.set_page(next_button.attrs["href"])

		# Es retorna True indicant que s'ha pogut paginar
		return True
