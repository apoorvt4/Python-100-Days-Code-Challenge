# name = 'Aboorv'
# for i in name:
#     print(i)
#     if(i == "b"):
#         print("this is special")

# colors = ["Red", "Blue", "Green", "Yellow"]
# for colors in colors:
#     print(colors)
#     for i in colors:
#         print(i)

# for k in range(1, 12, 3):
#     print(k)

step = int(input("Enter the step: "))

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in range(0, len(list_1), step):
    print(list_1[i+1])