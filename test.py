import numpy
import scipy.optimize
import random

# strings
beer_reviews = \
"/mnt/c/repositories/Recommender-Systems/labelled-data/beer_50000.json"
age_key = 'user/ageInSeconds'
abv_key = 'beer/ABV'
rev_key = 'review/overall'

def parseJSON(fname):
    for l in open(fname):
        yield eval(l)

data = list(parseJSON(beer_reviews))
young = [d for d in data if age_key in d and d[age_key] < 60*60*365*80*24]

x = [[1, d[abv_key], d[abv_key]**2] for d in young]
y = [d[rev_key] for d  in young]

theta, residuals, rank, s = numpy.linalg.lstsq(x, y, rcond=-1)
print theta

