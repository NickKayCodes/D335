wage = 36.2
hours = 40
weeks = 50
salary = wage * hours * weeks
print(f"wage: {wage}, hours: {hours}, salary: {salary}")

wage = 62
hours_worked = 80
weeks = 52
normal_weekly_pay = hours * wage
overtime_hours = hours_worked - hours
overtime_pay = (wage * 1/2)+ (wage*hours)
total_pay = normal_weekly_pay + overtime_pay
print("Salary is:", salary)
print("weekly pay:", normal_weekly_pay)
print("overtime payed:", overtime_pay)
print("total pay:", total_pay)
