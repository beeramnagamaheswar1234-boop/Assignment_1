'''
Assignment 1 part c
Name:  B naga maheswar reddy
prn : 250200007
application :CDS/2025/1864
Collaborators: P shashank
'''
starting_salary = float(input("Enter the starting salary: "))

# constants given in question
total_cost = 1000000
down_payment = 0.25 * total_cost
semi_raise = 0.07
r = 0.04
months = 36

# bisection search limits (0 to 10000 means 0.0000 to 1.0000)
low = 0
high = 10000
steps = 0
best_rate = None

# function to calculate savings in 36 months
def savings_after_36(rate):
    current_savings = 0
    annual_salary = starting_salary

    for m in range(1, months + 1):
        current_savings += current_savings * (r / 12)
        current_savings += (annual_salary / 12) * rate

        # salary raise every 6 months
        if m % 6 == 0:
            annual_salary += annual_salary * semi_raise

    return current_savings


# check if even saving 100% is not enough
if savings_after_36(1.0) < down_payment:
    print("It is not possible to pay the down payment in three years.")
else:

    # bisection search loop
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        rate = mid / 10000

        saved = savings_after_36(rate)

        # check within $100 accuracy
        if abs(saved - down_payment) <= 100:
            best_rate = rate
            break
        elif saved < down_payment:
            low = mid + 1
        else:
            high = mid - 1

    # print results
    print("Best savings rate:", round(best_rate, 4))
    print("Steps in bisection search:", steps)
