#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "573726936-Gu39SuWMGpI2wT8HWpPyWm8sagPHJswinZ311l3o"
access_token_secret = "uBTM0bfmojmnTAsBO4296vzivrX6gzwfNCdHvIjqqFP7o"
consumer_key = "GN7HhHnWP4vCSn4V2kR1Lx4Zm"
consumer_secret = "PQIM68bBkrbzU2kmnYwIivxOo68JH20t2G9gmQWidYv6XBikD5"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['family', 'parent', 'father','mother','children','friend','modern life'])
    
    
