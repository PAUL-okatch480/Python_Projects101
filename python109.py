variable_a= 4.56
variable_b= "123"
#type casting the created variables
variable_a=float(variable_a)
variable_b=int(variable_b)
#sum the results and ouptut it as well as the data type
result= variable_a + variable_b
print(result,":", type(result))

mixed_variable= '42.42'
float_version = float(mixed_variable)
int_version= int(float_version)
#output their separet data types
print(float_version,':', type(float_version))
print(int_version,':', type(int_version))

multiline = '''This is a multiline operation
It allows us to write a number of lines
for the same variable
then we output using the print function
I find it very useful for writing long strings that span multiple lines
'''
print(multiline)
name = "John"
first_character = name[0]
second_character = name[1]
third_character = name[2]
print("first_character:", first_character)
print("second_character:", second_character)
print("third_character:", third_character)

_challenge_string = "Python is a powerful programming language"
print(_challenge_string[2])
print(_challenge_string[5])
print(_challenge_string[10])
print(_challenge_string[15:25])
print(_challenge_string[30:])

#print concatenation is an interesting concept in python, it allows us to combine strings together
string1 = "I am very positive that I will be a great programmer"
string2 = "The results are already showing that I am improving"
string3 ="I will continue with the hard work to achieve my goals"

result = string1 + " " + "\n" + string2 + " " + "\n" + string3
print(result)
