from AccidentsScrapper.Page import Page


class PageYearsIndex(Page):
	def __init__(self, url):
		super().__init__(url)

	def get_years_urls(self):
		years_div = self.soup.find("div", {"id": "center_2R"})
		years_urls = years_div.findChildren("a")

		return list(map(lambda a: a.attrs["href"], years_urls))
