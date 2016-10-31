# our actual code imports
from bravado.client import SwaggerClient
import pandas as pd
import numpy as np
import operator
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from pandas.util.testing import assert_frame_equal

from collections import Counter


# The spec that will be used to generate the methods of the API client.
OPENTRIALS_API_SPEC = 'http://api.opentrials.net/v1/swagger.yaml'

# we want our data returned as an array of dicts, and not as class instances.
config = {'use_models': False}

# instantiate our API client
client = SwaggerClient.from_url(OPENTRIALS_API_SPEC, config=config)

## inspect the client properties
#print dir(client)
#
#result = client.trials.searchTrials(q='depression', per_page=10).result()

dfAll = pd.DataFrame()

for year in range(2000,2017):
    df = pd.DataFrame()
    d = []

    print year
    for i in range(1,10):
        try:
            result = client.trials.searchTrials(q='(registration_date:[{}-01-01 TO {}-12-31])'.format(year,year), per_page=10, page=i).result()
            for i in result['items']:
                d.append({'sample size': i['target_sample_size']})

        except:
            pass

    df[str(year)] = pd.DataFrame(d)
    #df['year'] = year
    df = df.dropna()

    dfAll = pd.concat([df,dfAll],axis=1)

print dfAll.mean()
dfAll.to_csv('sampleSize2.csv', encoding='utf-8')
