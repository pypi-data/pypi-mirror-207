'''
Deduplicates HSDS3 formatted addresses using exact matching on name, address_1, address_2, city, state_province, and postal_code
'''

import pandas as pd
import numpy as np
import pandas_dedupe

from silobuster.libs.uuid import random_uuid

from silobuster.libs.workers.helpers import split_addresses, add_unique_key


addr2_types = [
    'rm',
    'bldg',
    'apt',
    'unit'
]

import pandas as pd
from uuid import uuid4

def deduplicate_exact_match_address_3(df: pd.DataFrame):
    if 'cluster_id' in df.columns:
        df.drop(columns=['cluster_id'], inplace=True)
    # Create a key column in df and drop any duplicates
    df['key'] = (df['name'].str.lower().replace(' ', '') +
                df['address_1'].str.lower().replace(' ', '') +
                df['address_2'].str.lower().replace(' ', '') +
                df['city'].str.lower().replace(' ', '') +
                df['state_province'].str.lower().replace(' ', '') +
                df['postal_code'].str.lower().replace(' ', ''))
    df.drop_duplicates(subset='key', inplace=True)
    df.reset_index(drop=True, inplace=True)

    # Create empty dataframes to hold unique, duplicate, and cluster data
    uniques = pd.DataFrame(columns=[*df.columns])
    duplicates = pd.DataFrame(columns=[*df.columns])
    clusters = pd.DataFrame(columns=[*df.columns, 'cluster_id'])

    # Iterate over each row in the original dataframe
    for _, row in df.iterrows():
        # Check if there is a row with the same key in the uniques dataframe
        unique_row = uniques.loc[(uniques['key'] == row['key'])]

        if not unique_row.empty:
            # If there is, add the current row to the duplicates dataframe and give it the same cluster_id
            row['cluster_id'] = unique_row.iloc[0]['cluster_id']
            duplicates.loc[len(duplicates.index)] = row
        else:
            # If there isn't, assign a new cluster_id and add the row to the uniques dataframe
            row['cluster_id'] = random_uuid()
            uniques.loc[len(uniques.index)] = row

    # Add the duplicates to the clusters dataframe
    clusters = duplicates.copy()
    clusters.drop_duplicates(subset='cluster_id', inplace=True)

    # Combine the uniques and duplicates dataframes and drop the key column
    df_results = pd.concat([uniques, duplicates], ignore_index=True)
    df_results.drop(columns=['key'], inplace=True)

    # Print out some summary statistics and return the dataframes
    print(f'Original: {len(df)}')
    print(f'Clusters: {len(clusters)}')
    print(f'Uniques: {len(uniques)}')
    print(f'Duplicates: {len(duplicates)}')
    print(f'Results: {len(df_results)}')

    return {
        'results': df_results,
        'uniques': uniques,
        'clusters': clusters,
        'duplicates': duplicates,
        'original': df
    }


def deduplicate_exact_match_address(df: pd.DataFrame):
    original = df.copy()

    df['address_1'] = df['address_1'].fillna('')
    df['address_2'] = df['address_2'].fillna('')
    df['city'] = df['city'].fillna('')
    df['state_province'] = df['state_province'].fillna('')
    df['postal_code'] = df['postal_code'].fillna('')

    df['key'] = df.apply(lambda row: str(row['name']).lower().replace(' ', '') + 
                        str(row['address_1']).lower().replace(' ', '') + 
                        str(row['address_2']).lower().replace(' ', '') + 
                        str(row['city']).lower().replace(' ', '') + 
                        str(row['state_province']).lower().replace(' ', '') + 
                        str(row['address_2']).lower()[:5], axis = 1)

    

    # create a new column for the cluster ID
    df['cluster_id'] = None

    # create a boolean mask for duplicates
    duplicates_mask = df.duplicated(subset=['key'], keep=False)
    
    # create a boolean mask for uniques
    uniques_mask = ~duplicates_mask

    
    # create a new dataframe for duplicates
    duplicates = df[duplicates_mask].copy()
    duplicates['cluster_group'] = duplicates.groupby('key')['key'].transform(lambda x: random_uuid())
    duplicates['cluster_id'] = duplicates['cluster_group']
    duplicates.drop(columns=['cluster_group'], inplace=True)

    # duplicates = df[duplicates_mask].reset_index(drop=True).copy()
    # duplicates['cluster_id'] = duplicates.groupby('key').transform(lambda x: random_uuid())
    # duplicates['cluster_id'] = duplicates.groupby('key').transform(lambda x: random_uuid()).reset_index(drop=True)


    # create a new dataframe for uniques
    uniques = df[uniques_mask].copy()

    # update the cluster ID for duplicates
    df.update(duplicates)

    # drop the key column from all dataframes
    df.drop(columns=['key'], inplace=True)
    duplicates.drop(columns=['key'], inplace=True)
    uniques.drop(columns=['key'], inplace=True)

    # create a new dataframe for clusters
    clusters = duplicates[['cluster_id']].drop_duplicates().copy()
    clusters = clusters.merge(duplicates, on='cluster_id', how='left')

    # reset the index of all dataframes
    df.reset_index(drop=True, inplace=True)
    duplicates.reset_index(drop=True, inplace=True)
    uniques.reset_index(drop=True, inplace=True)
    clusters.reset_index(drop=True, inplace=True)

    # return the results
    return {
        'results': df,
        'uniques': uniques,
        'clusters': clusters,
        'duplicates': duplicates,
        'original': original
    }


