from AccidentsScrapper.Page.PageYearsIndex import PageYearsIndex
from AccidentsScrapper.Page.PageYearAccidents import PageYearAccidents
from AccidentsScrapper.Page.PageAccident import PageAccident

from Database import Database

INDEX_URL = "/ca/el_servei/premsa_i_comunicacio/comunicats_d_accidents_mortals/"


class AccidentsScrapper:
	def __init__(self):
		self.page_years_index = PageYearsIndex(INDEX_URL)

	def scrap(self):
		database = Database()
		with database:
			self.get_data(database)

	def get_data(self, database):
		years_urls = self.page_years_index.get_years_urls()

		for year_url in years_urls:
			page_year_accidents = PageYearAccidents(year_url)
			page_year_accidents = page_year_accidents.get_year_accidents_urls()

			for accident_url in page_year_accidents:
				page_accident = PageAccident(accident_url)
				accident_data = page_accident.get_data()

				database.write_record(accident_data)
