#Basics:
def say_hi():
    print("hello user")

say_hi()
print("----------------")

#passing in parameters:
def say_hi_names(name):
    print("hello " + name)

say_hi_names("mike")
say_hi_names("steve")
print("----------------")

def say_hi_names(name, age):
    print("hello " + name + " you are " + str(age))

say_hi_names("mike", 70)
say_hi_names("steve", 23)
print("----------------")

#Return Statement in Functions:
def cube(num):
    return num*num*num

print(cube(10))
print("----------------")

def cube(num):
    return num*num*num

result = cube(10)
print(result)
print("----------------")

#anything after the return is never executed
def cube(num):
    return num*num*num
    print("Extremely important code")

result = cube(10)
print(result)
print("----------------")