def deduplicate_exact_match_address_4(df: pd.DataFrame):
    original = df.copy()
    # create a key column in df
    df['key'] = (df['name'].str.lower().replace(' ', '') +
                df['address_1'].str.lower().replace(' ', '') +
                df['address_2'].str.lower().replace(' ', '') +
                df['city'].str.lower().replace(' ', '') +
                df['state_province'].str.lower().replace(' ', '') +
                df['postal_code'].str.lower().replace(' ', ''))

    # create a boolean mask for duplicates
    duplicates_mask = df.duplicated(subset=['key'], keep=False)

    # create a boolean mask for uniques
    uniques_mask = ~duplicates_mask

    # create a new column for the cluster ID
    df['cluster_id'] = None

    # create a new dataframe for duplicates
    # duplicates = df[duplicates_mask].copy()
    duplicates = df[duplicates_mask][[*df.columns, 'cluster_id']].copy()


    # create a new dataframe for uniques
    uniques = df[uniques_mask].copy()


    # generate UUIDs for each cluster
    # create empty dictionary to store key-cluster ID mapping
    key_cluster_mapping = {}

    # iterate over duplicates
    for index, row in duplicates.iterrows():
        key = row['key']
        if key in key_cluster_mapping:
            # if key already in mapping, use existing cluster ID
            cluster_id = key_cluster_mapping[key]
        else:
            # if key not in mapping, generate new cluster ID
            cluster_id = random_uuid()
            key_cluster_mapping[key] = cluster_id
        # assign cluster ID to row
        row['cluster_id'] = cluster_id

    # update the cluster ID for duplicates
    # df.loc[duplicates_mask, 'cluster_id'] = cluster_ids
    df.loc[duplicates_mask, 'cluster_id'] = duplicates['cluster_id']


    # drop the key column from all dataframes
    df.drop(columns=['key'], inplace=True)
    duplicates.drop(columns=['key'], inplace=True)
    uniques.drop(columns=['key'], inplace=True)

    # create a new dataframe for clusters
    clusters = duplicates[['cluster_id']].drop_duplicates().copy()
    clusters = clusters.merge(duplicates, on='cluster_id', how='left')

    # reset the index of all dataframes
    df.reset_index(drop=True, inplace=True)
    duplicates.reset_index(drop=True, inplace=True)
    uniques.reset_index(drop=True, inplace=True)
    clusters.reset_index(drop=True, inplace=True)

    # return the results
    return {
        'results': df,
        'uniques': uniques,
        'clusters': clusters,
        'duplicates': duplicates,
        'original': original
    }



