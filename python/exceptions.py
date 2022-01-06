import sys
import os
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

try:
    x = int(input("x "))
    y = int(input("y "))
except NameError:
    print("Error: invalid input.")
#   sys.exit(1)      ---------> to exit of the program
    restart_program()

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    restart_program()

print(f"{x} / {y} = {result}")