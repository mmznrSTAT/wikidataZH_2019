# Wikidata ZH Hackathon 2019

We combine challenge 4 and 6. Our goal is to update the population of in wikidata based on open statistical data by the Kanton and the City of Zurich. 

Team: Katharina Kaelin, Roman Karavia, Sebastian Windeck, Philipp Rütimann, Matthias Mazenauer, Michael Grüebler

## Data Source

### Canton of Zurich
Dataset description: Einwohnerbestand Ende Jahr nach zivilrechtlichem Wohnsitz (ab 2010 inkl. vorläufig Aufgenommene, die seit mehr als einem Jahr in der Gemeinde leben, aber ohne Wochenaufenthalter und Asylbewerber)

Get Data as csv from Canton of Zurich via API
https://www.web.statistik.zh.ch:8443/gp/GP?type=EXPORT&indikatoren=1333&raumtyp=1&text=yes

Data Format: JSON or CSV

Attributes: 

Filter indikatoren=133 Bevölkerungs Personen / raumtyp=1 Alle Gemeinden

| Technical Name   | Fiel Description         | Definition  |
| ---------------- | ------------------------ | ----------- |
| RAUMEINHEIT_ID   | ID der Gemeinde          |          |
| DATEN_VORHANDEN  | true/false Datenstand    | true/false für Datenstand |
| RAUMEINHEIT_NAME | Gemeindename             | Name der Gemeinde  |
| BFS              | BFS Gemeindenummer       | Eindeuteige Gemeindenummer der Gemeinde gemäss BFS |
| ALLE_WERTE       | Anzahl Personen pro Jahr |  |

License: Open use. Must provide the source. 

Source: https://opendata.swiss/de/dataset/bevolkerung-pers

### City of Zurich
Dataset description: Wirtschaftliche Wohnbevölkerung der Stadt Zürich nach Statistischem Stadtquartier und Jahr, seit 1970. Datenqualität: 1970 – 1992 Fortschreibungsergebnisse, seit 1993 Bestand gemäss Register des Personenmeldeamtes.
https://data.stadt-zuerich.ch/dataset/bev_bestand_jahr_quartier_seit1970_od3240/resource/570f006e-2f2a-4b1f-9233-c4916c753475

Data Format: CSV

Attributes: 

| Technical Name  | Fiel Description            | Definition  |
| --------------- | --------------------------- | ----------- |
| StichtagDatJahr | Ereignisjahr                | Jahr         |
| QuarSort        | Stadtquartier (Sort)        | Offizielle ID des Statistischen Stadtquartiers (Integer) |
| QuarLang        | Stadtquartier               | Name des Statistischen Stadtquartiers (String) |
| AnzBestWir      | Wirtschaftliche Bevölkerung | Wirtschaftlich anwesende Personen (Integer) |

License: Creative Commons CCZero

Source: https://data.stadt-zuerich.ch/dataset/bev_bestand_jahr_quartier_seit1970_od3240

## Wikidata Definition

Important Identifiers in Wikidata (SPARQL terminology):

| Name           | Wikidata ID   |
| -------------- | ------------- | 
| Stadt Zürich   | Q72           | 
| Population     | P1082         | 
| Quartier       | Q19644586     | 
| Date (Year)    | P585          | 
| Preferred Rank | wikibase:rank |

## SPARQL Code Snippets

SPARQL Query to get Municipalities of the Canton Of Zurich from swiss topo endpoint

```
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX gn: <http://www.geonames.org/ontology#>
PREFIX schema: <http://schema.org/>
PREFIX dcterm: <http://purl.org/dc/terms/>

SELECT ?AdminUnit  ?Name
WHERE {
  ?AdminUnit gn:featureCode <http://www.geonames.org/ontology#A.ADM3> .
  ?AdminUnit schema:name ?Name .
  ?AdminUnit gn:parentADM1 ?Canton .
  ?Canton dcterms:issued ?Date .
  ?Canton <https://ld.geo.admin.ch/def/bfsNumber> ?bfsNumber .
  FILTER (?Date = "2019-01-01"^^xsd:date) .
  FILTER (?bfsNumber = "1"^^xsd:integer) .
}
``


