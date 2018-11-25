print("=========================================")

for letter in "Giraffe Academy" :  #for each letter in "giraffe academy" :
    print(letter)

friends = ["Jim", "Karen", "Kevin"]
# len(friends) is the length of the array!

for friend in friends :         # the friend variable can be named anything!
    print(friend)

for index in range(3, 10) :        #print all numbers from 3 to 10 (not including 10!)
    print(index)

for index in range(len(friends)) :  #range is 0 to the length of array
    print(friends[index])

for index in range(5) :
    if index == 0 :
        print ("first iteration")
    else :
        print(index)

print("=========================================")
