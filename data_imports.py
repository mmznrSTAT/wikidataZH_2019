import pandas as pd
import requests
import zipfile
import os
import shutil
from SPARQLWrapper import SPARQLWrapper, JSON, XML
import logging

def import_wikidata():
    """
    Generates a SPARQL query and converts this data to pandas datadframe
    :return: pd.Dataframe['wikidata_id','date','population','qualifier']
    """
    # Q70208 Gemeinde
    # Q11943 Kanton Zürich
    # P1082 Einwohner
    # P585 Zeitmpunkt
    query = """
        SELECT ?wikidata_id ?bfs_id ?date ?population ?qualifier
            WHERE
            {
              
              ?wikidata_id wdt:P31 wd:Q70208.
              ?wikidata_id wdt:P131 wd:Q11943.
              ?wikidata_id p:P1082 ?myvalue.
              ?wikidata_id wdt:P771 ?bfs_id.
              ?myvalue pq:P585 ?date.
              ?myvalue ps:P1082 ?population.
              ?myvalue wikibase:rank ?qualifier.
              SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
            }
        """
    
    sparql = SPARQLWrapper("https://query.wikidata.org/sparql", agent = "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    
    result = results['results']['bindings']

    population = []
    for p in result:
        mon = {
            'wikidata_id': p['wikidata_id']['value'].replace('http://www.wikidata.org/entity/', ''),
            'bfs_id' : p['bfs_id']['value'],
            'date': p['date']['value'],
            'population': p['population']['value'],
            'qualifier': p['qualifier']['value'].replace('http://wikiba.se/ontology#', ''),
        }
        population.append(mon)
    
    
    pop = pd.DataFrame(population)
    pop['date'] = pop.date.str.slice(0, 10)
    pop['bfs_id'] = pop['bfs_id'].astype(int)
    logging.info('Import Wikidata: extracted {0} entries successful'.format(pop['date'].count()))
    return pop

def import_KT():
    URL = "https://www.web.statistik.zh.ch:8443/gp/GP?type=EXPORT&indikatoren=133&raumtyp=1&export=csv"

    r = requests.get(url=URL)
    try:
        os.mkdir('data')
    except OSError as ex:
        print(ex)

    open('data/dataKt.zip', 'wb').write(r.content)

    zfile = zipfile.ZipFile('data/dataKt.zip')

    ##for finfo in zfile.infolist():
    ##    ifile = zfile.open(finfo)
    ##    line_list = ifile.readlines()
    ##    print(line_list)

    with zipfile.ZipFile('data/dataKt.zip', 'r') as f:
        names = f.namelist()

    df = pd.read_csv(zfile.open(names[0]), sep=';')
    zfile.close()
    shutil.rmtree('data')
    return df