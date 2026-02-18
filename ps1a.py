'''
Assignment 1 part A
Name:  B naga maheswar reddy
prn : 250200007
application :CDS/2025/1864
Collaborators: P shashank
'''
# take inputs from user
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

# down payment is 25% of total cost
down_payment = 0.25 * total_cost

# initial savings
current_savings = 0

# annual return is 4%
r = 0.04

# month counter
months = 0

# loop until savings reach down payment
while current_savings < down_payment:
    # monthly interest added
    current_savings += current_savings * (r / 12)

    # monthly salary saving added
    current_savings += (annual_salary / 12) * portion_saved

    # increase month count
    months += 1

# print result
print("Number of months:", months)
