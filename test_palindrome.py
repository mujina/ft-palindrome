import pytest
from typing import Any

from palindrome import ft_palindrome

@pytest.fixture
def palindrome():
    return ft_palindrome()

def test_is_palindrome(palindrome):
    test_arg = 'abba'  # type: String
    assert palindrome.is_palindrome(test_arg) == "Palindrome"

def test_is_not_a_palindrome(palindrome):
    test_arg = 'abcd'
    assert palindrome.is_palindrome(test_arg) == "Not"

def test_number_arg_raises_type_error(palindrome):
    with pytest.raises(TypeError):
        test_arg = 12321
        palindrome.is_palindrome(test_arg)

def test_other_arg_type_raises_type_error(palindrome):
    with pytest.raises(TypeError):
        test_arg = []
        palindrome.is_palindrome(test_arg)

def test_no_arg_type_raises_type_error(palindrome):
    with pytest.raises(TypeError):
        test_arg = None
        palindrome.is_palindrome(test_arg)

