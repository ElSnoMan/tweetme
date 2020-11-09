import os


def test_environment_variables():
    assert os.getenv('TWITTER_API_KEY')
    assert os.getenv('TWITTER_API_SECRET')
    assert os.getenv('TWITTER_BEARER_TOKEN')
    assert os.getenv('TWITTER_ACCESS_TOKEN')
    assert os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
