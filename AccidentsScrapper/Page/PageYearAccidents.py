from AccidentsScrapper.Page import Page


class PageYearAccidents(Page):
	def __init__(self, url):
		super().__init__(url)

	def get_year_accidents_urls(self):
		accidents_urls = self.get_visible_year_accidents_urls()

		while self.paginate():
			accidents_urls += self.get_visible_year_accidents_urls()

		return list(filter(lambda url: ".pdf" not in url, accidents_urls))

	def get_visible_year_accidents_urls(self):
		accidents_div = self.soup.find("div", {"class": "llistat_destacat_noticies"})
		accidents_urls = accidents_div.findChildren("a")

		return list(map(lambda a: a.attrs["href"], accidents_urls))

	def paginate(self):
		next_button = self.soup.find("a", {"class": "seguent"})

		if "desactivat" in next_button.attrs["class"]:
			return False

		self.set_page(next_button.attrs["href"])

		return True
