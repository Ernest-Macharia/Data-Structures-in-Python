x = [3,6,2,10,7,22,4,9,5]
num = [y if y%2 == 0 else 10 * y for y in x]
print("numbers: " + str(num))