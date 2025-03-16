import pytest
from src.discordify import discordify
import re

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

    def test_leetify_get(self):
        actual = discordify.leetify('hello')
        assert len(actual) > 0
    def test_leetify_string(self):
        actual = discordify.leetify('hello')
        assert isinstance(actual, str)
    def test_leetify_equality(self):
        actual = discordify.leetify('hello')
        assert actual == "H3LL0"

        actual = discordify.leetify('Hi, how are you?')
        assert actual == "H1, H0W 4R3 Y0U?"

    def test_uwuify_get(self):
        actual = discordify.uwuify('hello')
        assert len(actual) > 0
    def test_uwuify_string(self):
        actual = discordify.uwuify('hello')
        assert isinstance(actual, str)
    def test_uwuify_equality(self):
        actual = discordify.uwuify('hello')
        assert actual == "✧˖°. hewwo ₊˚⊹♡"

        actual = discordify.uwuify('Hello. How are you?')
        assert actual == "✧˖°. hewwo˚｡⋆୨୧˚\n⋆˙⟡ how awe you? ₊˚⊹♡"
        
    def test_sarcasmify_get(self):
        actual = discordify.sarcasmify('hello')
        assert len(actual) > 0
    def test_sarcasmify_string(self):
        actual = discordify.sarcasmify('hello')
        assert isinstance(actual, str)
    def test_sarcasmify_alternating_case(self):
        actual = discordify.sarcasmify('hello')
        actual = re.sub(r' 🙄$', '', actual)
        
        is_upper = None
        for i, char in enumerate(actual):
            if not char.isalpha():
                continue
                
            if is_upper is None:
                is_upper = char.isupper()
            else:
                assert char.isupper() != is_upper
                is_upper = char.isupper()
    
    def test_sarcasmify_emoji(self):
        # Test that the emoji is always added
        actual = discordify.sarcasmify('hello')
        assert actual.endswith(' 🙄')
        
        actual = discordify.sarcasmify('This is a test!')
        assert actual.endswith(' 🙄')
