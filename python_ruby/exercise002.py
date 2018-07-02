sample_str = "goviNd"

# reverse a string
print ("Reversed string:")
print (sample_str[::-1])

print ("\nString length:")
print (len(sample_str))

print ("\ncapitalized string:")
print (sample_str.capitalize())

print ("\nuppercase")
print (sample_str.upper())
print ("\ndowncase")
print (sample_str.lower())
print ("\nis empty or not")
print (not bool(sample_str and sample_str.strip()))
print ("\nprinting the string three times")
print ((sample_str+" ") * 3)
