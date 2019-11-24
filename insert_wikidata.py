# Quelle setzen
#  Q4115189|P1082|805|P585|+2017-12-31T00:00:00Z/9|P459|Q12483|S854|"https://data.stadt-zuerich.ch/dataset/bev_bestand_jahr_quartier_seit1970_od3240"
from datetime import datetime
import copy
def create_reference():
    timeStringNow = datetime.now().strftime("+%Y-%m-%dT00:00:00Z")
    # Timestamp P585
    refRetrieved = wdi_core.WDTime(timeStringNow, prop_nr="P813", is_reference=True)
    # URL Source P854
    refURL = wdi_core.WDUrl(value="https://data.stadt-zuerich.ch/dataset/bev_bestand_jahr_quartier_seit1970_od3240",
                            prop_nr="P854", is_reference=True)

    return [refRetrieved, refURL]

def create_qualifier():
    insertDate = datetime.now().strftime("+%Y-%m-%dT00:00:00Z")
    # Point in time P585
    refRetrieved = wdi_core.WDTime(insertDate, prop_nr="P585", is_qualifier=True)
    # Statistics P459
    bestimmungsmethode = wdi_core.WDItemID(value='Q12483', prop_nr='P459', is_qualifier=True)

    return [refRetrieved, bestimmungsmethode]


def insert_wikidate():#
    reference = create_reference()
    qualfier = create_qualifier()
    statement = [
        wdi_core.WDQuantity(value=1001, prop_nr="P1082", references=[copy.deepcopy(reference)], rank='preferred',
                            qualifiers=copy.deepcopy(qualfier), check_qualifier_equality=False)]
    wd_item = wdi_core.WDItemEngine(data=statement, wd_item_id='Q4115189', new_item=False, fast_run=False)
    wd_item.write(login)