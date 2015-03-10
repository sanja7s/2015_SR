'''
Created on Mar 4, 2015

@author: sscepano
'''
'''
This code combines two approaches to detect if the tweet text is in ENglish.

1) At first we use stopwords-based approach: stopwords are recognized based on the NLTK corpus of stopwords from many languages.
Then likelihood of the languages is calculated based on the number of stopwords found matching that particular language.
The language from which the highest number of stopwords is found is selected as the tweet language.

2) If this approach did not result in EN tweet detected, we double-check with all words based approach.
NLTK has another corpus, where we check for all the words and if all the words of the tweet are in EN corpus,
then the tweet is classified as EN still. This can happen when the tweet does not have stopwords in order to be short.

If the tweet is found to be in EN in any approach, we output it.
'''
import nltk

# for testing iterations only on the start lines of the input file
TESTN = 2000000000
# input file from B.G.
file_in = "/home/sscepano/Project7s/Twitter/BrunoDATA/mentions_reciprocal_six_months.dat"
f = open(file_in, 'r')
# output in EN tweets only
file_out = "/home/sscepano/Project7s/Twitter/BrunoDATA/EN_COMB.dat"
f_out = open(file_out, 'w')

# a feature of NLTK, it has EN vocabulary corpus 
english_vocab = set(w.lower() for w in nltk.corpus.words.words("en"))

# total lines counter
i = 0
# detected English lines counter
k = 0
for line_orig in f:
    i+=1
    # Bruno gave us the file split only by spaces, including how the words in tweets are delimited
    # thus we need to extract the tweets' text in a bit tricky, but ok way, taking everything after the first 4 terms
    line = line_orig.split()
    # sometimes the text is empty, and either a new tweet appears in the same line (I treat it with this code here as such case)
    try:
        while line[0] == line[5]:
            line = line[5:]
            i+=1
    except IndexError as e:
        print e, i
    text  = line[5:]
#     text = " ".join(text_simple)
# 
#     input_words = nltk.wordpunct_tokenize(text)
    language_likelihood = {}
    for language in nltk.corpus.stopwords._fileids:
        language_likelihood[language] = len(set(text) & set(nltk.corpus.stopwords.words(language)))   
    detected_lang =sorted(language_likelihood, key=language_likelihood.get, reverse=True)[0]                               
    if detected_lang == "english":
        f_out.write(line_orig)
        k += 1
    else:
        text_vocab = set(w.lower() for w in text if w.lower().isalpha() and w <> 'RT')
        unusual = text_vocab.difference(english_vocab)    
#             print unusual
        # THE most stringest test I can make is -- if there is any word found not in EN, then we omit the tweet
        # this has obvious mistake that the strings like "bday" will be considered "unusual", but it does capture "gooo"     
        if len(unusual) == 0:
            f_out.write(line_orig)
            k += 1
        
    if i >= TESTN:
        print "exited due to the limit in test lines", TESTN
        break

print "COMBINATION based detect"     
print "ENglish tweets found: ", k, " Percent: ", k/float(i)*100
print "Total tweets processed: ", i