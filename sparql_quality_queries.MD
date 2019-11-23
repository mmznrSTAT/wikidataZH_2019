# SPARQL Quality Queries

## Municipalities with wrong preferred rank

The quality is good, if the query does not return any records.

[code link](https://w.wiki/CZd)
```SPARQL
SELECT ?Gemeinde ?preferredYear ?maxYear {
  FILTER(?preferredYear < ?maxYear)
  {
    SELECT ?Gemeinde (year(?Zeitpunkt_Stand) as ?preferredYear) WHERE {
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
      ?Gemeinde wdt:P31 wd:Q70208 ;
        wdt:P131 wd:Q11943 ;
        p:P1082 ?Einwohnerzahl. 
      ?Einwohnerzahl pq:P585 ?Zeitpunkt_Stand;
        wikibase:rank wikibase:PreferredRank .
    }
  }
  {
    SELECT ?Gemeinde (year(max(?Zeitpunkt_Stand2)) as ?maxYear) WHERE {
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    ?Gemeinde wdt:P31 wd:Q70208 ;
      wdt:P131 wd:Q11943 ;
      p:P1082 ?Einwohnerzahl2. 
    ?Einwohnerzahl2 pq:P585 ?Zeitpunkt_Stand2 .
  }
  GROUP BY ?Gemeinde
  }
}
```

## Quarters with wrong preferred rank

The quality is good, if the query does not return any records.

[code link](https://w.wiki/CZe)
```SPARQL
SELECT ?Quartier ?preferredYear ?maxYear {
  FILTER(?preferredYear < ?maxYear)
  {
    SELECT ?Quartier (year(?Zeitpunkt_Stand) as ?preferredYear) WHERE {
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    ?Quartier wdt:P31 wd:Q19644586 ;
      p:P1082 ?Einwohnerzahl. 
    ?Einwohnerzahl pq:P585 ?Zeitpunkt_Stand;
      wikibase:rank wikibase:PreferredRank .
    }
  }
  {
  SELECT ?Quartier (year(max(?Zeitpunkt_Stand2)) as ?maxYear) WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
  ?Quartier wdt:P31 wd:Q19644586 ;
    p:P1082 ?Einwohnerzahl2. 
  ?Einwohnerzahl2 pq:P585 ?Zeitpunkt_Stand2 .
  }
  GROUP BY ?Quartier
  }
}
```
