# this code was taken from Stack OverFlow as an example of how to use unitest when testing
# my Project 2 and writing unit tests.

import unittest
from unittest.mock import create_autospec, MagicMock, ANY, patch
import tweepy
from getWeek5Rankings import ConsumerKey


class MockedUser(object):
    protected = False


class TwitterTestCase(unittest.TestCase):

    def test_first(self):
        api = create_autospec(tweepy.API, name='FirstAPI')
        api.get_user = MagicMock(return_value=MockedUser)
        tweepy.API = MagicMock(return_value=api)
        self.assertTrue(ConsumerKey.validate('123'))
        api.get_user.assert_called_once_with('123')
