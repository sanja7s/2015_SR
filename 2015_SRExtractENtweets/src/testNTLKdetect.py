'''
Created on Feb 20, 2015

@author: root
'''
import nltk
from nltk.corpus import stopwords


# for testing iterations only on the sart lines of the input file
TESTN = 50
# input file from B.G.
file_in = "/home/sscepano/Project7s/Twitter/BrunoDATA/mentions_reciprocal_six_months.dat"
f = open(file_in, 'r')

# a feature of NLTK it seems, it has the EN vocabulary corpus 
english_vocab = set(w.lower() for w in nltk.corpus.words.words())


print len(english_vocab)

print nltk.corpus.words.words()

print len(stopwords.words())