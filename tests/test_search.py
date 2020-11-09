from twitter.api import Twitter
from googletrans import Translator


def test_me(twitter: Twitter):
    me = twitter.api.me()
    assert me.name == 'Carlos Kidman'
    assert me.entities['description']['urls'][0]['display_url'] == 'twitch.tv/carloskidman'


def test_translate_portuguese_tweet(twitter: Twitter):
    params = {
        'q': 'python',
        'lang': 'pt',  # Portuguese
        'count': '1'
    }
    results = twitter.api.search(**params)
    text = results[0].text
    print(text)
    translator = Translator()
    language = translator.detect(text)
    assert language.lang == 'pt'
    translated = translator.translate(text, dest='en')
    print(translated)
