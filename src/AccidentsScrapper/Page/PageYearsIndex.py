from src.AccidentsScrapper.Page import Page


class PageYearsIndex(Page):
	def __init__(self, url):
		super().__init__(url)

	def get_years_urls(self):
		# Es troben els enllaços als índexs anuals d'accidents
		years_div = self.soup.find("div", {"id": "center_2R"})
		years_urls = years_div.findChildren("a")

		# S'extreu l'atribut href de tots els elements de tipus enllaç que s'han trobat
		return list(map(lambda a: a.attrs["href"], years_urls))
