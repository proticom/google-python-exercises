#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def sort_fn(s):
  return s[-8:]

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # Extract Server from File
  match = re.search(r'_(\S+)',filename)
  server_name = match.group(1)

  # Open File
  f = open(filename, 'rU') 

  # Read File
  s = f.read()

  # Close File
  f.close()

  # Find All Puzzle Pieces
  #"GET /edu/languages/google-python-class/images/puzzle/a-baae.jpg HTTP/1.0"
  puzzle_pieces = re.findall(r'GET (\S+puzzle\S+) HTTP',s)

  # Make Unique and Sorted
  pieces = []
  for puzzle_pieces[0] in sorted(puzzle_pieces, key=sort_fn):
    if 'http://' + server_name + puzzle_pieces[0] not in pieces:
      pieces.append('http://' + server_name + puzzle_pieces[0])
  return pieces

  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # Verify Directory Exists.  If not create it.
  print 'Verifying Directory: ' + dest_dir
  if os.path.exists(dest_dir)==False:
    print 'Creating Directory: ' + dest_dir
    os.makedirs(dest_dir)

  # Download Image Files with incremented nama and create IMG html line
  f = open(dest_dir + '/index.html', 'a')
  img_html = []
  img_count = len(img_urls)
  i = 0
  for img in img_urls:
    i = i + 1
    print 'Retrieving File ' + str(i) + ' of ' + str(img_count) + '.'
    urllib.urlretrieve(img, dest_dir + '/img' + str(i))
    img_html.append('<img src=\"img' + str(i) + '\">')

  # Create index.html file
  print 'Writing index.html'
  f.write('<verbatim>')
  f.write('<html>')
  f.write('<body>')
  f.write(''.join(img_html))
  f.write('</body>')
  f.write('</html>')
  f.close()
  

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
