from facial_req import facial_req
from send_email import send_email

import datetime

complete_names = ['Alice', 'Bob', 'Charlotte', 'David', 'Elliot', 'Fiona']

start_time = ['9:00', '10:15', '11:30', '12:45', '13:30', '14:40']

currentDT = datetime.datetime.now()

while True:
	currentDT = datetime.datetime.now()
	time = str(currentDT.hour) + ':' + str(currentDT.minute)

	if time in start_time:
		present_names = facial_req()
		type = 'Present'
		send_email(present_names, type)

		tardy_names = facial_req() 
		type = 'Tardy' 
		send_email(tardy_names,type)
		absent_names = [] 

		for name in complete_names:
			if name in present_names or name in tardy_names:
				pass
			else:
				absent_names.append(name) 

		type = 'Absent' 
		send_email(absent_names)