'''
	Program:	Hybotics_Utils.py, some nice little *NIX utilities I use in many places.

				Copyright (C) 2013 Dale Weber. ALL Rights Reserved. License to be chosen.

	Author:		Dale Weber <hybotics.pdx@gmail.com, @hybotics (App.Net and Twitter)>

	Version:	0.3.1 (Unstable)
	Date:		25-Jan-2014
	Purpose:	To have a place to put the utilities I create for *NIX functions
	
				Renamed library to Hybotics_Utils.py
	
	Requires:	Python v3.3.1 or later

'''
import os

'''
	Functions
'''

def getTimeZone():
	tzpath = "/etc/timezone"
	tzone = "TIMEZONE"

	if os.path.islink(tzpath):
		tpath = os.path.realpath(tzpath)
		spath = os.path.split(tpath)
		tzone = spath[1]
	elif os.path.isfile(tzpath):
		t = open(tzpath, "r", encoding="utf-8")
		tzone = t.read()
		tzone = tzone[0 : len(tzone) - 1]
		t.close()

	return tzone

'''
	As it says, just clear the screen..
'''
def clearScreen ():
    os.system(['clear','cls'][os.name == 'nt'])

    return None

'''
	Returns "None" or the value of zilch - handles the possibility
		of a string = None
'''
def zilch (zilch):
	if (zilch == None):
		st = "None"
	else:
		st = zilch

	return st
                                                                                
'''
	Returns a string representation of a list
'''
def stringList (l):
	length = len(l)

	lStr = "None"

	if (length > 0):
		lStr = "[ " + l[0]

		index = 1

		while (index < length):
			lStr = lStr + ", " + l[index]
			index += 1

		lStr = lStr + " ]"

	return lStr

'''
	Returns a string for a boolean value
'''
def stringBoolean (tf, itrue, ifalse):
	if (tf == True):
		st = itrue
	elif (tf == False):
		st = ifalse
	else:
		st = "None"

	return st
