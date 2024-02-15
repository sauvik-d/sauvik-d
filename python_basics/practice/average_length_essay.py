import string

input_string = input("Enter the string: ")
new_string = input_string.translate(str.maketrans('', '', string.punctuation))
number_of_words = len(new_string.split())
count = 0
for i in new_string:
    if(i != ' '):
        count = count + 1


average = round(count / number_of_words)
print(average)
