def compare_dfs(df_wikidata, df_statdata):
    '''
    :param df_wikidata:
    :param df_statdata:
    :return: list of index in df_statdata not in df_wikidata
    '''
    return df_statdata[df_statdata['date'].isin(df_wikidata['date']) == True].index.tolist()
