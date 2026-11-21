#string methods such as upper, lower, title, and strip are very useful for manipulating strings in python
#concatenation
string1 = "Hello"
string2 = "World"
result = string1 + " " + string2
print(result)

#string replication
string3 = "Python "
replicated_string = string3 * 3
print(replicated_string)
#slicing 

string4 = "Python is a powerful programming language"
sliced_string = string4[10:20]
sliced_string = sliced_string.upper()  # Convert the sliced string to uppercase
print(sliced_string)
sliced_string = sliced_string.strip()  # Remove any leading or trailing whitespace
print(sliced_string)
sliced_string = sliced_string.title()  # Convert the string to title case
print(sliced_string)

sentence ="Searching for a specific keyword in this sentence"
index= sentence.find("keyword")
print(index)

#replace keyword
original_text= "Python is a powerful programming language"
new_text = original_text.replace ("powerful", "versatile")
print(new_text)

#The strip keyword
raw_input= "      This is a sentence with spaces.       "
stripped_input = raw_input.strip()
print(stripped_input)

#capitalize keyword
original_string = "hello world"
capitalised_string = original_string.capitalize()
print(capitalised_string)

#the lower keyword
original_string = "HELLO WORLD"
lowercase_string = original_string.lower()
print(lowercase_string)


#string manipulation
growth_rate=5.67
continental_region = "Africa"
print("The growth rate in {} is {:.2f} %".format(continental_region, growth_rate))

#Use of fstrings also apply
print(f"The growth rate in {continental_region} is {growth_rate:.2f} %")


