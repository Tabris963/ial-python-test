# 4. write a module `esercizio4.py` that reads a list of words from the command line and prints them out on standard output each one inside a `<p>` HTML tag:

 #   $ python esercizio4.py ciao hey
 #   <p>ciao</p>
 #   <p>hey</p>

import sys

def htmlStyle(argv):
	for word in sys.argv[1:]:
		print "<p> " + word +" </p>" 


if __name__ == '__main__':
	htmlStyle(sys.argv)