# coding: utf-8
# 5. write a python module `esercizio5.py` that reads the remote HTTP endpoint http://ialpython.apiary.io/laboratories 
# and prints to standard output all the laboratories with network status `down`

import requests

resp = requests.get('http://ialpython.apiary.io/laboratories')
laboratories = resp.json() #ne risulta una lista di dizionari

laboratories_2=[]

for dictionary in laboratories: #inizia a ciclare ogni dizionario della lista
	for word in dictionary: #inizia a ciclare ogni chiave del dizionario
		if word=="network_status": #controllo sulle chiavi
			if dictionary[word]=="down": #controllo sui valori
				laboratories_2.append(dictionary["name"]) #Restituisce SOLO il nome del laboratorio con la rete che è "down"

print laboratories_2