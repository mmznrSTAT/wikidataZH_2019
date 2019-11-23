import pandas as pd
import logging
import numpy as np
from data_imports import *


def compare_dfs_kt(df_wikidata, df_statdata):
    """
    This functions checks all entries from ZH Kanton Data and compares it with the wikidata
    :param df_wikidata:
    :param df_statdata:
    :return: list of index in df_statdata not in df_wikidata --> need to be uploaded to wikidata
    """
    logging.info('Compare: {0} stat_entries with {1} wikidate_entries'.format(df_statdata['date'].count,
                                                                              df_wikidata['date'].count))

    # Create the check column
    df_statdata['check'] = df_statdata['date'].astype(str) + '---' + df_statdata['BFS_NR'].astype(str)
    df_wikidata['check'] = df_wikidata['date'].astype(str) + '---' + df_wikidata['bfs_id'].astype(str)
    print("NOT IN THE DATASET")
    print(df_statdata[(df_statdata['check'].isin(df_wikidata['check']) == False)]['date'].astype(str).str[:4].unique())

    return df_statdata[(df_statdata['check'].isin(df_wikidata['check']) == False)].index.tolist()


def compare_dfs_gm(df_wikidata, df_statdata):

    logging.info('Compare: {0} stat_entries with {1} wikidate_entries'.format(df_statdata['date'].count,
                                                                              df_wikidata['date'].count))

    # Create the check column
    df_statdata['check'] = df_statdata['date'].astype(str) + '---' + df_statdata['wikidata_id'].astype(str)
    df_wikidata['check'] = df_wikidata['date'].astype(str) + '---' + df_wikidata['wikidata_id'].astype(str)
    print("NOT IN THE DATASET")
    print(df_statdata[(df_statdata['check'].isin(df_wikidata['check']) == False)]['date'].astype(str).str[:4].unique())

    return df_statdata[(df_statdata['check'].isin(df_wikidata['check']) == False)].index.tolist()


def main():
    # Database request of city/kanton level
    cityZH = import_cityZH_api()
    kantonZH = import_kantonZH_api()

    # Network requests
    geoadmin = import_geoadmin_wikidata_kt()
    wikidataKT = import_wikidata_kt()
    wikidataQT = import_wikidata_qt()
    # wikidata_id
    print("MERGER")
    merger = pd.merge(kantonZH, geoadmin, how='left', left_on=['BFS_NR'], right_on=['bfs']).dropna()
    print(merger.head())
    # 2. Wiki mit API Kanton
    print(compare_dfs_kt(wikidataKT, merger))

    # 2. Wiki
    print(compare_dfs_gm(wikidataQT, cityZH))

if __name__ == "__main__":
    main()
