# dic = {
#     344: "Apoorv",
#     85: "Neha",
#     86: "sahil",
#     1212: "Harry"
# }

# print(dic[85])

info = {'name':'Apoorv', 'age':19, 'eligible':True}
# print(info)
# print(info.keys())
# print(info.values())

# for key in info.keys():
#     print(f"The value of corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
     print(f"The value of corresponding to the key {key} is {value}")

