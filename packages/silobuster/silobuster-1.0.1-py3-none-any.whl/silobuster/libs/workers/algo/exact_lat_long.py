'''
Deduplicates HSDS3 formatted latitude and longitude using exact matches.
'''

from silobuster.libs.uuid import random_uuid
import pandas as pd


def exact_lat_long(df: pd.DataFrame):

    df.fillna("", inplace=True)
    df['key'] = df.apply(lambda row: str(row['name']).replace(' ', '').lower().strip() + str(row['latitude']) + str(row['longitude']), axis = 1)
    duplicates = pd.DataFrame(columns=[*df.columns, "original_id", "original_name", "original_latitude", "original_longitude"])
    uniques = pd.DataFrame(columns=[*df.columns, 'cluster_id'])
    clusters = pd.DataFrame(columns=[*df.columns, 'cluster_id'])

    for index, row in df.iterrows():
        # if row["latitude"] == "" or row["longitude"] == "" or row["address_1"] == "" or row["address_2"] == "":
        if row["latitude"] == "" or row["longitude"] == "":
            cluster_id = random_uuid()
            row['cluster_id'] = cluster_id
            uniques.loc[len(uniques.index)] = row
            continue
            
        unique_flag = True
        
        unique_row = uniques.loc[(uniques['key'] == str(row['name']).replace(' ', '').lower().strip() + str(row['latitude']) + str(row['longitude']))]
        if not unique_row.empty:

            row['cluster_id'] = unique_row.iloc[0]['cluster_id']

            row['original_id'] = unique_row.iloc[0]['id']
            row['original_name'] = unique_row.iloc[0]['name']
            row['original_latitude'] = unique_row.iloc[0]['latitude']
            row['original_longitude'] = unique_row.iloc[0]['longitude']
            duplicates.loc[len(duplicates.index)] = row
            
            if not uniques.loc[(uniques['cluster_id']) == unique_row.iloc[0]['cluster_id']].empty:
                clusters.loc[len(clusters.index)] = unique_row.iloc[0] # Add the original column to the cluster
            clusters.loc[len(clusters.index)] = row # add the duplicate column to the cluster
            
            unique_flag = False
    
        if unique_flag:
            row['cluster_id'] = random_uuid()
            uniques.loc[len(uniques.index)] = row
    
    uniques.drop(columns=['key',], inplace=True)
    duplicates.drop(columns=['key',], inplace=True)
    df.drop(columns=['key',], inplace=True)
    
    return {
        'results': uniques,
        'clusters': clusters,
        'duplicates': duplicates,
        'original': df
    }

