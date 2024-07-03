# s = {2, 4, 2, 6}
# print(s)

# info = {"Carla", 19, False, 5.9, 19}
# print(info)

# Apoorv = set()
# print(type(Apoorv))

# for value in info:
#     print(value)

# Sets Methods in Python


# s1 = {1, 2, 5, 6}
# s2 = {3, 6, 7}
# print(s1.union(s2))

# s1.update(s2)
# print(s1, s2)
# print(s1)

cities = {"Tokyo", "Madrid", "Delhi", "New York", "Kabul"}
cities2 = {"Tokyo", "Seoul", "Berlin", "Delhi", "Hongkong"}

cities.add("Mumbai")
print(cities)
item = cities.pop()
print(item)

if "Mumbai" in cities:
    print("Mumbai is present")
else:
    print("Mumbai is not present")