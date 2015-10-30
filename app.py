import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def status(text):
    print 'Updating status ' + text + '...'
    api.update_status(status=text)

if __name__ == "__main__":

    while True:
        command = raw_input()
        if command=='status':
            print 'Enter Status:'
            text = raw_input()
            status(text)
