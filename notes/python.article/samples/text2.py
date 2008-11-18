#!/usr/bin/python

import re

fh = open('wiki.txt')
for line in fh.readlines():
   if re.search("hello", line): print "Match!" 
   print line

