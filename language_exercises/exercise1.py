# 1. Write a function `dict_values_ascending` that accecpts a dictionary as an argument and returns a list of dictionary *values* in ascending order
dict_1={'marco': 'desk 1','giulio': 'desk 2','mike': 'room 3'}


def dict_values_ascending(dict_1):
	tempList=[] #crea una lista vuota
	for word in dict_1: 
		tempList.append(dict_1[word]) #aggiungi alla lista i valori in dict_1
	tempList.sort() #~metti in ordine alfabetico il contenuto della lista
	print tempList


if __name__ == '__main__':
	dict_values_ascending(dict_1)


