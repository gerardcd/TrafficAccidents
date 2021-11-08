from src.AccidentsScrapper.Page.PageYearsIndex import PageYearsIndex
from src.AccidentsScrapper.Page.PageYearAccidents import PageYearAccidents
from src.AccidentsScrapper.Page.PageAccident import PageAccident

from src.Database import Database

INDEX_URL = "/ca/el_servei/premsa_i_comunicacio/comunicats_d_accidents_mortals/"


class AccidentsScrapper:
	def __init__(self):
		self.page_years_index = PageYearsIndex(INDEX_URL)

	def scrap(self):
		database = Database()
		with database:
			database.write_header()
			self.get_data(database)

	def get_data(self, database):

		# Obtenir els índexs anuals
		years_urls = self.page_years_index.get_years_urls()

		# Per cada pàgina d'index anual
		for year_url in years_urls:

			# S'obtenen tots els accidents de l'any
			page_year_accidents = PageYearAccidents(year_url)
			page_year_accidents = page_year_accidents.get_year_accidents_urls()

			# Per cada accident
			for accident_url in page_year_accidents:

				# S'extreu la informació de l'accident
				page_accident = PageAccident(accident_url)
				accident_data = page_accident.get_data()

				# S'escriu la informació extreta a la base de dades (fitxer CSV)
				database.write_record(accident_data)
