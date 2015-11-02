import tweepy
#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
auth = tweepy.OAuthHandler('7tFcOO7GSIzpwbOLVN87s6gp9', 'AxmvGX8ck1W6lY29O7BajT9tsjwvbsGo618TQOtrLHqOkemMcA')
auth.set_access_token('3163756434-F9uPOajp97lq8UYo3ui2bvo41k8lggwyYsjydWb', 'lDObvgBxrpDSm6HVLOwtDZnlO87EQ2AuEVTBedeV5XEPD')




api = tweepy.API(auth)

def status(text):
    print 'Updating status ' + text + '...'
    api.update_status(status=text)
page_list = []

def show_timeline():
    for status in api.user_timeline():
           print status.text

if __name__ == "__main__":
    while True:
        command = raw_input()
        if command=='status':
            print 'Enter Status:'
            text = raw_input()
            status(text)
        if command=='timeline':
            show_timeline()
