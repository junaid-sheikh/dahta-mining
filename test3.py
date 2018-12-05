import numpy
import scipy.optimize
import random

def parseJSON(fname):
    for l in open(fname):
        yield eval(l)

data = list(parseJSON("/mnt/c/repositories/Recommender-Systems/labelled-data/beer_50000.json"))

young = [d for d in data if 'user/ageInSeconds' in d and d['user/ageInSeconds'] < 60*60*365*80*24]

features = [[1, d['user/ageInSeconds']] for d in young]
results = [d['review/overall'] for d  in young]

print(results[:10])