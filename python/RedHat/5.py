a, b = [set('efgy'), set('exyz')]
# union
print(a | b)
print(a & b)
print(a - b)
print(b - a)
# symmetric difference
print(a ^ b)
fruits = {
    "a": "Apples",
    "b": "Bananas"
}

fruits["s"] = "Strawberries"
print(fruits)
value = fruits["a"]
print(value)
reward_pts = {
    "Bryce": 500,
    "Heather": 2000,
    "Kaylie": 750,
}
points = reward_pts.get("Bryce")
new_point = reward_pts.get("Stephanie", 0)
print(new_point)
print(reward_pts)
unknown = "Make is Unknown"
cars ={
    'Mustang': 'Ford',
    'Falcon': 'Ford',
    'Camaro': 'Chevy',
    'Corvette': 'Chevy',
    'Eclipse': 'Mitsubishi',
    'Integra': 'Acura'
}
make = cars.pop("Corvette")
print(make)
make = cars.pop("Accord", unknown)
print(make)
a_tuple = cars.popitem()
print(a_tuple[0], a_tuple[1])
model, make = cars.popitem()
print(model, make)
print(cars)
numbers = [3, 1, -10, 54, 75, 29]
words =["Hello", "Goodbye", "goodbye", "hello"]
label1, label2 = ("Unsorted: ", "Sorted: ")
numbers.sort()
words.sort()
print(numbers)
print(words)
numbers.sort(reverse=True)
words.sort(reverse=True)
print(numbers)
print(words)
originals = [[3, 1, -10, 54, 75, 29],
             ("Cheese", "Pepperoni", "Bacon", "Mushrooms"),
             {"AL", "NY", "MD", "VA", "PA", "KY", "VT"},
             {'New Hampshire': 'NH', 'Maryland': 'MD',
              'Nevada': 'NV', 'Maine': 'ME'}]
for collection in originals:
    print(collection)
print()
for collection in originals:
    sorted_list = sorted(collection)
    print(type(collection).__name__, "sorted:", sorted_list)
names = """Smith Johnson Williams Brown Jones Miller Lee Garcia Rodriguez Wilson Martinez Anderson Taylor Thomas Hernandez Moore Martin Jackson Thompson White Lopez Davis"""
names = names.split()
names.sort()
print(names)
names.sort(key=len)
print(names)


def the_last_word(a_string):
    fmt = "For Input: {:18}    Sort Using: {}"
    last_word = a_string.strip().split()[-1]
    print(fmt.format(a_string, last_word))
    return last_word


names = """Ava Smith, Ethan Johnson, Abigail Williams, ,Sophia Brown, Michael Jones, Emily Miller, Declan Lee"""
names = names.split(", ")
print(names)
names.sort(key=the_last_word)
print(names)


def get_value(akey):
    return states[akey]


states = {'New Hampshire': 'NH', 'Maryland': 'MD',
          'Nevada': 'NV', 'Maine': 'ME'}
long_names = list(states.keys())
long_names.sort(key=get_value)
for name in long_names:
    print(name, states[name])
print()
long_names = list(states.keys())
long_names.sort(key=states.get)
for name in long_names:
    print(name, states[name])
print()
