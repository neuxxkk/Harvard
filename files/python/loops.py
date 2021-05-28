print("# Manual list add\n")
for i in [0, 1, 2, 3, 4, 5]:
    print(f"{i}","\n"*2)
    

print("# Range list add\n")
for i1 in range(6):       # If u have a huge number this will be useful
    print(f"{i1}","\n"*2)


print("# Looping list of 'str'\n")
names = ["Harry", "Ron", "Hermione", "Ginny"]

names.append("Draco")

names.sort()

for name in names:       # Each name in my list of names lets print out yhis list
    print(f"{name}","\n"*2)
    

print("# Looping characters of a str\n")
name = "Harry"

for character in name:
    print(f"{character}","\n"*2)
