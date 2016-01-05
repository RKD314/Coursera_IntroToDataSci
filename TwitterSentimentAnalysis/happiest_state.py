import sys
import json


# function that makes sentiment dictionary given file
def make_sentiment_dictionary(fn):
    sent_file = open(fn)                                        # opening the sentiment file
        
    scores = {}                                                 # initialize an empty dictionary

    for line in sent_file:                                      # for each line in the sentiment file
        term, score = line.split("\t", 2)                       # split it into term and score components
        scores[term] = int(score)                               # the term is the key, the score (integer) is the value

    return scores                                               # return the dictionary of scores
    

# function that loops over tweets
def tweet_loop(tfn, scores_dict):
    # initialize dictionary to store count and sentiment info on the states' tweets
    states_counts = {'AK': [0,0],'AL': [0,0],'AR': [0,0],'AZ': [0,0],'CA': [0,0],'CO': [0,0],'CT': [0,0],'DC': [0,0],'DE': [0,0],'FL': [0,0],'GA': [0,0],'HI': [0,0],'IA': [0,0],'ID': [0,0],'IL': [0,0],'IN': [0,0],'KS': [0,0],'KY': [0,0],'LA': [0,0],'MA': [0,0],'MD': [0,0],'ME': [0,0],'MI': [0,0],'MN': [0,0],'MO': [0,0],'MS': [0,0],'MT': [0,0],'NC': [0,0],'ND': [0,0],'NE': [0,0],'NH': [0,0],'NJ': [0,0],'NM': [0,0],'NV': [0,0],'NY': [0,0],'OH': [0,0],'OK': [0,0],'OR': [0,0],'PA': [0,0],'RI': [0,0],'SC': [0,0],'SD': [0,0],'TN': [0,0],'TX': [0,0],'UT': [0,0],'VA': [0,0],'VT': [0,0],'WA': [0,0],'WI': [0,0],'WV': [0,0],'WY': [0,0]}

    tweet_file = open(tfn)                                      # open the file of tweets
            
    for line in tweet_file:                                     # loop over tweets    
    
        tweet_jsoned = json.loads(line)                         # take the tweet out of JSON format
                
        if not 'text' in tweet_jsoned:                          # check if the tweet has a 'text' field
            continue                                            # if not, go to the next tweet
        if not 'user' in tweet_jsoned:                          # check if the tweet has a 'user' field
            continue                                            # if not, go to the next tweet
        user_info = tweet_jsoned['user']                        # put the user info field into it's own dictionary
        if not user_info['location']:                           # check if the user has location information
            continue                                            # if not, go to the next tweet
                
        current_state = find_state(user_info['location'])       # find whether any state information in the "user", "location" key
        if current_state == "FALSE":                            # if not
            continue                                            # we go on to the next tweet
        sum_sentiments = find_sentiment_score(tweet_jsoned['text'], scores_dict) # initialize the cumulative sentiment score for tweet
                
        states_counts[current_state][0] += sum_sentiments       # add to the cumulative sentiment score for tweets from the current state
        states_counts[current_state][1] += 1                    # increment the count of tweets from the current state
        
    return states_counts


# function that, given a single tweet, finds the state and returns current_state
def find_state(user_location):     
    # initialize a dictionary to store the states' abbreviations and names
    states_dict = states = {'AK': 'Alaska','AL': 'Alabama','AR': 'Arkansas','AZ': 'Arizona','CA': 'California','CO': 'Colorado','CT': 'Connecticut','DC': 'District of Columbia','DE': 'Delaware','FL': 'Florida','GA': 'Georgia','HI': 'Hawaii','IA': 'Iowa','ID': 'Idaho','IL': 'Illinois','IN': 'Indiana','KS': 'Kansas','KY': 'Kentucky','LA': 'Louisiana','MA': 'Massachusetts','MD': 'Maryland','ME': 'Maine','MI': 'Michigan','MN': 'Minnesota','MO': 'Missouri','MS': 'Mississippi','MT': 'Montana','NC': 'North Carolina','ND': 'North Dakota','NE': 'Nebraska','NH': 'New Hampshire','NJ': 'New Jersey','NM': 'New Mexico','NV': 'Nevada','NY': 'New York','OH': 'Ohio','OK': 'Oklahoma','OR': 'Oregon','PA': 'Pennsylvania','RI': 'Rhode Island','SC': 'South Carolina','SD': 'South Dakota','TN': 'Tennessee','TX': 'Texas','UT': 'Utah','VA': 'Virginia','VT': 'Vermont','WA': 'Washington','WI': 'Wisconsin','WV': 'West Virginia','WY': 'Wyoming'}
    
    state_name = ""                                             # initialize the variable for state name (what will be returned)
    location_words = user_location.split()                      # split the user's location information into words
    
    for i in location_words:                                    # for each word in the user's location
        if len(i) < 2 or "," in i:                              # if there are less than 2 letters in the word, or a comma, go to the next one
            state_name = "FALSE"
            continue
        elif len(i) > 2:                                        # if there are more than 2 letters in the word, check if it is in the dictionary of states
            if not i in states_dict:                            # if not, then go to the next word
                state_name = "FALSE"
                continue
            else:                                               # otherwise, it must be a value not a key since it is more than 2 characters
                for k in states_dict:                           # look over the states dictionary
                    if i in states_dict[k]:                     # if the word belongs to the state value
                        state_name = k                          # then the state name is equivalent to the key
                        return state_name
        else:                                                   # if the word is exactly 2 characters long, check if it is in the dictionary of states
            if not i in states_dict:                            # if not then go onto the next word
                state_name = "FALSE"
                continue
            else:                                               # if it is in the dictionary check that it matches a key
                for k in states_dict:                           # look over the states dictionary
                    if i == k:                                  # if the word is equivalent to one of the keys
                        state_name = i                          # then fill that for the state name
                        return state_name
    
    if state_name == "":
        state_name = "FALSE"
    
    return state_name
            

# function that, given a single tweet, computes the sentiment score
def find_sentiment_score(tweet, score_dic):
    sent_sum = 0                                                # initialize the cumulative sentiment score for the tweet
    tweet_text = tweet.encode('utf-8')                          # isolate tweet text
    tweet_split = tweet_text.split()                            # and split it into words
                            
    for k in tweet_split:                                       # for each word in the tweet
        if k in score_dic:                                      # check if the word is in the sentiment dictionary
            sent_sum += score_dic[k]                            # if yes, then add the word's sentiment to the cumulative sentiment score
           
    return sent_sum


# function that finds state with the highest average sentiment score per tweet
def find_highest_sent_state(the_states):
    highest_state = ""
    highest_avg = 0
    current_avg = 0.
    
    for k in the_states:
        if the_states[k][1] > 0:
            current_avg = float(float(the_states[k][0])/float(the_states[k][1]))
        else:
            current_avg = 0.
        
        if current_avg >= highest_avg:
            highest_avg = current_avg
            highest_state = k
        else:
            continue
            
    print "%s" % highest_state    
        
# main code
def main():        
    s_scores = make_sentiment_dictionary(sys.argv[1])        # make dictionary of sentiment words
    
    state_info = tweet_loop(sys.argv[2], s_scores)           # loop over tweets
    
    #print state_info
    
    find_highest_sent_state(state_info)                      # print the abbreviation of the state with highest avg sentiment with it's score

if __name__ == '__main__':
    main()

