import sys
import os

def go(a=1,b=2):
	print a,b

if __name__ == "__main__":
	try: a = sys.argv[1]
	except: a = None
	try: b = sys.argv[2]
	except: b = None

	go(a, b)

