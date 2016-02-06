import os
import sys
def recFile(path1,text):
	for i in os.listdir(path1):
		p=os.path.join(path1,i)
		if(os.path.isdir(p)==False):
			if text in open(p).read():
				print p+"\n"

		else:
			recFile(p,text)	
try:			
	path1=sys.argv[1]
	text = sys.argv[2]
except:
	print "not enough arguments"	
	exit(0)
recFile(path1,text)			
