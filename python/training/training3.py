list_friends = ["Bitayudh", "Bishanka", "Bamya", "Bathagata"]
print(list_friends)
print(list_friends[2])
print(list_friends[-1])
print(list_friends[1:3])
friends_roll = [707, 702, 735, 719]
list_friends.extend(friends_roll)
print(list_friends)
list_friends.append("Abinash")
print(list_friends)
list_friends.insert(1, "Suvam")
print(list_friends)
list_friends.remove("Abinash")
print(list_friends)
friends_roll.sort()
print(friends_roll)
friends = list_friends.copy()
print(friends)
