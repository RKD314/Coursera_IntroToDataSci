import sys
import json

def get_five_tweets(tfn):
    tweet_file = open(tfn)                                  # open the file of tweets
    return_tweets = [{},{},{},{},{}]                                      # initialize list to contain 5 tweets (they are dictionaries)
            
    counter = 0                                             # a counter for when we get to 5 appropriate tweets
    
    for line in tweet_file:                                 # loop over the tweets
        if counter > 4:                                     # we only want to look at five of them
            continue                                        # if counter goes past 4 then leave code
                        
        tweet_jsoned = json.loads(line)                 # take the tweets out of JSON format
                
        if not 'lang' in tweet_jsoned:                      # check that the tweets have info on the language
            continue                                        # if not then leave the code
        if tweet_jsoned['lang'] != 'en':                    # check that the tweets are in English
            continue                                        # if not then leave the code
        
        if not 'text' in tweet_jsoned:                      # check that the tweets have the text field
            continue                                        # if not then leave the code
        
        return_tweets[counter] = tweet_jsoned               # fill in the appropriate element of return_tweets
        
        counter += 1                                        # increment the counter
        
    return return_tweets                                   
    
def print_the_keys(list_of_tweets):
    a_single_tweet = {}                                     # make a new dictionary to hold the info from a single tweet
    a_single_tweet = list_of_tweets[0]                      # take the info from the list of tweets
    for i in a_single_tweet:                                # loop over the keys in the tweet
        print "%s is a key" % i                             # print them
        
def five_tweets_location_values(list_of_tweets):
    print "We are trying to find location information."

    print "This is what is keyed to the 'place' key for five tweets:"
    for tweet in list_of_tweets:
        if not 'place' in tweet:
            continue
        print tweet['place']
        
    print "This is what is keyed to the 'geo' key for five tweets:"
    for tweet in list_of_tweets:            
        if not 'geo' in tweet:
            continue
        print tweet['geo']

    print "This is what is keyed to the 'coordinates' key for five tweets:"
    for tweet in list_of_tweets:            
        if not 'coordinates' in tweet:
            continue
        print tweet['coordinates']

    print "This is what is keyed to the 'created_at' key for five tweets:"
    for tweet in list_of_tweets:            
        if not 'created_at' in tweet:
            continue
        print tweet['created_at']
            
    print "This is what is keyed to the 'user' key for five tweets:"
    for tweet in list_of_tweets:            
        if not 'user' in tweet:
            continue
        #print tweet['user']
        
        for usinfo in tweet['user']:
            print "%s is a key for the 'user' field" % usinfo
            
def print_user_info(list_of_tweets):
    a_single_tweet = {}                                     # make a new dictionary to hold the info from a single tweet
    a_single_tweet = list_of_tweets[0]                      # take the info from the list of tweets
    if not 'user' in a_single_tweet:
        print "no user info found!"
        return
        
    user_info = a_single_tweet['user']
    for i in user_info:                                # loop over the keys in the tweet
        print "%s:" % i                             # print them
        print user_info[i]
        print ""
            
                
def main():
    
    my_tweets = get_five_tweets(sys.argv[1])
    
    print "The following is a list of keys in the tweet..."
    print_the_keys(my_tweets)
    print ""
    print ""
    
    five_tweets_location_values(my_tweets) 
    
    print_user_info(my_tweets) 
        
if __name__ == '__main__':
    main()
