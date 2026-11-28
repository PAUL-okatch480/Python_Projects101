#lists
students=["Wanyoike","Peter","Paul", "Omondi","Kelvin"]
for student in students:
    print(student)

if "Paul" in students:
    print("Paul Okatch has been nominated as the student of the year.")
    print("This follows his excemplary performance in the previous sem 1 exam.")
else:
    print("Peter is the student of the year!")
numbers=[1,2,3,4,5,6,7,8,9]
for i in range (len(numbers)):
    numbers[i]=numbers[i] * 2

print(numbers)

range_list= list(range(0,13))
print(range_list)