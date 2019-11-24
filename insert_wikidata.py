# Quelle setzen
#  Q4115189|P1082|805|P585|+2017-12-31T00:00:00Z/9|P459|Q12483|S854|"https://data.stadt-zuerich.ch/dataset/bev_bestand_jahr_quartier_seit1970_od3240"
from wikidataintegrator import wdi_core, wdi_login
from wikidataintegrator.ref_handlers import update_retrieved_if_new_multiple_refs
import pandas as pd
import numpy as np
import requests
from datetime import datetime
from time import sleep
from random import random

from datetime import datetime
import copy

# TODO: login for wikidate to config
# TODO: preferred change to newest
def create_reference():
    timeStringNow = datetime.now().strftime("+%Y-%m-%dT00:00:00Z")
    # Timestamp P585
    refRetrieved = wdi_core.WDTime(timeStringNow, prop_nr="P813", is_reference=True)
    # URL Source P854
    refURL = wdi_core.WDUrl(value="https://data.stadt-zuerich.ch/dataset/bev_bestand_jahr_quartier_seit1970_od3240",
                            prop_nr="P854", is_reference=True)

    return [refRetrieved, refURL]

def create_qualifier(insertDate):
    # Point in time P585
    insertDate = insertDate.strftime("+%Y-%m-%dT00:00:00Z")
    refRetrieved = wdi_core.WDTime(insertDate, prop_nr="P585", is_qualifier=True)
    # Statistics P459
    bestimmungsmethode = wdi_core.WDItemID(value='Q12483', prop_nr='P459', is_qualifier=True)

    return [refRetrieved, bestimmungsmethode]

# TODO: improve structure of the function
def insert_wikidate(df):#
    df = df[df['bool'] == False]
    for i, row in df.iterrows():
        print("Insert data value: {0} - {1} - {2} : {3}".format(row['wikidata_id'], row['name'], row['date'],
                                                                row['population']))
        reference = create_reference()
        qualfier = create_qualifier(row['date'])
        statement = [
            wdi_core.WDQuantity(value=row['population'], prop_nr="P1082", references=[copy.deepcopy(reference)],
                                rank='normal', qualifiers=copy.deepcopy(qualfier), check_qualifier_equality=False)]
        wd_item = wdi_core.WDItemEngine(data=statement, wd_item_id=row['wikidata_id'], new_item=False, fast_run=False,
                                        append_value=['P1082'])
        wd_item.write(login)
        sleep(8 + random())