# 3. Write a function that counts the lines of a file. The file name is provided as a function argument. It returns the number of lines in the file.

def count_line_inFile(fileName):
	reading = open(fileName, "rb")
	i = -1 
	for line in reading:	
		i += 1
	print i

if __name__ == '__main__':
	count_line_inFile("prova.txt")