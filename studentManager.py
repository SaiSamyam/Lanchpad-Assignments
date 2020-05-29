from tabulate import tabulate 
from pprint import pprint
import json

# create class Students
class Student:
	#constructor
	def __init__(self): 
		print('\n Enter the following student data: ')
		self.name = input('\n Enter name of the student: ')  
		self.rollno =  int(input('\n Enter roll number of the student: '))
		self.math = int(input('\n Enter the marks scored by the student in Mathematics: '))
		self.science = int(input('\n Enter the marks scored by the student in Science: '))
		self.socialscience = int(input('\n Enter the marks scored by the student in Social Science: '))
		self.english = int(input('\n Enter the marks scored by the student in English: '))
		self.language = int(input('\n Enter the marks scored by the student in Language: '))
		self.total = self.math + self.science + self.socialscience + self.english + self.language 
		self.percentage = self.total/500 * 100
	
	def update(self,data,rn):
		print(tabulate([(1,'UPDATE MARKS IN MATHEMATICS'),(2,'UPDATE MARKS IN SCIENCE'),(3,'UPDATE MARKS IN SOCIAL SCIENCE'),(4,'UPDATE MARKS IN ENGLISH'),(5,'UPDATE MARKS IN LANGUAGE'),(6,'DONE')]))
		choice = int(input('Enter the above choice: '))
		new = int(input('Enter the revaluated marks: '))
		while True:
			if choice == 1:
				for key,val in data.items():
					if key == rn:
						for keys,values in val.items():
							val['c.MATHEMATICS: '] = new

			elif choice == 2:
				for key,val in data.items():
					if key == rn:
						for keys,values in val.items():
							val['d.SCIENCE: '] = new

			elif choice == 3:
				for key,val in data.items():
					if key == rn:
						for keys,values in val.items():
							val['e.SOCIAL SCIENCE: '] = new

			elif choice == 4:
				for key,val in data.items():
					if key == rn:
						for keys,values in val.items():
							val['f.ENGLISH: '] = new

			elif choice == 5:
				for key,val in data.items():
					if key == rn:
						for keys,values in val.items():
							val['g.LANGUAGE: '] = new

			elif choice == 6:
				print('REVALUATION COMPLETED')
				break

			else:
				print('TRY AGAIN')




						
				

							






				





				
		



	









			 
	