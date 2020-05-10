from datetime import datetime
startTime = datetime.now()

class Parking:
	two_wheeler_slots=500
	four_wheeler_slots=300
	def __init__ (self):
		self.four_wheeler_slots= four_wheeler_slots
		self.two_wheeler_slots= two_wheeler_slots
		

	def vehicle_entry():
		print('is it a :\n 1. two wheeler \n 2.four wheeler')
		vehicle_entry =int(input('choose option:'))
		
		if vehicle_entry == 1:
			self.two_wheeler_slots=self.four_wheeler_slots -1
			print(two_wheeler_slots)

		elif vehical_entry == 2 :
			self.four_wheeler_slots= self.four_wheeler_slots -1
			print(four_wheeler_slots)

		def vehicle_exit():
			print('exit :\n 1. two wheeler 2. four wheeler')
			exiting = int(input('choose option: '))
			
			if exiting == 1:
				self.two_wheeler_slots=self.two_wheeler_slots + 1
				print(two_wheeler_slots)

			elif exiting == 2:
				self.four_wheeler_slots=self.four_wheeler_slots + 1
				print(four_wheeler_slots)

	


	while True:
		print('Welcome to S&s mall \n 1. enter \n2. exit')

		inp=int(input('what do u want to do?:'))
		
		if inp== 1:
			lisenceno=input('Vehicle number:')
			vehicle = Parking()
			vehicle.vehicle_entry()

		elif inp == 2 :
			vehicle.vehicle_exit()
			print(startTime)
			time_taken= str(datetime.now() - startTime)
			print(time_taken)
			a = '1:00:00.0000'			
			b = '3:00:00.0000'
			c = '12:00:00.0000'  
			if time_taken <= a:
				print('Please pay 30 ruppes for 1 hour or less')
			elif time_taken >= b:	
				print('Please pay 80 ruppes for 3 hours or more') 
			elif time_taken>= c:
				print('Please pay 120 ruppes for 12 hours or more')			
		else:
			break	 			


	



		
	



