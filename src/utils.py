def get_unique_words(tweets):
    words = set()
    for user in tweets.keys():
        for tweet in tweets[user]:
            words.update(tweet['text'].split(" "))
    return words
