# f = open('readfile.txt', 'r')
# i = 0

# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Marks of student {i} in Maths is {m1*2}")
#     print(f"Marks of student {i} in English is {m2*2}")
#     print(f"Marks of student {i} in SST is {m3*2}")
#     print(line)

f = open('readfile2.txt', 'w')

lines = ['line 1\n', 'line 2\n', 'line 3\n']

f.writelines(lines)
f.close()