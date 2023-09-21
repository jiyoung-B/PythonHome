myString = "This is a string"
print(myString)
print(type(myString))
print(myString + "is of the data type" + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

# f-string
# 버전1
name = input("What is your name? ")
print(name)
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name,color,animal))

# 버전2
name = "Michael"
age = 24
print("Name is " + name + ", Age is " + str(age))
print("Name is %s, Age is %d" % (name, age))
# 버전3
print(f"Name is {name:10s} , Age is {age:5d}.")
