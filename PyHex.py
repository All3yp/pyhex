##############################################################
#	Gerador de hexa em python								 #
#			                  Created by Kr1pt0nG1rl		 #
#	          anhax team		                        	 #
#									Pyladies++				 #
#															 #
#											                 #
##############################################################

import os
import sys


try:
	string = sys.argv[1]
	cmd = "echo -n" + string + " | xxd  -ps | sed 's/[[:xdigit:]]\{2\}/\\\\x&/g'"
	os.system(cmd)
except IndexError:
	#string = raw_input("\nInforme uma string!\r")
	print("\nInforme uma string!\r") # ao compilar vc passa o parâmetro EX: 'python pyhex.py  "teste" '
	#string = input("\nInforme uma string!\r")

