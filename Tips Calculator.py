# Get user's input
bill = float(input("Enter the bill amount: $"))
tip_percentage = float (input("Enter the percentage of tips (e.g. 10%), "))
people = int(input("How many people on splitting the bill? "))

# Calculate the splitting amount
tip_amount = bill * (tip_percentage /100)
total_bill_amount = tip_amount + bill
if people == 0:
 print("Number of people can not be zero")
elif people > 0:
 amount_per_person = total_bill_amount / people


# Delivery the results
print (f"Original bill amount is {bill:.2f} ")
print (f"Tip({tip_percentage}%):  ${tip_amount:.2f}")
print (f"Total Bill amount is ${total_bill_amount:.2f}")
print (f"Each people pay: ${(total_bill_amount / people):.2f}")