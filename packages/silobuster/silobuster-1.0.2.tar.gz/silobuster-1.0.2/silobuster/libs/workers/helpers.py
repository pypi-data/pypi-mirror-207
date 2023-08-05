import secrets
import hashlib
import pandas as pd
import numpy as np


from silobuster.libs.uuid import random_uuid



def split_addresses(addr1: str, addr2: str=""):
    addr1 = addr1.lower().strip()
    addr2 = addr2.lower().strip()

    # Extract unit if address line 2 is provided
    if addr2:
        unit = addr2
    else:
        unit = ""

    # Check if address line 1 contains a comma and use it to extract unit if present
    if "," in addr1:
        addr1_parts = addr1.split(",")
        if unit == "":
            unit = addr1_parts[-1].strip()
        addr1 = ",".join(addr1_parts[:-1]).strip()

    # Extract street number, name, and type from address line 1
    parts = addr1.split(" ")
    street_number = parts[0]
    street_name = " ".join(parts[1:-1])
    street_type = parts[-1].split(",")[0]  # Remove any commas from street type

    return street_number, street_name, street_type, unit



# Generate a random sequence of bytes
def random_hash():
    random_bytes = secrets.token_bytes(16)
    # Generate a hash value of the bytes
    return hashlib.md5(random_bytes).hexdigest()


def add_unique_key(df: pd.DataFrame, column_name: str='unique_key', set_as_index: bool=False, drop_existing=True):
    if drop_existing:
        if column_name in df.columns:
            df.drop(columns=[column_name], inplace=True)

    
    uuids = np.array([random_uuid() for _ in range(len(df))])
    #df.loc[:,column_name] = uuids
    #df[column_name] = uuids.tolist()
    df = pd.concat([df, pd.Series(uuids, name=column_name)], axis=1)


    if set_as_index:
        new_df = df.copy()
        new_df.reset_index(drop=True, inplace=True)
        new_df.set_index(column_name, inplace=True)
        return new_df
    
    return df



import uuid


import pandas as pd
import uuid


# def replace_cluster_id_with_uuid(df: pd.DataFrame, column: str, blank_duplicates: bool=True):
    
#     if not isinstance(df, pd.DataFrame):
#         raise ValueError("Expected a Pandas DataFrame")
    

#     uuid_dict = {}
    
#     def map_uuid(group):
#         x = group.iloc[0]
#         if x not in uuid_dict:
#             uuid_dict[x] = uuid.uuid4()
#         return group.map(lambda _: uuid_dict[x])
    
#     try:
#         # Group the dataframe by the specified column
#         grouped_df = df.groupby(column)
        
#         # Replace the column values in each group with UUIDs
#         df[column] = grouped_df[column].transform(map_uuid)
#     except KeyError:
#         pass
#     except:
#         raise


#     return df

def replace_cluster_id_with_uuid(df: pd.DataFrame, column: str, blank_duplicates: bool=True):
    
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Expected a Pandas DataFrame")
    
    uuid_dict = {}
    
    def map_uuid(group):
        x = group.iloc[0]
        if pd.isna(x) or x == '':
            return ''
        
        if blank_duplicates and len(group) == 1:
            return ''
        
        if x not in uuid_dict:
            uuid_dict[x] = uuid.uuid4()
        return group.map(lambda _: uuid_dict[x])

    
    try:
        # Group the dataframe by the specified column
        grouped_df = df.groupby(column)
        
        # Replace the column values in each group with UUIDs
        df[column] = grouped_df[column].transform(lambda x: map_uuid(x))
        
        # Check if cluster ID is unique, and set to blank string if not
        # if blank_duplicates:
        #     mask = grouped_df[column].transform(lambda x: len(x.unique()) == 1)
        #     df.loc[mask, column] = ""
        
    except KeyError:
        pass
    except:
        raise
        
    return df
