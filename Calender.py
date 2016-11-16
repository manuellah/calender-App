import sys

class Calender(object):
	"""
		Calender App to keep track of events on their calendar.
	"""
	def __init__(self):
		self.events_dict = {}

	def addEvent(self):
		#Function to add events to the calender
		date =  input("Enter Date of the Event")
		name =  input("Enter Name of the Event")
		time =  input("Set Time of the Event")
		date_time = (date, time)
		events_dict[date_time] = name

	def view_LastEvent():

		#Function to view LastEvent on the calender
		key_container = self.events_dict.keys()
		key_container.sort()
		last = key_container(len(key_container) - 1) 

		description = events_dict[last]
		print "Event {} ondate {} Time".format(description, last[0], last[1])

		
	def list_AllEvents(self):
		#Function to view all events on the calender
		for key in self.events_dict:

			print (key, self.events_dict[key] )

		
	def new_command(self):
		cmd = raw_input('Enter a command')
		print cmd
		cmd = cmd.upper()
		print cmd

		if cmd in ['ADD', 'LIST_LAST', 'LIST_ALL', 'N']:
			if cmd == 'ADD':
				self.addEvent()
			elif cmd == 'LIST_ALL':
				self.list_AllEvents()
			elif cmd == 'LIST_LAST':
				self.view_LastEvent()
			elif cmd == 'N':
				sys.exit()

		else:
			print 'Invalid command ', cmd




if __name__ == "__main__":

	Calender().new_command()

