list_literal = [6, 4, 2]
list_literal.append(12)
list_literal.append(8)
list_literal.append(4)
print(list_literal)
list_literal[1] = 3
print(list_literal)
# sorting list
x = [(3, 6), (4, 7), (5, 9), (8, 4), (3, 1)]
x.sort()
print(x)
# range function
list_range = list(range(1, 1000))
print(list_range)
min_value = min(list_range)
max_value = max(list_range)
print(min_value)
print(max_value)
list_even = []
list_odd = []
for i in range(0, len(list_range)):
    if list_range[i] % 2 == 0:
        list_even.append(list_range[i])
    else:
        list_odd.append(list_range[i])

print(list_even)
print(list_odd)
# Dictionary Exercises
internet_terms = {
    "BTW": "By the Way",
    "iykyk": "If you know you know",
    "thnx": "Thanks",
    "lol": "Laughing out Loud",
    "OG": "Oh God!",
    "B": "Member of B company",
}
print(internet_terms)

