# append file
file_point = open("pythontest.txt", "a")
file_point.write("\n")
file_point.close()


# writing in html
html_point = open("pytest.html", "w")
html_point.write("<p>This is writing in HTML using Python</p>")
html_point.close()
