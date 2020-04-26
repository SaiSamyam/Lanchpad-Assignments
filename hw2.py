mydict={"hello" : "world", "speckbit" : "self-learning", "life" : "meaning"}
val=input('Enter value:')

for keys , values in mydict.items():
	if values == val:
		print(keys)