import sys

class Calender(object):
	"""
		Calender App to keep track of events on the calendar.
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
		#Function to view LastEvent on the calender
		if not self.events_dict:
			print "No Available Items"
			self.new_command()
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
		# Commandline logic
		print '===='* 20
		print "\n\nPlease enter a command to continue:"
		print
		print "Here is a list of available commands:(Case not sensitive)"
		print "0. HELLO"
		print "1. ADD EVENT : To add an event"
		print "2. LIST ALL  : To list all"
		print "3. LIST LAST : To list last event"
		print "4. EXIT      : To exit \n"
		
		cmd = raw_input()
		cmd = cmd.upper()

		if cmd in ['ADD EVENT', 'LIST LAST', 'LIST ALL', 'EXIT', 'HELLO']:
			if cmd == 'HELLO':
				print 'Hi, and Welcome, To start here is a list of all your events!'
				print
				if self.events_dict == {}:
					print "Congradulations, your event list is Empty!"
					self.new_command()
				else:
					self.list_AllEvents()
			if cmd == 'ADD EVENT':
				self.addEvent()
			elif cmd == 'LIST ALL':
				if self.events_dict == {}:
					print "Congradulations, your event list is Empty!"
					self.new_command()
				else:
					self.list_AllEvents()
			elif cmd == 'LIST LAST':
				self.view_LastEvent()
			elif cmd == 'EXIT':
				print
				answer = raw_input("Are you sure?(yes/no) ")
				while answer in ['no', 'yes']:
					if answer == 'no':
						self.new_command()
					if answer == 'yes':
						print "Goodluck today, Bye!"
						print
						sys.exit()
				else:
					print 'Invalid command, please try again!'
					self.new_command()

		else:
			print 'Invalid command, Please check below for available commands and try again!'
			self.new_command()





if __name__ == "__main__":

	Calender().new_command()

