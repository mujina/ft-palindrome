#!/usr/bin/env python
import sys
import logging

logger = logging.getLogger('ft_palindrome')
logger.setLevel(logging.INFO)
screen_handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(screen_handler)

class ft_palindrome:

    def __init(self):
        pass

    def is_palindrome(self, p):

        if not p:
            raise TypeError("Argument not defined")

        if isinstance(p, str) and not p.isalpha():
            raise TypeError("Argument must be a string.")

        if p == "".join(reversed(p)):
            return("Palindrome")
        else:
            return("Not")

if __name__ == "__main__":
  ft_palindrome = ft_palindrome()
  arg = sys.argv[1]
  ans = ft_palindrome.is_palindrome(arg)
  print(ans)

