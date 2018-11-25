#I'm at a restaurant
#If I want steak
#   I order a steak
#otherwise if i Want pasta
#   I order spaghett
#otherwise
#   I commit suicide

#boolean variable
is_male = False
is_tall = True

#or
if is_male or is_tall :
    print("oi m8 or big lass")
else :
    print("evening wee lass")
print("--------------------------")

#and
if is_male and is_tall :
    print("oi big man")
else :
    print("evening wee lass")
print("--------------------------")

#elif
if is_male and is_tall :
    print("oi big man")
elif is_male and not(is_tall) :
    print("evening wee man")
elif not(is_male) and is_tall :
        print("evening thicc lass")
else:
    print("evening wee lass")
print("--------------------------")

# if statements using comparisons:
# operators : !=, == , >=, <=
def max_num(num1, num2, num3) :
    if num1 >= num2 and num1 >=num3 :
        return num1
    elif num2 >= num1 and num2 >= num3 :
        return num2
    else :
        return num3

print(max_num(3,4,5))
print("--------------------------")
