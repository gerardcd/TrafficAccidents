import csv

from Database import Database

HEADER = ["Point"]

database = Database("dades_1635702440.4170232.csv")

with database, open("mapa.csv", "w+") as map_file:
	csv_reader = database.get_reader()
	csv_writer = csv.writer(map_file, quotechar="\"", quoting=csv.QUOTE_ALL)

	csv_writer.writerow(HEADER)

	for row in csv_reader:
		text = row["via"]

		if ", al punt quilomètric " in text:
			text = text.replace(": ", "").replace(":", "").replace(" : ", "").split(", al punt quilomètric ")

			carretera = text[0]
			km = text[1].split(" ")[0].split(",")[0]

			line = [f"{carretera}, {km}, catalunya"]

			csv_writer.writerow(line)
