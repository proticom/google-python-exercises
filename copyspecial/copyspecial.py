#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
## Example pulls filenames from a dir, prints their relative and absolute paths
def validate_dir(dir):
  if os.path.exists(dir)==False:
    os.makedirs(dir)
  return


def get_special_paths(dir):
  l_files = []
  filenames = os.listdir(dir)
  for filename in filenames:
    match = re.search(r'__\w+__',filename)
    if match:
      f_path = os.path.join(dir,filename)
      f_abspath = os.path.abspath(f_path)
      l_files.append(f_abspath)
  return l_files

def copy_to(from_dir,to_dir):
  validate_dir(to_dir)
  for path in get_special_paths(from_dir):
    shutil.copy(path,to_dir)


def zip_to(paths,zippath):
  l_files = get_special_paths(paths)
  cmd = 'zip -j ' + zippath + ' ' + ' '.join(l_files)
  print "Command to run:", cmd   ## good to debug cmd before actually running it
  (status, output) = commands.getstatusoutput(cmd)
  if status:    ## Error case, print the command's output to stderr and exit
    sys.stderr.write(output)
    sys.exit(1)
  print output  ## Otherwise do something with the command's output

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  if todir == '' and tozip == '':
    for file in get_special_paths(args[0]):
      print file

  if todir != '':
    copy_to(args[0],todir)

  if tozip != '':
    zip_to(args[0],tozip)

  
if __name__ == "__main__":
  main()
