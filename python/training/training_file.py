# this means read the file
pythontest_file = open("pythontest.txt", "r")

# print(pythontest_file.readlines())
# comment the line before it to use the next one
# print(pythontest_file.readlines()[1])

for fileprint in pythontest_file.readlines():
    print(fileprint)
pythontest_file.close()
