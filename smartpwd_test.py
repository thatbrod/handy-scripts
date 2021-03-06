#!/usr/bin/python
"""Tests for smartpwd."""

from __future__ import print_function

import unittest

from smartpwd import smartpwd


class SmartpwdTest(unittest.TestCase):

  def setUp(self):
    self.home = "/usr/home"
    self.maxlen = 16

  def testJustHome(self):
    cwd = "/usr/home"

    actual = smartpwd(cwd, self.home, self.maxlen)
    expected = "~"

    self.assertEqual(expected, actual)

  def testJustHomeAsCwdButWithLongIntermediateDirectoryName(self):
    cwd = "/usr/home/reallylikeuneccesarilylongdirectoryname/shortdir1"

    actual = smartpwd(cwd, self.home, self.maxlen)
    expected = "~/r.../shortdir1"

    self.assertEqual(expected, actual)

  def testDirectoryThatFitsSnuggly(self):
    cwd = "/etc/shortdir1"

    actual = smartpwd(cwd, self.home, self.maxlen)
    expected = cwd

    self.assertEqual(expected, actual)

  def testReallyLongInitialDirectory(self):
    cwd = "/reallylikeuneccesarliylongdirectoryname/shortdir1/shortdir2"

    actual = smartpwd(cwd, self.home, self.maxlen)
    expected = "/re.../shortdir2"

    self.assertEqual(expected, actual)

  def testReallyLongFinalDirectory(self):
    cwd = "/shortdir1/shortdir2/reallylikeuneccesarliylongdirectoryname"

    actual = smartpwd(cwd, self.home, self.maxlen)
    # N.B. this is the only case where we ignore maxlen.
    expected = ".../reallylikeuneccesarliylongdirectoryname"

    self.assertEqual(expected, actual)                        
                                                              
  def testReallyLongIntermediateDirectory(self):
    cwd = "/shortdir1/reallylikeuneccesarliylongdirectoryname/shortdir2"

    actual = smartpwd(cwd, self.home, self.maxlen)
    expected = "/sh.../shortdir2"

    self.assertEqual(expected, actual)


if __name__ == "__main__":
  unittest.main()
