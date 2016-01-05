import sys
import json


# function that loops over tweets
def tweet_loop(tfn):
    # dictionary that stores infos on how many tweets have certain fields filled
    counts_fields_tweet = {'text':0, 'user':0, 'place':0, 'coordinates':0, 'user_location':0, 'place_full_name':0, 'place_name':0, 'total':0}

    tweet_file = open(tfn)                                      # open the file of tweets
            
    for line in tweet_file:                                     # loop over tweets   
    
        counts_fields_tweet['total'] += 1                       # increment the total number of tweets by 1 
    
        tweet_jsoned = json.loads(line)                         # take the tweet out of JSON format
                
        if 'text' in tweet_jsoned:                              # check if the tweet has a 'text' field
            counts_fields_tweet['text'] += 1                    # if yes, increment the counter for this field
            
        if 'user' in tweet_jsoned:                              # check if the tweet has a 'user' field
            counts_fields_tweet['user'] += 1                    # if yes, increment the counter for this field
            user_infos = tweet_jsoned['user']                   # separate dictionary for user field
            if user_infos is not None and 'location' in user_infos:    # check if the user info has location filled
                counts_fields_tweet['user_location'] += 1       # if yes, increment the counter for this field

        if 'place' in tweet_jsoned:                             # check if the tweet has a 'place' field
            counts_fields_tweet['place'] += 1                   # if yes, increment the counter for this field
            place_infos = tweet_jsoned['place']                 # separate dictionary for place field
            if place_infos is not None and 'full_name' in place_infos: # check if the place info has full name of location filled
                counts_fields_tweet['place_full_name'] += 1     # if yes, increment the counter for this field
            if place_infos is not None and 'name' in place_infos:      # check if the place info has the name of the location filled
                counts_fields_tweet['place_name'] += 1          # if yes, increment the counter for this field

        if 'coordinates' in tweet_jsoned:                       # check if the tweet has a 'coordinates' field
            counts_fields_tweet['coordinates'] += 1             # if yes, increment the counter for this field
            
    return counts_fields_tweet

# main code
def main():        
    
    infos = tweet_loop(sys.argv[1])           # loop over tweets
    
    total = float(infos['total'])
    text_frac = float(float(infos['text'])/total)*100.
    user_frac = float(float(infos['user'])/total)*100.
    user_loc_frac = float(float(infos['user_location'])/total)*100.
    plac_frac = float(float(infos['place'])/total)*100.
    plac_full = float(float(infos['place_full_name'])/total)*100.
    plac_nam = float(float(infos['place_name'])/total)*100.
    coord = float(float(infos['coordinates'])/total)*100.
    
    print "There were %i total tweets in this file." % total
    print ""
    print "%.2f percent of the tweets had text" % text_frac
    print "%.2f percent of the tweets had user information" % user_frac
    print "%.2f percent of the tweets had user location information" % user_loc_frac
    print "%.2f percent of the tweets had place information" % plac_frac
    print "%.2f percent of the tweets had place full name information" % plac_full
    print "%.2f percent of the tweets had place name information" % plac_nam
    print "%.2f percent of the tweets had coordinates information" % coord

if __name__ == '__main__':
    main()

