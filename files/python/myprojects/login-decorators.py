def login(x):
    def wrapper():
        print("Login")
        x()
        if y != "":
            print("Hello, world!")
        
        else:
            print("Do the login")

    return wrapper


@login
def inputname():
    global y
    y = input("Type your name: ")

inputname()

