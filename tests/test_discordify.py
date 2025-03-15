import pytest
from src.discordify import discordify
class Tests:
    def test_dummify_get(self):
        actual = discordify.dummify('hello')
        assert len(actual) > 0
    def test_dummify_string(self):
        actual = discordify.dummify('hello')
        assert isinstance(actual, str)
    def test_dummify_equality(self):
        actual = discordify.dummify('hello')
        assert actual == "holle"

        actual = discordify.dummify('Hi, how are you?')
        assert actual == "Hu, how era yoi?"
    
    def test_stutterify_get(self):
        actual = discordify.stutterify('hello')
        assert len(actual) > 0
    def test_stutterify_string(self):
        actual = discordify.stutterify('hello')
        assert isinstance(actual, str)
    def test_stutterify_equality(self):
        actual = discordify.stutterify('hello')
        assert actual == "h-hello"

        actual = discordify.stutterify('Hello, how are you? I am fine, but tired.')
        assert actual == "H-Hello, how are y-you? I-I am fine, but... tired."