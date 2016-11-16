import sys

class Calender(object):
	"""
		Calender App to keep track of events on their calendar.
	"""
	def __init__(self):
		self.events_dict = {}

	def addEvent(self):
		#Function to add events to the calender
		date =  str(raw_input("Enter Date of the Event  "))
		name =  str(raw_input("Enter Name of the Event  "))
		time =  str(raw_input("Set Time of the Event  "))
		date_time = (date, time)
		self.events_dict[date_time] = name
		self.new_command()

	def view_LastEvent(self):
		if not self.events_dict:
			print "NO ITEM"
			return
		#Function to view LastEvent on the calender
		key_container = self.events_dict.keys()

		key_container.sort()
		last =  key_container[-1]
		t = tuple(last)
		description = self.events_dict[t]
		print "Event {} on date {} Time {}".format(description, last[0], last[1])
		self.new_command()

		
	def list_AllEvents(self):
		#Function to view all events on the calender
		for key in self.events_dict:

			print "Event {} on date {} Time  {}".format(self.events_dict[key], key[0], key[1])
		self.new_command()

		
	def new_command(self):
		print '===='* 30
		print "\n\nEnter a command , list of commands are: ADD -> add, LIST_ALL -> To list all, LIST_LAST -> to list last event and N to exit (Case not sensitive) "
		print "ADD -> add, LIST_ALL -> To list all, LIST_LAST -> to list last event and N to exit (Case not sensitive) \n"
		cmd = raw_input()
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

