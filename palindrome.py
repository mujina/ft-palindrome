#!/usr/bin/env python
import sys

def is_palindrome(p):
  if p == "".join(reversed(p)): 
    print("Palindrome")
  else:
    print("Not")

if __name__ == "__main__":
  is_palindrome(sys.argv[1])
