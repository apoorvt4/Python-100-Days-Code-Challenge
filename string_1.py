# String are Immutable
a = "Apoorv @@@@ @@@ @@@@@ @@ Apoorv @@@@@@@ Tiwari"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("@"))
print(a.replace("Apoorv", "Harry"))
print(a.split(" "))
blogHeading = "introduCtion tO pythOn"
print(blogHeading.capitalize())

str1 = "Welcome to the console!!!"
print(len(str1))
print(str1.center(50))

print(a.count("Apoorv"))

str2 = "Welcome to console@@@"
print(str2.endswith("@@@"))

str2 = "Welcome to console@@@"
print(str2.endswith("to", 4, 10))

str2 = "He's name is Dan He is an honest man"
print(str2.find("is"))
#print(str2.index("is"))

str2 = "WelocmeToTheConsole"
print(str2.isalnum())
str2 = "WelocmeToTheConsole00"
print(str2.isalpha())
str2 = "WelocmeToTheConsole"
print(str2.title())
str2 = "WelocmeToTheConsole"
print(str2.swapcase())