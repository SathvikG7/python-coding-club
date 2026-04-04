phonebook = {"sathvik": 1234,
             "muni": 5678,
             "dhanvi": 9101112,
             "anindita": 13141516}

print(phonebook["sathvik"])
phonebook["sathvik"] = 17181920

print(phonebook["sathvik"])

phonebook["ravi"]= 21222324

print(phonebook)

phonebook.update({"amar":12238, "ravi": 99999})
print(phonebook)