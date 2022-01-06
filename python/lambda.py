#INSTEAD THIS
#    ||
#    ||
#    \/                    

#people= [
#    {"name":"Harry", "house":"Gryffindor"},
#    {"name":"Draco", "house":"Slytherin"},
#    {"name":"Cho", "house":"Ravenclaw"}
#]
#
#def f(person):
#    return person["name"]
#
#people.sort(key=f)
#
#print(people)


#DO THIS
#  ||
#  ||
#  \/     

people= [
    {"name":"Harry", "house":"Gryffindor"},                         # Yeah i know, its a kindle of unuseles                             
    {"name":"Draco", "house":"Slytherin"},
    {"name":"Cho", "house":"Ravenclaw"}
]

people.sort(key=lambda person:  person["name"])

print(people)