def deduplicate_exact_match_address_original(df: pd.DataFrame):
    df.reset_index(drop=True, inplace=True)

    # set unique key as index if it exists and drop existing index
    df = add_unique_key(df, set_as_index=True, drop_existing=True)

    # create new column for cluster ID
    df['cluster_id'] = pd.Series(dtype='object')

    # if organization_id column doesn't exist, add it
    if 'organization_id' not in df.columns:
        df = add_unique_key(df, 'organization_id')

    df.fillna("", inplace=True)

    # create a key column in df
    df['key'] = (df['name'].str.lower().replace(' ', '') +
                df['address_1'].str.lower().replace(' ', '') +
                df['address_2'].str.lower().replace(' ', '') +
                df['city'].str.lower().replace(' ', '') +
                df['state_province'].str.lower().replace(' ', '') +
                df['address_2'].str.lower().str[:5])

    # create a key column in uniques
    uniques = df.copy()
    uniques['key'] = (uniques['name'].str.lower().replace(' ', '') +
                    uniques['address_1'].str.lower().replace(' ', '') +
                    uniques['address_2'].str.lower().replace(' ', '') +
                    uniques['city'].str.lower().replace(' ', '') +
                    uniques['state_province'].str.lower().replace(' ', '') +
                    uniques['address_2'].str.lower().str[:5])

    # merge df with uniques on key
    merged = pd.merge(df, uniques, on='key', how='left', suffixes=('', '_y'))

    # create a boolean mask for duplicates
    duplicates_mask = merged['cluster_id_y'].notnull()
    duplicates = merged[duplicates_mask].copy()

    # update cluster dataframe
    clusters = pd.concat([uniques, duplicates], sort=False)
    clusters.drop_duplicates(subset=['key', 'cluster_id'], inplace=True)

    # update uniques dataframe
    uniques = merged[~duplicates_mask].copy()
    uniques.drop_duplicates(subset=['key', 'cluster_id'], inplace=True)

    # assign new cluster_id for uniques
    uniques.loc[uniques['cluster_id'].isnull(), 'cluster_id'] = [random_uuid() for _ in range(len(uniques[uniques['cluster_id'].isnull()]))]

    # drop key column from dataframes
    df = df.drop(columns=['key'])
    uniques = uniques.drop(columns=['key'])
    duplicates = duplicates.drop(columns=['key'])

    # combine uniques and duplicates into final results dataframe
    df_results = pd.concat([uniques, duplicates], ignore_index=True)

    print(f'Original: {len(df)}')
    print(f'Clusters: {len(clusters)}')
    print(f'Uniques: {len(uniques)}')
    print(f'Duplicates: {len(duplicates)}')
    print(f'Results: {len(df_results)}')

    return {
        'results': df_results,
        'uniques': uniques,
        'clusters': clusters,
        'duplicates': duplicates,
        'original': df
    }


# def deduplicate_exact_match_address(df: pd.DataFrame):
#     df.reset_index(drop=True)

#     df = add_unique_key(df,set_as_index=True, drop_existing=True)
    
#     if not 'organization_id' in df.columns:
#         df = add_unique_key(df, 'organization_id')


#     df.fillna("",inplace=True)
#     df['key'] = df.apply(lambda row: str(row['name']).lower().replace(' ', '') + str(row['address_1']).lower().replace(' ', '') + str(row['address_2']).lower().replace(' ', '') + str(row['city']).lower().replace(' ', '') + str(row['state_province']).lower().replace(' ', '') + str(row['address_2']).lower()[:5], axis = 1)
#     duplicates = pd.DataFrame(columns=[*df.columns, "original_organization_id", "original_name", "original_address_1", "original_address_2", "original_city", "original_city", "original_state_province", "original_postal_code"])    
#     uniques = pd.DataFrame(columns=[*df.columns, 'cluster_id'])
#     clusters = pd.DataFrame(columns=[*df.columns, 'cluster_id'])

#     df_results = df.copy()
#     df_results['cluster_id'] = pd.Series(dtype='object')

#     count = 0
#     for index, row in df.iterrows():
#         count += 1

#         if count % 200:
#             break
#             print (f'iteration: {count}')


#         unique_flag = True

#         unique_row = uniques.loc[(uniques['key'] == str(row['name']).lower().replace(' ', '') + str(row['address_1']).lower().replace(' ', '') + str(row['address_2']).lower().replace(' ', '') + str(row['city']).lower().replace(' ', '') + str(row['state_province']).lower().replace(' ', '') + str(row['address_2']).lower()[:5])]
#         if not unique_row.empty:

#             # Set the results df
# #            df_results.loc[df_results['unique_key'] == unique_row.iloc[0]['unique_key'], 'cluster_id'] = unique_row.iloc[0]['cluster_id']
# #            df_results.loc[df_results['unique_key'] == row['unique_key'], 'cluster_id'] = unique_row.iloc[0]['cluster_id']
            

