import tweepy
import re
from PIL import Image, ImageDraw, ImageFont

def tweets_get(key):
    '''Get the text from twitter using tweepy and convert text into image'''


    consumer_key = 'BePXBQnnodwym2KOVSVaDGMJt'
    consumer_secret = 'vj4G9SYGRzHWZLwHoHtsUjqeBNgQQY7q4FFPnxs3SkTDGfaQ7E'
    access_token = '1171640747352842244-WPkonJaaXqQFSDJPwyT218uYW6WsSO'
    access_token_secret = 'izFind6UV5DghAsQLdXxoo2TVpks7hv8mJ5lEKG32r0Kl'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    public_tweets = api.search(q=key, count=10)
    setFont = ImageFont.truetype('/Library/Fonts/Arial.ttf', 50)

    count = 0;
    color = "#000000"
    header_y = 500
    image = Image.open('image/start.jpg')
    width, height = image.size
    draw = ImageDraw.Draw(image)

    tweets_contain = []

    for tweets in public_tweets:
        gap = '\n'
        list_contain_tweets = list(tweets.text)
        for n in range(len(list_contain_tweets)):
            if (n % 60 == 0):
                list_contain_tweets.insert(n, gap)

        tweets.text = ''.join(list_contain_tweets)
        tweets.text = re.sub("#", r'\#', tweets.text)
        tweets.text = re.sub("@", r'\@', tweets.text)
        tweets.text = re.sub('\n', '', tweets.text)

        tweets.text = tweets.text + '\n'
        tweets_contain.append(tweets.text)

        print(tweets.text)


    for num, content in enumerate(tweets_contain):
        num += 1
        draw.text((100,height - header_y),u'%s. %s' %(num, content),color,setFont)
        header_y -= 50

    image.save('image/' + key + '.jpg')
    print('-------END-------')


if __name__ == '__main__':
    tweets_get('tesla')
