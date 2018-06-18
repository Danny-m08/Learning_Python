#!/usr/bin/python2.7
import argparse
import os
import re
import stat
import sys
from stat import *

def printFiles( directory ):
	files = os.listdir(directory)
	cwd = os.getcwd()
	os.chdir(directory)
	for temp in files:
		if temp[0] != '.':
			mode = os.stat(temp)[ST_MODE]
			if stat.S_ISREG(mode):
				print directory + '/' + temp

	return

def regexFiles( exp, directory ):
	files = os.listdir(directory)
	os.chdir(directory)
	retype = re.compile(exp + '$')
	for temp in files:
			if temp[0] != '.' and retype.match(temp):
				print directory + '/' + temp
	return

def regexFilecontent( exp, directory ):
	line_number = 0
	files = os.listdir(directory)
        os.chdir(directory)
        retype = re.compile(exp)
	for temp in files:
		mode = os.stat(temp)[ST_MODE]
		if stat.S_ISREG(mode):
			file = open(temp, 'r')
                       	lines = file.readlines()
                        for line in lines:              #parse each line
                        	line_number+= 1
                               	for string in line.split(): #split line into multiple strings
                               		if retype.match(string):
                                       		print directory + '/' + temp, line_number, ': ' + line
        	line_number = 0
        	file.close()
	return


def both( file_exp, cont_exp, directory ):
	line_number = 0
	files = os.listdir(directory)
        os.chdir(directory)
        filere = re.compile(file_exp)
	contre = re.compile(cont_exp)
	for temp in files:
		if filere.match(temp):
			file = open(temp, 'r')
			lines = file.readlines()
			for line in lines:
				line_number = line_number + 1
				for string in line.split():
					if contre.match(string):
						print('%(dir)s/%(file)s %(line)i : %(cont)s' %{'dir':directory, 'file':temp, 'line':line_number, 'cont':line})
		line_number = 0	
	if file:
		file.close()
	
	

def main():


	parser = argparse.ArgumentParser(description='')
	parser.add_argument('directory', help='directory name') 
	parser.add_argument('-name', help = 'file name')		#mode = os.stat(temp)
	parser.add_argument('-grep', help = 'file name')
	args = parser.parse_args()
	if not args.grep and not args.name:
		printFiles( args.directory)
		exit(0)
	elif not args.grep:		#if only name is provided
		regexFiles(args.name, args.directory)
		exit(0)
	elif not args.name:		#else if only grep is provided
		regexFilecontent( args.grep, args.directory)
		exit(0)
	else:
		both( args.name, args.grep, args.directory)
	return

if __name__ == '__main__': main()
