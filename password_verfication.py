import re
special_char=['@','#','$']
numbers=[1,2,3,4,5,6,7,8,9,0]
uppercase_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


while True:
	password=input('Enter a password:')
	if len(password) < 8:
		print('Make sure your password has a minimum of 8 characters')
	elif len(password) > 16:
		print('Make sure your password has a maximum of 16 characters')
	elif re.search(str(numbers),password) is None:
		print('Make sure your password has a number in it')
	elif re.search(str(uppercase_letters),password) is None:
		print('Make sure your password has a captial letter')
	elif re.search(str(special_char),password) is None:
		print('Make sure your password has a special_char')

	else:
		print('Valid password')
		break			