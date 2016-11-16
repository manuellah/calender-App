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
		date =  input(Enter Date of the Event)
		name =  input(Enter Name of the Event)
		time =  input(Set Time of the Event)
		date_time = (date, time)
		event_dict[date_time] = name

	def view_LastEvent():
		#Function to view LastEvent on the calender
		pass
		
	def list_AllEvents():
		#Function to view all events on the calender
		pass


if __name__ == "__main__":
	user = sys.argv[1]
    method = sys.argv[2]
    user = Calender(user)
    method = method.upper()
    if method in [ADD, LIST_LAST, LIST_ALL]:
    	pass
    
