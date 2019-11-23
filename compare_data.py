import pandas as pd
import logging


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


    logging.info('Compare: {0} stat_entries with {1} wikidate_entries'.format(df_statdata['date'].count,
                                                                              df_wikidata['date'].count))
    return df_kanton[df_statdata['date'].isin(df_wikidata['date']) == True].index.tolist()