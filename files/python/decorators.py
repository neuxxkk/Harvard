def announce(x):
    def wrapper():
        print("New function comming soon")
        x()
        print("Done!")
    return wrapper
            

@announce # Instead (x) is (hello)
def hello():
    print("Hello, world!")

hello()