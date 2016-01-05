import sys
import json

def make_sentiment_dictionary(fn):
    sent_file = open(fn)    # opening the sentiment file
        
    scores = {} # initialize an empty dictionary

    for line in sent_file:
        term, score = line.split("\t", 2)
        scores[term] = int(score)  # Convert the score to an integer.

    return scores
    
def loop_over_tweets(tfn, sentiments):
    tweet_file = open(tfn)  # open the file of tweets
    
    for line in tweet_file:         # loop over tweets
        print 'Analyzing a new tweet...'
                
        sum_sentiments = 0
        tweet_jsoned = json.loads(line)
           
        if not 'lang' in tweet_jsoned:
            continue
        if tweet_jsoned['lang'] != 'en':
            continue
        if not 'text' in tweet_jsoned:
            continue
        else:
            tweet_text = tweet_jsoned['text'].encode('utf-8')            
            tweet_split = tweet_text.split()
        
        for k in tweet_split:       # for each word in the tweet
            if k in sentiments:     # check if the word is in the dictionary for sentiment
                sum_sentiments += sentiments[k]
                
        print sum_sentiments

def main():
          
    sent_scores = make_sentiment_dictionary(sys.argv[1])
    loop_over_tweets(sys.argv[2], sent_scores)

if __name__ == '__main__':
    main()
