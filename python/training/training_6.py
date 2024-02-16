# while loop
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")
# guessing game
secret_word = "Master"
guess = ""
while guess != secret_word:
    guess = input("Enter guess word: ")

print("Guessed successfully")
# for loops
for letter in "Vikram":
    print(letter)
my_list = ["Polladhavan", "Aadukalam", "Asuran", "Vidhuthalai"]
for cinema in my_list:
    print(cinema)


for index in range(3, 10):
    print(index)
for index in range(len(my_list)):
    print(my_list[index])

