# -*- coding: utf-8 -*-

##############################################################
#	Gerador de hexa em python	
#
#			       Created by Kr1pt0nG1rl	
#        anhax team		                        	
#			        	Pyladies++				
#															 
#									                         
##############################################################


import os
import sys


def iniciar():
	try:
		string = sys.argv[1]
		cmd = "echo -n" + string + " | xxd  -ps | sed 's/[[:xdigit:]]\{2\}/\\\\x&/g'"
		os.system(cmd)
	except IndexError:
		string = raw_input("\nEnter to string: ")
		if(string != ""):

			cmd = "echo -n" + string + " | xxd  -ps | sed 's/[[:xdigit:]]\{2\}/\\\\x&/g'"
			os.system(cmd)
		else:
			print("\n Finished !!")



def start():
	iniciar()


start()




