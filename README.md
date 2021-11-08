# Traffic accidents in Catalonia

Aquest repositori conté el codi necessari per a realitzar web scrapping sobre el lloc web de l'Oficina de Premsa i Comunicació del Servei Català de Trànsit de la Generalitat de Catalunya i extreu la informació dels accidents de totes les notes de premsa publicades en aquest lloc. També conte el dataset obtingut i codi per a extreure les localitzacions dels accidents i crear un nou dataset que pot ser directament importat a Google Maps.

Les respostes a l'enunciat de la pràctica es poden trobar a l'arxiu TCVD.gerard.cegarra.PRAC1.pdf d'aquest repositori.

## Components del grup

Gerard Cegarra Dueñas

## Estructura del codi

* __main.py__: script principal per a executar el procés d'scrapping
* __AccidentsScrapper__: implementació del procés d'scrapping
* __\_\_init\_\_.py__: classe principal del scrapper
* __Page__: implementació del procés d'scrapping de les diferents pàgines
* __\_\_init\_\_.py__: classe base per a les pàgines
* __PageYearsIndex.py__: pàgina amb l'índex dels diferents anys
* __PageYearAccidents.py__: pàgina amb l'índex d'accidents d'un any en concret
* __PageAccident.py__: pàgina amb la informació d'un accident en concret
* __Database__: implementació de la gestió de fitxers CSV
* __\_\_init\_\_.py__: classe principal de la gestió de fitxers CSV
* __map__: generació del dataset secundari amb les localitzacions dels accidents
* __create_map_data.py__: codi per a la creació del dataset secundari
* __mapa.csv__: dataset amb la localització extreta dels accidents
* __mapa.png__: foto del mapa resultant de Google Maps després d'importar el dataset secundari
* __storage__: magatzem per als resultats del procés d'scrapping
* __dades_1635702440.4170232.csv__: dataset resultant del procés d'scrapping

## DOI Zenodo del dataset generat

10.5281/zenodo.5652001