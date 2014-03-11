# 2. Write a function named `add_dict(dict_1, dict_2)` that joins the two dictionaries 
# provided as arguments and returns a single dictionary with all the items of `dict_1` and `dict_2`
dict_1={'123123':'78798798', 'adasda':'adasdasdasda', 'qdqhhdqwdqw':'adasdasdas'}
dict_2={'marco': 'desk','giulio': 'desk 2','mike': 'room 3'}

def add_dict(dict_1, dict_2):
	dict_X={} #crea un dizionario vuoto
	for word in dict_1: 
		dict_X[word]=dict_1[word] #copia ogni chiave/valore di dict_1 in dict_X
	for word in dict_2:
		dict_X[word]=dict_2[word] #fai la stessa cosa di dict_1 con dict_2

	print dict_X #stampa dict_X

if __name__ == '__main__':
	add_dict(dict_1, dict_2)