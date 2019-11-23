# Wikidata ZH Hackathon 2019

Challenge 4 and 6
Put data on Wikidata


## Ressources:

Wichtige Identifiers für Wikidata:
Stadt Zürich: q72
Population: P1082

Get Data as csv from Canton of Zurich via API
https://www.web.statistik.zh.ch:8443/gp/GP?type=EXPORT&indikatoren=133&raumtyp=1&text=yes

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
```


