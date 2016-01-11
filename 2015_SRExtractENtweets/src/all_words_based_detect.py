'''
Created on Feb 20, 2015

@author: root
'''
import nltk

# for testing iterations only on the start lines of the input file
TESTN = 200000000 
# input file from B.G.
file_in = "/home/sscepano/Project7s/Twitter/BrunoDATA/mentions_reciprocal_six_months.dat"
f = open(file_in, 'r')
# output in EN tweets only
file_out = "/home/sscepano/Project7s/Twitter/BrunoDATA/EN_all_words.dat"
f_out = open(file_out, 'w')

# a feature of NLTK it seems, it has EN vocabulary corpus 
english_vocab = set(w.lower() for w in nltk.corpus.words.words("en"))

i = 0
k = 0
for line in f:
    i+=1
    # Bruno gave us the file split only by spaces, including how the words in tweets are delimited
    # thus we need to extract the tweets' text in a bit tricky, but ok way, taking everything after the first 4 terms
    line = line.split()
    # sometimes the text is empty, and either a new tweet appear in the same line (I treat it with this code here as such)
    # or then we have to figure out can a user reply with a reply to another user ...
    try:
        while line[0] == line[5]:
            line = line[5:]
            i+=1
    except: IndexError
        
    text  = line[5:]
#    print line
#    print text
    text_vocab = set(w.lower() for w in text if w.lower().isalpha() and w <> 'RT')
    unusual = text_vocab.difference(english_vocab)    
#     print unusual
    # THE most stringest test I can make is -- if there is any word found not in EN, then we omit the tweet
    # this has obvious mistake that the strings like "bday" will be considered "unusual"
    
    if len(unusual) == 0:
        k += 1
        line_out = " ".join(line)
        f_out.write(line_out + '\n')
    
    if i >= TESTN:
        print "exited due to the limit in test lines", TESTN
        break
        
print "ENglish tweets found: ", k, " Percent: ", k/float(i)*100
print "Total tweets processed: ", i

    
    