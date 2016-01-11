'''
Created on Mar 11, 2015

@author: sscepano
'''
    # This one serves for reading in data in full --- for finding number of users, user homes etc
import src.qualitative_test_mongo_cv as q_test
import logging
import traceback
import sys



_log = logging.getLogger(__name__)

def main():

    logging.basicConfig(level=logging.INFO, format='%(name)s: %(levelname)-8s %(message)s')

    _log.info("Data loaded.")
    while True:
        sys.argv = raw_input("Enter the 2 words and press enter to start a process cycle:\n").split()
        try:
            reload(q_test)
        except NameError:
            _log.error("Could not reload the module.")
        try:
            # THIS THE FUNCTION YOU ARE TESTING
            word1 = sys.argv[0]
            word2 = sys.argv[1]
            print "Relatedness of the words: ", word1, word2
            SR = q_test.find_words_SR(word1, word2)
            
            print "Relatedness of the words: ", word1, word2, " is ", SR

            
        except Exception as e:
            _log.error("Caught exception from the process\n%s\n%s" % (e, traceback.format_exc()))

        _log.info("Cycle ready.")


if __name__ == '__main__':
    main()
    
    
    '''
computer-keyboard 0.762 0.0261 0.77 0.757 --  0.806778608625
student-professor 0.681 0.3772 0.16 0.640 --  0.796470883524
news-report 0.816 0.0883 0.33 0.728 -- now NEWS
stock-market 0.808 n/a 0.41 0.775 -- 0.85954178585
psychology-science 0.671 n/a 0.40 0.665 -- 0.722928463173
computer-software 0.850 0.5791 0.87 0.806 -- 0.814316709814
man-woman 0.830 n/a 0.37 0.790 -- 0.856005317833
stock-live 0.373 0.01 0.03 0.320 -- 0.806736151487
weather-forecast 0.834 n/a 0.81 0.780 -- 0.85512275379
computer-news 0.447 0.0363 0.05 0.499 -- 
--------------------------------------
report sun  is  0.658328257585

    '''
    
    
    
    '''
    
cord-smile 0.13 0.02 0.54 0.170 0.170 0.030 0.030 0.030 0 0                        --- 0.904043464758
rooster-voyage 0.08 0.04 0.62 0.213 0.213 0.186 0.182 0.142 0.158 0.208            --- 0.959864375765
noon-string 0.08 0.04 0.54 0.240 0.240 0.141 0.147 0.127 0.124 0                    --- 0.862499111307
glass-magician 0.11 0.44 2.08 0.335 0.335 0.174 0.176 0.115 0.060 0                --- 0.823259723598
monk-slave 0.55 0.57 0.92 0.323 0.323 0.229 0.203 0.090 0.024 0
coast-forest 0.42 0.85 3.15 0.607 0.607 0.500 0.525 0.425 0.356 0.271
monk-oracle 1.10 0.91 5.00 0.218 0.218 0.113 0.118 0 0 0
lad-wizard 0.42 0.99 0.92 0.262 0.262 0.213 0.192 0.052 0.066 0                    --- 0.700690640863
forest-graveyard 0.84 1.00 1.85 0.342 0.333 0.241 0.226 0.206 0.164 0.119
food-rooster 0.89 1.09 4.42 0.309 0.339 0.354 0.324 0.259 0.228 0.193
coast-hill 0.87 1.26 4.38 0.634 0.607 0.581 0.574 0.574 0.577 0.593
car-journey 1.16 1.55 5.85 0.517 0.517 0.494 0.432 0.273 0.182 0.130
crane-implement 1.68 2.37 2.69 0.112 0.112 0.108 0.044 0.044 0 0
brother-lad 1.66 2.41 4.46 0.313 0.327 0.324 0.318 0.173 0.228 0.213
bird-crane 2.97 2.63 7.38 0.535 0.535 0.549 0.622 0.442 0.410 0.259
bird-cock 3.05 2.63 7.10 0.443 0.443 0.429 0.416 0.416 0.379 0.338
food-fruit 3.08 2.69 7.52 0.669 0.682 0.682 0.686 0.586 0.548 0.465
brother-monk 2.82 2.74 6.27 0.510 0.532 0.506 0.479 0.309 0.156 0.117
furnace-stove 3.10 3.11 8.79 0.445 0.445 0.413 0.521 0.361 0.319 0
magician-wizard 3.50 3.21 9.02 0.568 0.568 0.565 0.563 0.433 0.340 0.267
journey-voyage 3.84 3.58 9.29 0.644 0.644 0.578 0.624 0.494 0.375 0.297                ---  0.851711190814
coast-shore 3.70 3.60 9.10 0.706 0.716 0.734 0.746 0.620 0.539 0.462
implement-tool 2.95 3.66 6.46 0.642 0.642 0.632 0.672 0.502 0.102 0
boy-lad 3.76 3.82 8.83 0.459 0.490 0.511 0.680 0.430 0.462 0.390
automobile-car 3.92 3.92 8.94 0.800 0.814 0.810 0.875 0.785 0.761 0.750
gem-jewel 3.84 3.94 8.96 0.585 0.585 0.547 0.629 0.489 0.491 0.449                   ---  0.879916755764
    
    '''