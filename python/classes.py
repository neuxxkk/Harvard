class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

    def sum(self):
        r = self.x + self.y
        return r
 
p = Point(2, 8)
print(p.x)
print(p.y)
print(f'Sum of {p.x} and {p.y} is {p.sum()}')