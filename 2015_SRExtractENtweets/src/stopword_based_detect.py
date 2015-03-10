'''
Created on Feb 21, 2015

@author: sscepano
'''
import nltk

# for testing iterations only on the start lines of the input file
TESTN = 200000000
# input file from B.G.
file_in = "/home/sscepano/Project7s/Twitter/BrunoDATA/mentions_reciprocal_six_months.dat"
f = open(file_in, 'r')
# output in EN tweets only
file_out = "/home/sscepano/Project7s/Twitter/BrunoDATA/EN_stopwords.dat"
f_out = open(file_out, 'w')

i = 0
k = 0
for line_orig in f:
    i+=1
#     print i
    # Bruno gave us the file split only by spaces, including how the words in tweets are delimited
    # thus we need to extract the tweets' text in a bit tricky, but ok way, taking everything after the first 4 terms
    line = line_orig.split()
    # sometimes the text is empty, and either a new tweet appear in the same line (I treat it with this code here as such)
    # or then we have to figure out can a user reply with a reply to another user ...
    try:
        while line[0] == line[5]:
            line = line[5:]
            i+=1
    except IndexError as e:
        print e, i
    text  = line[5:]

#     input_words = nltk.wordpunct_tokenize(text)
    language_likelihood = {}
    for language in nltk.corpus.stopwords._fileids:
        language_likelihood[language] = len(set(text) & set(nltk.corpus.stopwords.words(language)))
    
    detected_lang =sorted(language_likelihood, key=language_likelihood.get, reverse=True)[0]                            
 
    if detected_lang == "english":
        f_out.write(line_orig)
        k += 1

            
    if i >= TESTN:
        print "STOPWORDS based detect: exited due to the limit in test lines", TESTN
        break
 
print "STOPWORDS based detect"    
print "ENglish tweets found: ", k, " Percent: ", k/float(i)*100
print "Total tweets processed: ", i
