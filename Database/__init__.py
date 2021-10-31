import time
from os import path
import csv

COLUMNS = ["titol_accident", "data_publicacio", "hora_publicacio", "total_victimes", "data_accident", "hora_avis", "via", "descripcio_accident", "enllac"]


class Database:
	def __init__(self):
		self.file_name = "dades_" + str(time.time()) + ".csv"
		self.directory = "./storage"
		self.file_path = path.join(self.directory, self.file_name)

	def __enter__(self):
		self.file = open(self.file_path, "w+")
		self.csv_writer = csv.writer(self.file, delimiter=";", quotechar="\"", quoting=csv.QUOTE_MINIMAL)
		self.csv_writer.writerow(COLUMNS)

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.file.close()

	def write_record(self, record):
		row = [
			record[col] if col in record else None
			for col in COLUMNS
		]

		self.csv_writer.writerow(row)

		print([x[0:10] for x in row])
