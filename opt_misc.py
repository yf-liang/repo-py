#!/usr/bin/env python
# yeliang: July, 2015

import os
import re
import sys
import commands
import subprocess


class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

#  -------- function ---------------------------------------------------------
import string
import random
def rand_chars(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#  -------- function ---------------------------------------------------------
def do_cmd (cmd):
   # print ":" + cmd + ":"
   (result, output) = commands.getstatusoutput (cmd)
   return output


#  -------- main -------------------------------------------------------------

nparm = len(sys.argv)
if nparm <= 1:
   pmode = ""
else:
   pmode = str(sys.argv[1])
   
   
#  ---------------------------------------------------------------------------
if pmode == "test1":
   print "test1"

   tstr = " "
   tstr = tstr.strip()
   if (tstr == ""): print "empty 1"

   tstr = " 			 "
   tstr = tstr.strip()
   if (tstr == ""): print "empty 2"

   # set verbose if selected
   verbose = 1
   if (nparm >= 3):  
      tvar = str(sys.argv[2])
      if (tvar == '-v'):
         verbose = 0
         del sys.argv[2]
		 
   sys.exit()
   
   
   if pmode == "test1a":
   v = 'ten'
   for case in switch(v):
       if case('one'):
           print 1
           break
       if case('two'):
           print 2
           break
       if case('ten'):
           print 10
           break
       if case('eleven'):
           print 11
           break
       if case(): # default, could also just omit condition or 'if True'
           print "something else!"
           # No need to break here, it'll stop anyway
   sys.exit()

   
print """
 File: /path.dir/opt_misc.py 
Usage: /path/opt_misc.py [OPTION...] [FILE]...
"""




