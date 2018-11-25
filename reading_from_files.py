print("================Reading From Files================")


employee_file = open("employees.txt", "r") #name of file  , read mode (w is write, a is append, r+ is read and write)

print(employee_file.readable()) #checks if the file is readable (boolean value)
print("-------------------------------")

#print(employee_file.read())
#print("-------------------------------")

#print(employee_file.readline())
#print("-------------------------------")

#print(employee_file.readlines()[1]) #turns each line into an index in an array
#print("-------------------------------")

#for employee in employee_file.readlines() :
    print(employee)
#print("-------------------------------")

employee_file.close() #always make sure to close your files after you're done!


print("================Reading From Files================")
