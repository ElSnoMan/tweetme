from twitter.api import Twitter
import pytest


@pytest.fixture(scope='session')
def twitter():
    return Twitter()
