a = [23, 76, 546, "Slavia", "Skoda", -98, 765.65]

# Iterate by index/position

for i in range(0, 7):
    print(a[i])


x = len(a)
print(x)
# or we will write this also
for i in range(len(a)):
    print(a[i])

a = [43, 65, 43, "Mahindra", "Scorpio", 45, 64, 65, 87, 99, 76]
b = [43, 667, 876, 66, 555, "VW", "Virtus", 908, 879, 787, 883]

for i in range(len(a), len(b)):
    print(a[i], b[i])
