import requests
import pandas as pd


_population_resource_id = "570f006e-2f2a-4b1f-9233-c4916c753475"
_mapping_resource_id = "0090f2ed-1df9-4953-9561-5d413fd74758"


def _query_opendata_zurich(resource_id, parse_record):
    result = requests.get(
        f"https://data.stadt-zuerich.ch/api/3/action/datastore_search?resource_id={resource_id}"
    )
    records = result.json()["result"]["records"]
    parsed_rows = []
    for record in records:
        parsed_rows.append(parse_record(record))
    return parsed_rows


def _parse_population(record):
    return {
        "id": record["QuarSort"],
        "name": record["QuarLang"],
        "date": f"{record['StichtagDatJahr']}-12-31",
        "population": record["AnzBestWir"],
    }


def _parse_mapping(record):
    return {"id": record["QNr"], "wikidata_id": record["DataItemNr"]}


def _apply_wikidata_mapping(mapping_rows, population_rows):
    mapping_dict = {row["id"]: row["wikidata_id"] for row in mapping_rows}
    result = []
    for population_row in population_rows:
        population_row["wikidata_id"] = mapping_dict[population_row["id"]]


def city_of_zurich():
    population_rows = _query_opendata_zurich(_population_resource_id, _parse_population)
    mapping_rows = _query_opendata_zurich(_mapping_resource_id, _parse_mapping)
    _apply_wikidata_mapping(mapping_rows, population_rows)
    return pd.DataFrame(population_rows)


def main():
    data_frame = city_of_zurich()
    print(data_frame)


if __name__ == "__main__":
    main()
