import sys
import json

def make_sentiment_dictionary(fn):
    sent_file = open(fn)                                        # opening the sentiment file
        
    scores = {}                                                 # initialize an empty dictionary

    for line in sent_file:                                      # for each line in the sentiment file
        term, score = line.split("\t", 2)                       # split it into term and score components
        scores[term] = int(score)                               # the term is the key, the score (integer) is the value

    return scores                                               # return the dictionary of scores
    
def loop_over_tweets(tfn, sentiments):
    tweet_file = open(tfn)                                      # open the file of tweets
    
    new_words={}                                                # dictionary to contain new words
        
    for line in tweet_file:                                     # loop over tweets                
        sum_sentiments = 0                                      # initialize the cumulative sentiment score for the tweet
        
        tweet_jsoned = json.loads(line)                         # take the tweet out of JSON format
                
        if not 'text' in tweet_jsoned:                          # check if the tweet has a 'text' field
            continue                                            # if not, go to the next tweet
        else:
            tweet_text = tweet_jsoned['text'].encode('utf-8')   # if yes, then isolate it
            tweet_split = tweet_text.split()                    # and split it into words
                            
        for k in tweet_split:                                   # for each word in the tweet
            if k in sentiments:                                 # check if the word is in the sentiment dictionary
                sum_sentiments += sentiments[k]                 # if yes, then add the word's sentiment to the cumulative sentiment score
            elif not k in new_words:                            # if not
                new_words[k]=[0,0]                              # add the word to the new words dictionary as a key, with value [0,0]
                                                                   
        for i in new_words:                                     # for each key in the new words dictionary
            if not i in tweet_split:                            # if the word was not in the tweet
                continue                                        # go to the next item
            else:                                               # otherwise
                new_words[i][0] += sum_sentiments               # add the tweet's cumulative sentiment score to the first element of the value list
                new_words[i][1] += 1                            # increment the second element of the value list by 1 (counting total number of tweets)
            
    return new_words                                            # return the dictionary of lew words
            
def print_terms_with_scores(the_terms):
    term_score = 0.                                             # initialize variable to hold the score of each term

    for m in the_terms:                                         # for each key in the new terms dictionary
        if len(the_terms[m]) == 0:                              # if the word appeared 0 times, but is in the dictionary, 
            print "Something went wrong here!"                  # something went wrong
            continue                                            # in that case move on
        else:                                                   # otherwise, 
            term_score = float(float(the_terms[m][0])/float(the_terms[m][1]))   # calculate the term score

        print "%s %f" % (m, term_score)                         # print the term and it's score

def main():        
    sent_scores = make_sentiment_dictionary(sys.argv[1])        # make dictionary of sentiment words
    
    new_terms = loop_over_tweets(sys.argv[2], sent_scores)      # make the new terms dictionary
    
    print_terms_with_scores(new_terms)                          # print the new terms with their scores

if __name__ == '__main__':
    main()
