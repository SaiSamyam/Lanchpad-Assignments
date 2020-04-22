n=input('how many inputs  u want to take :')
records={}


for i in range(int(n)):
	name=input('Enter name:')
	USN=input('Enter USN:')
	records[USN]=name

print(records)	


