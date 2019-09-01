import sys
import os

def go(a=1,b=2):
	print a,b
	
def imback():
	print "i'm back"
	# maybe , this python syntax not working now .. 

if __name__ == "__main__":
	try: a = sys.argv[1]
	except: a = None
	try: b = sys.argv[2]
	except: b = None

	go(a, b)