#             row['cluster_id'] = unique_row.iloc[0]['cluster_id']

#             row['original_organization_id'] = unique_row.iloc[0]['organization_id']
#             row['original_name'] = unique_row.iloc[0]['name']
#             row['original_address_1'] = unique_row.iloc[0]['address_1']
#             row['original_address_2'] = unique_row.iloc[0]['address_2']
#             row['original_city'] = unique_row.iloc[0]['city']
#             row['state_province'] = unique_row.iloc[0]['state_province']
#             row['postal_code'] = unique_row.iloc[0]['postal_code']
#             duplicates.loc[len(duplicates.index)] = row

            
#             if unique_row.iloc[0]['cluster_id'].values[0] in uniques['cluster_id'].values.tolist():
#                 clusters.loc[len(clusters.index)] = unique_row.iloc[0]
#             clusters.loc[len(clusters.index)] = row


#             unique_flag = False


#         if unique_flag:
#             row['cluster_id'] = random_uuid()
#             uniques.loc[len(uniques.index)] = row

    
    
    
#     uniques.drop(columns=['key',], inplace=True)
#     uniques.fillna("",inplace=True)
#     duplicates.fillna('', inplace=True)
    
    
#     # uniques = add_unique_key(uniques, set_as_index=True)
#     # clusters = add_unique_key(clusters, set_as_index=True)
#     # duplicates = add_unique_key(duplicates, set_as_index=True)
    
#     # uniques.reset_index(drop=True, inplace=True)
#     # duplicates.reset_index(drop=True, inplace=True)
#     print (uniques.columns)
#     print (duplicates.columns)
#     print (uniques.index)
#     print (duplicates.index)
#     df_results = pd.concat([uniques, duplicates], ignore_index=True)
#     # df_results = pd.concat([uniques, duplicates])
    
#     print (f'Original: {len(df)}')
#     print (f'Clusters: {len(clusters)}')
#     print (f'Uniques: {len(uniques)}')
#     print (f'Duplicates: {len(duplicates)}')
#     print (f'Results: {len(df_results)}')

    
    
#     # df_results.set_index('unique_key', inplace=True)
#     # df_results.reindex(df_results.index.union(clusters.set_index('unique_key').index))
#     # df_results.update(clusters.set_index('unique_key')[clusters.columns])
#     # df_results.update(clusters[clusters.columns])

#     return {
#         'results': df_results,
#         'uniques': uniques,
#         'clusters': clusters,
#         'duplicates': duplicates,
#         'original': df
#     }



            # if not uniques.loc[uniques['cluster_id'].isin([unique_row.iloc[0]['cluster_id']])].empty:
            #     clusters.loc[len(clusters.index)] = unique_row.iloc[0] # Add the original row to the cluster
            # clusters.loc[len(clusters.index)] = row # add the duplicate column to the cluster

            # if unique_row.shape[0] > 0 and unique_row.iloc[0]['cluster_id'] in uniques['cluster_id'].values:

            # if not unique_row.empty and unique_row.iloc[0]['cluster_id'] in uniques['cluster_id'].values:

            #     clusters.loc[len(clusters.index)] = unique_row.iloc[0] # Add the original row to the cluster
            # clusters.loc[len(clusters.index)] = row # add the duplicate column to the cluster


            # if not unique_row.empty and unique_row.iloc[0]['cluster_id'] in uniques['cluster_id'].tolist():
            #     clusters.loc[len(clusters.index)] = unique_row.iloc[0] # Add the original row to the cluster
            # clusters.loc[len(clusters.index)] = row # add the duplicate column to the cluster


            # print("unique_row shape:", unique_row.shape)
            # print("uniques['cluster_id'].values shape:", uniques['cluster_id'].values.shape)

            # if not unique_row.empty and unique_row.iloc[0]['cluster_id'] in uniques['cluster_id'].values:
            #     clusters.loc[len(clusters.index)] = unique_row.iloc[0] # Add the original row to the cluster
            # clusters.loc[len(clusters.index)] = row # add the duplicate column to the cluster


            # if not unique_row.empty and unique_row.iloc[0]['cluster_id'] in uniques['cluster_id'].values.tolist():
            #     clusters.loc[len(clusters.index)] = unique_row.iloc[0] # Add the original row to the cluster
            # clusters.loc[len(clusters.index)] = row # add the duplicate column to the cluster
