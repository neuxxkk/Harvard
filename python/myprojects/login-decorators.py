from time import sleep
def login(x):
    def wrapper():
        while 1:
            print("Login")
            x()
            if y.strip() != "":
                print(f"Hello, {y.strip().title()}!")
                sleep(2)
                break
            
            else:
                print("Do the login")

    return wrapper


@login
def inputname():
    global y
    y = input("Type your name: ")

inputname()


