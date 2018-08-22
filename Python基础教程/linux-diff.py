#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is diffrent two file"""
import difflib
import sys


def main1():

    # create file test1
    test1 = """test1:
    I love you
    OK, I know, thank you very much!
    Please go to my home tonight folow me.
    """
    test1_lines = test1.splitlines()

    # create file test2
    test2 = """test2:
    I Love You
    Ok, I Know, Thanks you very much!
    sorry, go out!
    """

    test2_lines = test2.splitlines()

    d = difflib.Differ()
    diff = d.compare(test1_lines, test2_lines)
    print '\n'.join(list(diff))


def main2():
    
    file1 = """file1:
    Download the file for your platform.
    If you're not sure which to choose,
    learn more about
    Ok!
    installing packages."""
    file1_lines = file1.splitlines()
    
    file2 = """file2:
    Download The file for your Platform.
    Oh! I understand.
    Learn more about too
    installing packages."""

    file2_lines = file2.splitlines()

    d = difflib.HtmlDiff()
    diff_file = d.make_file(file1_lines, file2_lines)

    filename = sys.argv[1]
    
    if filename:
        
        with open(str(filename), 'w') as f:
	    f.write(diff_file)


if __name__ == '__main__':
  
    if len(sys.argv) >= 2:

        main2()
    else:

        main1()
