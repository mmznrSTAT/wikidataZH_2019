import pandas as pd
import logging
from data_imports import *


def compare_dfs(df_wikidata, df_statdata):
    """
    This functions checks all entries from ZH Data and compares it with the
    :param df_wikidata:
    :param df_statdata:
    :return: list of index in df_statdata not in df_wikidata
    """
    logging.info('Compare: {0} stat_entries with {1} wikidate_entries'.format(df_statdata['date'].count,
                                                                              df_wikidata['date'].count))
    return df_statdata[df_statdata['date'].isin(df_wikidata['date']) == True].index.tolist()


def compare_kanton_mapping(df_wikidata, df_kanton):

    logging.info('Compare: {0} stat_entries with {1} wikidate_entries'.format(df_kanton['date'].count,
                                                                              df_wikidata['date'].count))
    return df_kanton[df_kanton['date'].isin(df_wikidata['date']) == True].index.tolist()


def main():
    # Database request of city/kanton level
    cityZH = import_cityZH_api()
    print("City of Zurich")
    #cityZH['date'] = cityZH['date'].dt.date
    print(cityZH)

    kantonZH = import_kantonZH_api()
    print("Kanton data")
    print(kantonZH)
    #kantonZH['date'] = kantonZH['date'].dt.date
    # Network requests
    geoadmin = import_geoadmin_wikidata_kt()
    print("Kanton geo.admin.data")
    print(geoadmin)
    #geoadmin['date'] = geoadmin['date'].dt.date
    wikidataKT = import_wikidata_kt()
    print("Wikidata for Kanton")
    print(wikidataKT)
    #wikidataKT['date'] = wikidataKT['date'].dt.date

    # 1. Join Q_Numbers
    # wikidata_id
    print("MERGER")
    merger = pd.merge(kantonZH, geoadmin, how='left', left_on=['BFS_NR'], right_on=['bfs'])
    print(merger.head())
    # 2. Wiki mit API Kanton
    # 2. Wiki


if __name__ == "__main__":
    main()
