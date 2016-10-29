#!/usr/local/bin/python

import urllib
import pandas as pd
import zipfile
import os 
import glob
import numpy as np

allFiles = glob.glob(os.path.join(os.getcwd(), "*.csv"))

#for month in range(1,13):
    #myURL = "https://s3.amazonaws.com/tripdata/2015{num:02d}-citibike-tripdata.zip".format(num=month)
    #myFile = "{num:02d}-citibike_tripdata.zip".format(num=month)
    #urllib.urlretrieve(myURL, myFile)
    #zip_ref = zipfile.ZipFile(myFile, 'r')
    #zip_ref.extractall(".")
    #zip_ref.close()
    
allData = pd.concat(pd.read_csv(f) for f in allFiles)
allData = allData.reset_index(drop=True)
#meanDur = allData.tripduration.mean(axis=0)
#print meanDur
#
#sameStationData = allData[allData['start station name'] == allData['end station name']]
#differentStationData = allData[allData['start station name'] != allData['end station name']]
#propSameStation = (float(sameStationData.shape[0])/allData.shape[0])*100
#print propSameStation
#
#def haversine_np(lon1, lat1, lon2, lat2):
#    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
#
#    dlon = lon2 - lon1
#    dlat = lat2 - lat1
#
#    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2
#
#    c = 2 * np.arcsin(np.sqrt(a))
#    km = 6367 * c
#    return km
#
#distances = haversine_np(differentStationData["start station longitude"], differentStationData["start station latitude"], differentStationData["end station longitude"], differentStationData["end station latitude"])
#print distances.head(3)
#dist_time = pd.concat([distances, differentStationData['tripduration']/3600], axis=1)
#dist_time.columns = ['distance','hours']
#print dist_time.head(3)
#kmh = dist_time['distance']/dist_time['hours']
#dist_time_kmh = pd.concat([dist_time, kmh], axis=1)
#dist_time_kmh.columns = ['distance','hours','kmh']
#print dist_time_kmh.head(3)
#cleanData = dist_time_kmh[dist_time_kmh['kmh'] > 0.1]
#distMean = cleanData['distance'].mean(axis=0)
#print distMean

startStations = allData[['bikeid','start station id']]
endStations = allData[['bikeid','end station id']]
startStations.columns = ['bikeid','stationid']
endStations.columns = ['bikeid','stationid']
startandendStations = pd.concat([startStations,endStations],axis=0)
startandendStations_grouped = startandendStations.groupby('bikeid').stationid.nunique()
stations_std = startandendStations_grouped.std()
print stations_std
