import re


def getinput(regex):
    prompt = "Enter a RegEx or (<enter> to reuse previous):"
    prevregex = regex
    regex = input(prompt)
    if not regex:
        regex = prevregex
    elif regex == "quit":
        return tuple()
    line = input("Enter a string to search: ")
    if line == "quit":
        return tuple()
    return regex, line


def main():
    previous_regex = ""
    print("Enter 'quit' at any time to quit the program")
    while True:
        the_tuple = getinput(previous_regex)
        if the_tuple:
            regex, text = the_tuple
            x = re.search(regex, text)
            if x:
                print(x, "\n")
            else:
                print("No Match found\n")
            previous_regex = regex
        else:
            break

# The span is a tuple of both the start and end positions of the match.
# The re.search() function takes a regex pattern as its first argument
# and the string to search as the second argument.
# Regular expressions are a highly specialized language used for pattern matching.
# By using this language, you can specify the rules for the set of possible strings
# that you want to match, modify, or split.
# The functions in the re module let you check if a particular string matches a given regular expression.
# Special characters, also called metacharacters, are characters that either
# stand for classes of ordinary characters, or affect how the regular expressions around them are interpreted.


if __name__ == "__main__":
    main()

