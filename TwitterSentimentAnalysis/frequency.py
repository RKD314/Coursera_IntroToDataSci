import sys
import json

def loop_over_tweets(tfn):
    tweet_file = open(tfn)                                      # open the file of tweets
    
    new_words={}                                                # dictionary to contain new words
        
    for line in tweet_file:                                     # loop over tweets                        
        tweet_jsoned = json.loads(line)                         # change input from json format
                
        #if not 'lang' in tweet_jsoned:
        #    continue
        #if tweet_jsoned['lang'] != 'en':
        #    continue
        
        if not 'text' in tweet_jsoned:                          # only take those entries from the API that have tweet text
            continue
        else:
            tweet_text = tweet_jsoned['text'].encode('utf-8')   # isolate the tweet text and encode it
            tweet_split = tweet_text.split()                    # split the tweet into words separated by a space
                                
        for k in tweet_split:                                   # for each word in the tweet
            if not k in new_words:                              # check if the word is in the dictionary for new words, if not
                new_words[k] = [1, 0]                           # set a list as the value for the new word
            else:                                               # if the word is in the dictionary
                new_words[k][0] += 1                            # increment by 1 the count of times it occured in the tweet (element 1)                 
                  
        for i in new_words:                                     # for each word in the dictionary
            new_words[i][1] += len(tweet_split)                 # add the number of words in this tweet to the second element of the list
             
    return new_words                                            # return the dictionary of words
            
def print_terms_with_scores(the_terms):
    frequency = 0.                                              # initialize the frequency variable
        
    for m in the_terms:                                         # for each of the keys in the dictionary
        if the_terms[m][1] == 0:                                # if there were no words in the tweets the key appeared in, there is a bug
            print "Something went wrong here!"                  # print error message
            continue                                            # leave the code
        else:            
            frequency = float(float(the_terms[m][0])/float(the_terms[m][1]))    # calculate the frequency
                                
        print "%s %f" % (m, frequency)                          # print the frequency

def main():
    
    #print 'Using tweets contained in %s' % sys.argv[1]
        
    new_terms = loop_over_tweets(sys.argv[1])
    
    print_terms_with_scores(new_terms)

if __name__ == '__main__':
    main()
