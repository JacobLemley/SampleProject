#dictionaries use key, value pairs

# lets make a programe for converting abreviated months to full names
# Jan -> January

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    2 : "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",

}

print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Bullshit", "Not a valid key"))
