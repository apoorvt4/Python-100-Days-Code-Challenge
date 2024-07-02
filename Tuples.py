tup = (1,2, 5, 77, 342, 32, "Green", True)
print(type(tup), tup)
# tup[0] = 99
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[-1])
print(tup[4])
print(tup[5])

if 342 in tup:
    print("yes")

tup2 = tup[1:4]
print(tup2)