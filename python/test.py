def test(x):
    def one():
        print("oi")
        x()
    return one
    

@test
def ine():
    print("vitor")

ine()