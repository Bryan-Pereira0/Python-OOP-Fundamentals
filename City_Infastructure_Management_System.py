#task1
class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
    def update_owner(self,new_owner):
        self.owner = new_owner
    
car1 = Vehicle("J42H3F", "Truck", "Ronald")
print(f"Owner of {car1.registration_number}: {car1.owner}")
car2 = Vehicle("HHH321", "Sedan", "Jimmy")
print(f"Owner of {car2.registration_number}: {car2.owner}")

car1.update_owner("Michael")
print(f"New owner of {car1.registration_number}: {car1.owner}")
#task2
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0
    def add_participant(self):
        self.participant_count += 1
    def get_participant_count(self):
        return self.participant_count

event = Event("Woodstock", "Aug 15-18, 1969")
print (f"People attending {event.name}: {event.get_participant_count()}")

event.add_participant()
print(f"Participants now attending: {event.get_participant_count()}")