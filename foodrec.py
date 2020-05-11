# -*- coding: utf-8 -*-
"""
Created on Thu May  7 12:03:11 2020

@author: ISHIKA
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib.request as urllib2
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction import FeatureHasher
fh=FeatureHasher(n_features=9208,input_type='string')
cv=CountVectorizer()
def get_index(title):
    return data[data["title"]==title]["index"].values
def get_title(index):
    return data[data["index"]==index]["title"].values
    



data=pd.read_csv(r"https://raw.githubusercontent.com/syedayazsa/data/master/food_items.csv")

#data=html.decode('utf-8')

data.drop(['Unnamed: 6', 'Unnamed: 7','manufacturer', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10','Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14','Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18','Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22','Unnamed: 23', 'Unnamed: 24', 'Unnamed: 25', 'Unnamed: 26','Unnamed: 27', 'Unnamed: 28', 'Unnamed: 29'],axis=1,inplace=True)
data.set_index(data['index'],inplace=True,drop=True)
#data.drop(['index'],axis=1,inplace=True)

data=data.astype(str)
featurs=["ingredients","brand"]
def combine_features(row):
    try:
        return row["ingredients"]+" "+row["brand"]
    except:
        print("Error: ",row)
data["final"]=data.apply(combine_features,axis=1)
cm=cv.fit_transform(data["final"])
cosine=cosine_similarity(cm)
fv=input("Enter the food you like: ")
oi=get_index(fv)

foods=list(enumerate(cosine[int(oi[0])]))
sort_list=sorted(foods,key=lambda x:x[1],reverse=True)
i=0
for element in sort_list:
    print(get_title(str(element[0])))
    i=i+1
    if(i>20):
        break