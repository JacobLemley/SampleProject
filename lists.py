lucky_numbers = [4,8,15,16,23,42]
friends = ["a","b","Jim","Jim","Jim","d","e"]

print(friends)

friends.extend(lucky_numbers)
print(friends)

friends.append("creed")
print(friends)

friends.insert(1, "Kelly")
print(friends)

friends.remove("Jim")
print(friends)

friends.pop()
print(friends)

print(friends.index("Kelly"))

print(friends.count("Jim"))

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)

friends.clear()
print(friends)
