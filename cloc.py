import os
import sys



def cloc(file):
	if(file.endswith('.java')):
			f = open(file)
			finalCount = lineCounter(f.readlines())
			f.close()

			return finalCount

def lineCounter(f):
	loc = 0
	cloc = 0
	for line in f:
		if(line != "\n"):
			loc+=1
			if( "*" in line or '"' in line or "//" in line):
				cloc += 1
	return round(cloc/loc,4)

def start(string):
	if (not isinstance(string, str)):
		return f"{string}"
	else:
		return string

def result(file):
	out = cloc(start(file))
	return out 

if __name__ == "__main__":
	result(sys.argv[1])
