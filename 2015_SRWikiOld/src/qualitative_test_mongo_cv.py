'''
Created on Mar 10, 2015

@author: sscepano
'''
'''
Here we implement a simple connection to mongodb where we take concept vectors for given two words and compare them
then we calculate the similarity
This one will serve for my qualitative testing
'''
import pymongo
import json
from pymongo import MongoClient
from pprint import pprint
from collections import defaultdict
import math

'''
example output from the mongo db, for reference

> db.concept_vectors.findOne({"_id":"tralala"})
{
    "_id" : "tralala",
    "cv" : [
        {
            "article" : "Agnes_Monica",
            "value" : 23.28595352172852,
            "aid" : 466218
        },
        {
            "article" : "Bermuda_at_the_2008_Summer_Olympics",
            "value" : 19.01290130615234,
            "aid" : 1251443
        },
        {
            "article" : "Boston_Society_of_Film_Critics_Award_for_Best_Supporting_Actress",
            "value" : 13.44415187835693,
            "aid" : 1427980
        }
    ]
}
'''

# connect to mongo right instance and db, par attention to port
client = MongoClient('localhost', 27017)
db = client.wiki_db_v1

reads = db.concept_vectors

# words which we want to test
word1 = "hate"
word2 = "love"

# the function to call the Mongo vector values and calculate SR
def find_words_SR(word1, word2):
    
    CV1 = reads.find({"_id":word1})
    CV2 = reads.find({"_id":word2})
    # lets save cvs in this dictionaries
    concepts1 = defaultdict(int)
    concepts2 = defaultdict(int)
    # extract first word cv to dict
    N1 = 0
    # NB here that we need to access CV1[0] from the cursor for out data
    for el in CV1[0]["cv"]:
        N1 += 1
        concepts1[el["aid"]] = el["value"]
    print N1
    #print concepts1
    # extract second word cv to dict
    N2 = 0
    # NB here that we need to access CV2[0] from the cursor for out data
    for el in CV2[0]["cv"]:
        N2 += 1
        concepts2[el["aid"]] = el["value"]
    print N2
    #print concepts2
    
    commonCV = defaultdict(int)
    SRdist = 0
    SQRsumv1 = 0
    SQRsumv2 = 0
    N12 = 0
    
    for el1 in concepts1.keys():
        for el2 in concepts2.keys():
            if el1 == el2:
                N12 += 1
                v1, v2 = concepts1[el1], concepts2[el2] 
#                 print v1, v2
                commonCV[el1] = (v1, v2)
                SRdist += v1 * v2
                SQRsumv1 += v1*v1
                SQRsumv2 += v2*v2
    
    print "In common ", N12             
    if N12 > 0:    
        Ochiai = float(N12)/math.sqrt(N1*N2)
#         print "Common el ", N12, " Ochiai ", Ochiai
        #print commonCV 
        SQRTSQRsumv1 = math.sqrt(SQRsumv1)
        SQRTSQRsumv2 = math.sqrt(SQRsumv2)
        SRdist = SRdist / float(SQRTSQRsumv1*SQRTSQRsumv2)
#         print "Before Ochiai", SRdist
        SRdistOchiai = Ochiai * SRdist
        print "After Ochiai", SRdistOchiai
    else:
        SRdist = 0
#         print "No common concepts so SR distance = ", SRdist
        
    return SRdist
    
    
        
