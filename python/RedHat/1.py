x = 4
y = 5
# floored quotient
print(y // x)
print(divmod(y, x))
x = 0xff
print(x)
# sep and end uses in print function
print("Sauvik Dutta", "Roll No", "720", sep=":", end=".")
print("Go\rRun")
print("Go\aRun")
print("Go\bRun")
print("Go\fRun")
print("Go\vRun")
print("GoRun")
print("\U0001F0A1")
print("\U0001F0CE")
str_test = "Oppenheimer"
print(str_test.startswith("Oppen"))
print(str_test.endswith("eimer"))
print(str_test.upper())
# checks whether string is fully literal or not
print("abcd123".isalpha())
# checks full numeric or not
print("12345".isnumeric())
# checks whether all characters are made with alphanumeric characters or not
print("1244".isalnum())
# string replace search and split
word = "is"
sentence = "The name is Sauvik Dutta and he is a Student."
position = sentence.find(word)
print(position)
print(sentence.find(word, position + 1))
print(sentence.find(word, 8, 12))
print("The word appears in sentence", sentence.count(word), "times.")
# these methods return a string of parameter given length after substituting the give parameter character
print(word.rjust(15))
print(word.ljust(15, "*"))
data = "1 3 2 1 1 4 2 3 2abc"
print(data.replace("1", "0"))
# previous was to replace all 1's and this is to replace only two 1's
print(data.replace("1", "0", 2))
# splitting
pieces = data.split(' ')
print(pieces)
print(type(pieces))

