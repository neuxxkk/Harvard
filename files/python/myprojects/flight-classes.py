class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = [] #Is saying that passenger is a list "["

    def add_passenger(self, name):
        if not self.open_seats(): # = if open_seats==0
            return False #You could also say: No avaible seats.
        self.passengers.append(name)
        return True #You could also said: Added name succsefully.

    def open_seats(self):
        return self.capacity - len(self.passengers) # = 3 - number of passengers

flight = Flight(3) #Thats mean "capacity" is equal 3

people = [] #passengers names, every name is gone to be account

who = input(f"Press enter and type who is going to fly, one by one!") #passengers names, every name is gone to be account
    
a = input("The first person is: ")
people.append(a)
b = input("The second person is: ")
people.append(b)
c = input("The third person is: ")
people.append(c)

more = input("Do you like to add someone more?(y/n) ")

if more == "y":
    d = input("The fourth person is: ")
    people.append(d)

    e = input("The fifith person is: ")
    people.append(e)

    f = input("The sixth person is: ")
    people.append(f)

    todos = [a,b,c,d,e,f]
else:
    todos = [a,b,c]

for cada in todos:
    if not cada:
        people.remove(cada)
    else:
        True


for person in people: #For it person in people ||
    succses = flight.add_passenger(person) #Add a passenger in flight(flight==3)
    if succses: # = if flight => len(self.passenger)
        print(f"Added {person} to flight succesfully.")
    else: # = if flight < len(self.passenger)
        print(f"No available seats for {person}")