stars = "*" * 12
pounds = 5 * "#"
print(stars, ":", pounds)
x = "Hello there"
print('t' in x, 'ell' in x, 'hell' in x)
spam = "Spam and eggs"
delim = "|"
# in [2:7] including from index 2 and excluding from index 7
print(spam[2:7], spam[5:], spam[:8], sep=delim)
# extended slicing
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[2:18:3])
start = 18
print(alphabet[start::1])
print(alphabet[::1])
# slicing from end
print(spam[-3:-1], spam[-3:], spam[:-1], sep=delim)
name = "First Name: {} \t Last Name: {}"
formatted = name.format("Sauvik", "Dutta")
print(formatted)
name = "{1}, {0}"
print(name.format("Sauvik", "Dutta"))
dimensions = "Type: {type}\nHeight:{height}, Width: {width}"
result = dimensions.format(height=60, width=20, type="Box")
print(result)

