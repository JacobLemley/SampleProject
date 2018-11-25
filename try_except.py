print("================Try / Except================")


try:
    value = 10/0
    number = int(input("enter a number: ")) #expects a number
    print(number)
except ZeroDivisionError:       #this is a specific error, this is generally good practice
    print(err)      #prints the actual error
except ValueError:
    print("Invalid Input u cunt")


print("================Try / Except================")
