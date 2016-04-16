#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  # Determine Lenght
  if len(s) >= 3:
    if s[-3:] == 'ing':
      return_value = s + 'ly'
    else:
      return_value = s + 'ing'
  else:
    return_value = s
  return return_value


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  int_not_occurrence = s.find('not')
  int_bad_occurence = s.find('bad')
  if int_not_occurrence < int_bad_occurence:
    return_value = s[:int_not_occurrence] + 'good' + s[int_bad_occurence + 3:]
  else:
    return_value = s
  return return_value


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  # Check a for Odd or Even
  if (float(len(a)))%2==0:
    correct_for_odd_a = 0
  else:
    correct_for_odd_a = 1
  a_front = a[:(len(a)/2)+correct_for_odd_a]
  a_back =  a[(len(a)/2)+correct_for_odd_a:]

  # Check b for Odd or Even
  if (float(len(b)))%2==0:
    correct_for_odd_b = 0
  else:
    correct_for_odd_b = 1
  b_front = b[:(len(b)/2)+correct_for_odd_b]
  b_back =  b[(len(b)/2)+correct_for_odd_b:]

  return a_front + b_front + a_back + b_back


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print 'verbing'
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print 'not_bad'
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
