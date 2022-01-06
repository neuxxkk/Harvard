houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}

who = input("Who do you wanna to know the Hogwarts house's? ")

if who == "Harry":
    print(f"{who} house is {houses['Harry']}")

if who == "Draco":
    print(f"{who} house is {houses['Draco']}")

if who == "Hermione":
    houses["Hermione"] = "Gryffindor"
    print(f"{who} house is {houses['Hermione']}")

else:
    print("You can just choice: Harry, Draco or Hermione!")
    



