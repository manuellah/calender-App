import sys

class Calender(object):
	"""
		Calender App to keep track of events on their calendar.
	"""
	def __init__(self, name):
		self.name = name
		self.event_dict = {}

	def addEvent(self):
		#Function to add events to the calender
		date =  input("Enter Date of the Event")
		name =  input("Enter Name of the Event")
		time =  input("Set Time of the Event")
		date_time = (date, time)
		event_dict[date_time] = name

	def view_LastEvent(self):
		#Function to view LastEvent on the calender
		pass
		
	def list_AllEvents(self):
		#Function to view all events on the calender
		for key, value in event.items() :
			print (key, value)
		
	def new_command(self):
		cmd = input('Enter a command')
		cmd = cmd.upper()

		if cmd in ['ADD', 'LIST_LAST', 'LIST_ALL', 'N']:
			if method == 'ADD':
				user.addEvent()
			elif method == 'LIST_ALL':
				user.list_AllEvents()
			elif method == 'LIST_LAST':
				user.view_LastEvent()
			elif method == 'N':
				sys.exit()

		else:
			print 'Invalid command ', cmd



if __name__ == "__main__":
	Calender(sys.argv[1]).new_command()
