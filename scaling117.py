#Dictionary
my_data={ "Name":"Paul Okatch", "Age":24, "Country":"Kenya", "School": "Alx Africa","Course":"Computer Science",
         "Admission Number":"S13/04423/24", "Year of study":3  }
my_data["Email"]="okatchpaul22@gmail.com"

for k, v in my_data.items():
    print(k,v)

employees=[]
fname, lname = input("Enter you first and lname : ").split()
employees.append ({'fname': fname, 'lname': lname})

print(employees)

#create a customer list
customers = []

while True:

    createEntry = input("Enter customer (yes/no): ").lower()

    if createEntry == "no":
        break

    fname1, lname1 = input("Enter customer name: ").split()

    customers.append({
        'fname1': fname1,
        'lname1': lname1
    })

# Print customer data
for cust in customers:
    print(cust['fname1'], cust['lname1'])
#recursion