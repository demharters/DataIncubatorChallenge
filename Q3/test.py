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

d = []
df_counts = pd.DataFrame()

for year in range(2000,2017):

    print year
    for i in range(1,100):
        try:
            result = client.trials.searchTrials(q='(registration_date:[{}-01-01 TO {}-12-31])'.format(year,year), per_page=10, page=i).result()
            for i in result['items']:
                intervList = [k['name'] for k in i['interventions'] if 'name' in k]
                for j in i['conditions']:
                    d.append({'id': i['id'], 'name': j['name'], 'registration date': i['registration_date']})
                    #d.append({'id': i['id'], 'name': j['name'], 'registration date': i['registration_date'], 'interventions': intervList})

        except:
            pass

    df = pd.DataFrame(d)
    words = []
   
    #df_tmp = pd.DataFrame(df['name'].value_counts())
    #df_tmp = pd.DataFrame(df_tmp['name'].str.split())
    #df_tmp.columns = ['name', 'count']
    #df_counts = pd.concat([df_tmp, df_counts])
    #df_tmp['year'] = year
    for index, row in df.iterrows():
        #for word in row['name'].split():
        #for word in row['name']:
            #words.append(word)
        words.append(row['name'])

    #stopwords = ['and','of','with','in','at','-','on','to','it','the','or','due','not','de','2','a']
    querywords = [word.lower() for word in words]
    #resultwords  = [word for word in querywords if word.lower() not in stopwords]
    counts = Counter(querywords)
    sortedCounts = sorted(counts.items(), key=operator.itemgetter(1), reverse = True)
    df_tmp = pd.DataFrame(sortedCounts[:20])
    df_tmp.columns = ['name','counts']
    df_tmp['year'] = year
    df_counts = pd.concat([df_tmp, df_counts])
    
    #vectorizer = TfidfVectorizer(stop_words='english')
    #X = vectorizer.fit_transform(df['name'])
    ##true_k = 2
    #true_k = 8
    #model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
    #model.fit(X)
    #
    #print("Top terms per cluster:")
    #order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    #terms = vectorizer.get_feature_names()
    #for i in range(true_k):
    #    print "Cluster %d:" % i,
    #    for ind in order_centroids[i, :5]:
    #        print ' %s' % terms[ind]

df_counts.to_csv('conditionCounts4.csv', encoding='utf-8')
#with open('conditionCount.csv', 'w') as f:
#    f.write("year,name,counts\n")
#    for key, item in df_list:
#        f.write("%s,%s,%s\n") % (key, item[0], item[1])
