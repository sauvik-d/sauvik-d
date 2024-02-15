file_name = "test.txt"
with open(file_name) as f:
    content = f.readline()

print(content)

infile = open(file_name, 'r')
data = infile.read()
infile.close()

print(data)

infile_new = open("does_not_exist.txt", "r")
data_new = infile_new.read()
infile_new.close()

print(data_new)
