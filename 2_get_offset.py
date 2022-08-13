#!/usr/bin/python
import sys, socket, os, subprocess

print "You don't need to run the application for get offset."
print "Just give me the EIP value, I'll find the offset :)\n"

if len(sys.argv) != 3:
	print "incorrect use of script by Onurgule"
	print "python2 2_find_offset.py len EIP"
	sys.exit()

try:
	#subprocess.run(['msf-pattern_create', '-l', sys.argv[3]],caprute_output=True)
	offset = subprocess.check_output('msf-pattern_offset -q '+sys.argv[2]+' -l ' +  (sys.argv[1]), shell=True)
	print "OFFSET:" + str(offset)

except:
	print "Error, I think it's the wrong EIP value. Run first script again."
	sys.exit()
