import json
import numpy as np
import pandas as pd


import json
import numpy as np
import pandas as pd


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        # print ("##################################################")
        # print (obj)
        # print (type(obj))
        # print ("##################################################")
        
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, pd.Series):
            return obj.tolist()
        if isinstance(obj, bool):
            if obj: 
                return 1
            else: 
                return 0
        if isinstance(obj, np.bool_):
            if obj:
                return 1
            else:
                return 0
        

        return super(NpEncoder, self).default(obj)
