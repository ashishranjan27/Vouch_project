import tweepy 
def get_followers_list(username):
    # assign the values accordingly 
    consumer_key = "mfSHzc5idBPnMq8WqGcEbG8IW" 
    consumer_secret = "Dsdixhra80SVKGXV9FpQw4tfXJqZxcfABAkxkPUipCBSmN3cVT" 
    access_token = "782630294826344448-Rw889ISDTY63jLbohPbQwseQhXZPayL" 
    access_token_secret = "M3M9coP476g6ed6vknCRLBqWn3MxKkanunyQsSTI3aDFk" 
    
    # authorization of consumer key and consumer secret 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    
    # set access to user's access key and access secret  
    auth.set_access_token(access_token, access_token_secret) 
    
    # calling the api  
    api = tweepy.API(auth) 
    
    # the screen_name of the targeted user 
    screen_name = str(username)
    followers_list=[]
    # printing the latest followers 20 to not heavily fill our db
    for follower in api.followers(screen_name): 
        print(follower.screen_name)
        followers_list.append(follower.screen_name)
    return followers_list


def get_user_timeline(username):
    # assign the values accordingly 
    consumer_key = "mfSHzc5idBPnMq8WqGcEbG8IW" 
    consumer_secret = "Dsdixhra80SVKGXV9FpQw4tfXJqZxcfABAkxkPUipCBSmN3cVT" 
    access_token = "782630294826344448-Rw889ISDTY63jLbohPbQwseQhXZPayL" 
    access_token_secret = "M3M9coP476g6ed6vknCRLBqWn3MxKkanunyQsSTI3aDFk" 
    
    # authorization of consumer key and consumer secret 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    
    # set access to user's access key and access secret  
    auth.set_access_token(access_token, access_token_secret) 
    
    # calling the api  
    api = tweepy.API(auth) 
    
    # the screen_name of the targeted user 
    screen_name = str(username)
    # printing the latest followers 20 to not heavily fill our db
    statuses = api.user_timeline(screen_name, count = 50) 
    return statuses
    
    