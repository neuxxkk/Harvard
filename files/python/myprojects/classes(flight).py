class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = [] #Is saying that passenger is a list "["

    def add_passenger(self, name):
        if not self.open_seats(): # = if open_seats==0
            return False #You could also said: No avaible seats.
        self.passengers.append(name)
        return True #You could also said: Added name succsefully.

    def open_seats(self):
        return self.capacity - len(self.passengers) # = 3 - number of passengers

flight = Flight(3) #Thats mean "capacity" is equal 3

people = ["Harry", "Ron","Hermione", "Ginny"] #passengers names, every name is gone to be account

for person in people: #For it person in people ||
    succses = flight.add_passenger(person) #Add a passenger in flight(flight==3)
    if succses: # = if flight => len(self.passenger)
        print(f"Added {person} to flight succesfully.")
    else: # = if flight < len(self.passenger)
        print(f"No available seats for {person}")