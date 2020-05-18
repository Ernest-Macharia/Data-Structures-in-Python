#string
x = "bag"
print(sorted(x))

#list
y = ["money", "post", "pricing"]
print(sorted(y))

#tuple
z = ("Ernesto", "Kigo", "Wanjiru")
print(sorted(z))

v = ["money", "past", "post", "pricing"]
print(sorted(v, key=lambda k: k[1]))