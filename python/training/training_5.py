# Dictionary
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])
print(monthConversions.get("Jun"))
print(monthConversions.get("boo"))
print(monthConversions.get("boo", "Not a valid key"))
key_dict = {
    21: "Karthik Subbaraj",
    272: "Kamal Hassan",
    "Visaranai": "Vetri Maaran",
}

print(key_dict.get("Visaranai"))
print(key_dict.get(21))
