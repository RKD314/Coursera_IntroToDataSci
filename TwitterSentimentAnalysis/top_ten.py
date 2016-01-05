import sys
import json


# function that loops over tweets
def tweet_loop(tfn):
    counts_tags = {}                                            # initialize dictionary that will hold hashtags and their counts

    tweet_file = open(tfn)                                      # open the file of tweets
            
    for line in tweet_file:                                     # loop over tweets       
        tweet_jsoned = json.loads(line)                         # take the tweet out of JSON format
        
        if not 'lang' in tweet_jsoned:
            continue
        if not tweet_jsoned['lang'] == "en":
            continue
                
        if not 'entities' in tweet_jsoned:                      # check if the entities field is there
            continue                                            # if not, go to the next tweet
        tweet_entities = tweet_jsoned['entities']
            
        if not 'hashtags' in tweet_entities:                    # check if the entities dictionary has a hashtags field
            continue                                            # if not, go to the next tweet
        list_tags = tweet_entities['hashtags']
 
        for x in range (0,len(list_tags)):                      # loop over the list of hashtags in the tweet
            if list_tags[x]['text'] in counts_tags:             # check if the given hashtag is already in the dictionary of hashtags
                counts_tags[list_tags[x]['text'].encode('utf-8')] += 1          # if it is then increment the value by 1
            else:
                counts_tags[list_tags[x]['text'].encode('utf-8')] = 1           # if it's not then add it there with a value 1

    return counts_tags

# main code
def main():        
    
    infos = tweet_loop(sys.argv[1])           # loop over tweets
    
    count_output = 0
    for w in sorted(infos, key=infos.get, reverse=True):        # for each key in the hashtags dictionary
        if count_output < 10:
            count_output += 1
            print "%s %i" % (w, infos[w])                           # print the hashtag and how many times it occurs
    
if __name__ == '__main__':
    main()

