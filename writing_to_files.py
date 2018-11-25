print("================Writing to Files================")


employee_file = open("employees.txt", "a") #opens in append mode to add onto the end of the file

employee_file.write("\nKelly - Customer Service") #\n creates a new line!

employee_file.close()

employee_file = open("employees1.txt", "w") #opens in append mode to add onto the end of the file

employee_file.write("\nKelly - Customer Service") #\n creates a new line!

employee_file.close()


print("================Writing to Files================")
