'''
Deduplicates HSDS3 formatted organization identifiers using exact match on the identifiers
'''


import pandas as pd
from silobuster.libs.uuid import random_uuid


def exact_identifier(df: pd.DataFrame):
    
    df.fillna("",inplace=True)
    duplicates = pd.DataFrame(columns=[*df.columns, "original_organization_id", "original_source_organization_id", "original_name", "original_identifier"])
    uniques = pd.DataFrame(columns=[*df.columns, "cluster_id"])
    clusters = pd.DataFrame(columns=[*df.columns, "cluster_id"])
    
    for index, row in df.iterrows():
        if row["identifier"] == "": # Skip blank identifiers
            cluster_id = random_uuid()
            row['cluster_id'] = cluster_id
            uniques.loc[len(uniques.index)] = row
            continue
            
        
        unique_flag = True
        unique_row = uniques.loc[(uniques['identifier']) == row['identifier']]
        
        if not unique_row.empty:
            
            # Add the new unique row
            row['cluster_id'] = unique_row.iloc[0]['cluster_id']
            
            row['original_organization_id'] = unique_row.iloc[0]['organization_id']
            row['original_source_organization_id'] = unique_row.iloc[0]['source_organization_id']
            row['original_name'] = unique_row.iloc[0]['name']
            row['original_identifier'] = unique_row.iloc[0]['identifier']
            duplicates.loc[len(duplicates.index)] = row
            
            
            if not uniques.loc[(uniques['cluster_id']) == unique_row.iloc[0]['cluster_id']].empty:
                clusters.loc[len(clusters.index)] = unique_row.iloc[0] # Add the original column to the cluster
            clusters.loc[len(clusters.index)] = row # add the duplicate column to the cluster

            unique_flag = False        

        if unique_flag:
            row['cluster_id'] = random_uuid()
            uniques.loc[len(uniques.index)] = row
            
    
    uniques.fillna("",inplace=True)
    duplicates.fillna("",inplace=True)
    clusters.fillna("", inplace=True)

    return {
        'results': uniques,
        'clusters': clusters,
        'duplicates': duplicates,
        'original': df
    }

