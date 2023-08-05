'''
Deduplicates addresses using the dedupe.io (Pandas version) using name, address_1, address_2, city, state_province, and postal_code
'''
import pandas as pd
import pandas_dedupe
import numpy as np

from inspect import getsourcefile
from os.path import abspath
from silobuster.libs.uuid import random_uuid
import datetime

from silobuster.libs.workers.helpers import split_addresses, replace_cluster_id_with_uuid

# Make sure we are getting the absolute path to the training file!
path_arr = abspath(getsourcefile(lambda:0)).split('/')
path_arr.pop()
curpath = '/'.join(path_arr)


addr2_types = [
    'rm',
    'bldg',
    'apt',
    'unit'
]


def dedupe_io_name_street(df: pd.DataFrame, **kwargs):
    '''
    Requires:
    keyword arguments:
    
    Run dedupe.io and match addresses. Use that data to dedupe within itself and return an organization and an address dataframe that is formatted for a node.
    '''
    lower_threshold = .6
    upper_threshold = .999

    formatted_df = df.copy(deep=True)
    formatted_df[['numerical', 'street_name', 'street_type', 'unit']] = formatted_df.apply(lambda row: pd.Series(split_addresses(str(row["address_1"]), str(row["address_2"]))), axis=1)
    formatted_df['postal_code'].map(lambda x: str(x).replace('-', '').replace(' ', ''))

    # Drop na and then combine after clustering
    
    formatted_df[['street_name', 'postal_code', 'name']] = formatted_df[['street_name', 'postal_code', 'name']].replace('', np.nan)
    cleaned_df = formatted_df.dropna(subset=['street_name'])
    cleaned_df = cleaned_df.dropna(subset=['name'])
    
    deduper_df = pandas_dedupe.dedupe_dataframe(df=cleaned_df, field_properties=[
            ('name', 'String', 'has missing'), 
            ('street_name', 'String', 'has missing'), 
            ('postal_code','Exact', 'has missing'),
            
            #('l_description','Text','has missing')
        ],
        config_name=curpath + '/dedupe_io_name_street',
    )

    # Save the dropped rows
    dropped_rows = formatted_df[~formatted_df.index.isin(deduper_df.index)]
    
    # Remove the dropped rows from the formatted dataframe
    formatted_df = formatted_df.loc[deduper_df.index]
    
    deduper_df.columns = deduper_df.columns.str.replace(' ', '_')
    
    deduper_df = replace_cluster_id_with_uuid(deduper_df, 'cluster_id')
    deduper_df = replace_cluster_id_with_uuid(deduper_df, 'cluster id')

    if kwargs.get('return_frame_only'):
        # Append the dropped rows to the deduper_df and return
        return pd.concat([deduper_df, dropped_rows], axis=0, ignore_index=True)



    addr_results = pd.DataFrame(columns=['id', 'hsds', 'coordinates', 'aliases'])
    org_results = pd.DataFrame(columns=['id', 'hsds', 'locations', 'attributes', 'aliases'])
    deduper_df = deduper_df.sort_values(by=["organization_id",])
    processed = set()
    current_id = 0
    addr_row = list()

    
    addr_row = list()
    addr_id = random_uuid()
    addr_hsds = dict()
    addr_coordinates = list()
    addr_aliases = list()
    
    org_row = list()
    org_id = random_uuid()
    org_hsds = dict()
    org_locations = set()
    org_attributes = dict()
    org_aliases = list()

    # df.drop(columns='cluster_id', axis=1, inplace=True)
    for index, row in deduper_df.iterrows():    
        
        if row['confidence'] < lower_threshold or row['confidence'] > upper_threshold:
            continue


        

        if current_id != row.loc['cluster_id']: # create the new row
            #if index > 0: # skip the first row
            addr_row.append(addr_id)
            addr_row.append(addr_hsds)
            addr_row.append(addr_coordinates)
            addr_row.append(addr_aliases)
            addr_results.loc[len(addr_results)] = addr_row

            org_row.append(org_id)
            org_row.append(org_hsds)
            org_row.append(list(org_locations))
            org_row.append(org_attributes)
            org_row.append(org_aliases)
            org_results.loc[len(org_results)] = org_row

            # Reset the attributes    
            addr_row = list()
            addr_id = random_uuid()
            addr_hsds = dict()
            addr_coordinates = list()
            addr_aliases = list()

            org_row = list()
            org_id = random_uuid()
            org_hsds = dict()
            org_locations = set()
            org_attributes = dict()
            org_aliases = list()
            

        
        org_locations.add(addr_id)

        processed.add(row['address_id']) # Keeps track of processed rows.
        current_id = row.loc['cluster_id'] # Controls when the collection is reset... Cluster changes
        
        # Create the 
        #if isinstance(row['latitude'], float) and isinstance(row['longitude'], float):
        addr_coordinates.append({
            'latitude': row['latitude'],
            'longitude': row['longitude'],
            'source': row['source']
        })

        addr_aliases.append({
            # 'address_1': row['address_1'],
            # 'address_2': row['address_2'],
            # 'city': row['city'],
            # 'state_province': row['state_province'],
            # 'postal_code': row['postal_code'],
            # 'source': row['source'],
            **row,
            'created_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%s")
        })
        
        org_aliases.append({
            **row,
            'created_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%s")
        })
        


    # Iterate all of the rows from the original dataframe and add any that wasnt duplicated
    for index, row in df.iterrows():
        if row['address_id'] in processed:
            continue

        addr_id = random_uuid()
        addr_results.loc[len(addr_results)] = [
            addr_id,
            {},
            [{
                'latitude': row['latitude'],
                'longitude': row['longitude'],
                'source': row['source']
            }],
            [{
                # 'address_1': row['address_1'],
                # 'address_2': row['address_2'],
                # 'city': row['city'],
                # 'state_province': row['state_province'],
                # 'postal_code': row['postal_code'],
                # 'source': row['source'],
                'created_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%s"),
                **row,
            }],
        ]

        org_results.loc[len(org_results)] = [
            random_uuid(),
            {},
            [addr_id,],
            {},
            [{
                'created_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%s"),
                **row,
            }]

        ]


    cluster_index = dict()
    
    for index, row in deduper_df.iterrows():    
    
        if cluster_index.get(row['cluster_id']):
            deduper_df.loc[index, 'cluster_id'] = cluster_index[row['cluster_id']]
        else:
            my_id = random_uuid()
            cluster_index[row['cluster_id']] = my_id
            deduper_df.loc[index, 'cluster_id'] = my_id


    return {
        'address_results': addr_results,
        'org_results': org_results,
        'dedupe_io_results': deduper_df,
        'original': df
    }

