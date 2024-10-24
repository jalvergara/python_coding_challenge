import pandas as pd

n = [3, 2, 1, 0]

u = 0

file = open("holamundo.txt","w")

for i in n:
    u+=1
    print(u)
    u_str = str(u)
    file.write(u_str)
    if u >= 2:
        print("hola mundo")
        break


number_whatever = "111111"

int_number = int(number_whatever)

print(int_number)