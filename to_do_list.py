class Task:
	pass

mydict={}

while True:
	print('Lets make ur life simpler')
	print('1. Create a task \n 2. View ur task \n 3. Completed your task \n 4.Thank you ')	
	 
	inp = int(input('Enter option number:'))
	
	if inp == 1:
		key =input('Task number:')
		values = input('What is ur task?:')
		mydict[key]=values

	elif inp == 2:
		print(mydict)

	elif inp == 3:
		print('if u have completed your task?\n mark as done')
		print(mydict)
		mark_done = input('Please enter the task number of the task completed:')
		for key in list(mydict.keys()) :
			if key == mark_done:
				del mydict[key]
				print('You have successfuly completed your task')

	elif inp == 4:
		break	
					