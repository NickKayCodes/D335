print("Hello there.")
print("Hello \n"
      "again.")
print("My name is....")
print("Carl?")

# Complete the program with five print statements to output the following figure with asterisks.
# *****
# *   *
# *****
# *   *
# *****

print("*****")
print("*   *")
print("*****")
print("*   *")
print("*****")

## 2.3.4 printing variables and multiple values
# wage = 400
# print("Your daily wage is $", wage)
#
# weekly_wage = 7*wage
# print("Your weekly wage is $", weekly_wage)
#
# bi_weekly_wage = 2*weekly_wage
# print("Your bi-weekly wage is $", bi_weekly_wage)
#
# monthly_wage = 4*weekly_wage
# print("Your monthly wage is $", monthly_wage)
#
#
# yearly_wage = 12*monthly_wage
# print("Your yearly wage is $", yearly_wage)
#
# print("****************************************")
# print("Your yearly wage is $", yearly_wage, "\nWhich consists of 12 monthly payments of", monthly_wage)


def wage_calculator(wage):
      print("Your daily wage is $", wage)

      weekly_wage = 7 * wage
      print("Your weekly wage is $", weekly_wage)

      bi_weekly_wage = 2 * weekly_wage
      print("Your bi-weekly wage is $", bi_weekly_wage)

      monthly_wage = 4 * weekly_wage
      print("Your monthly wage is $", monthly_wage)

      yearly_wage = 12 * monthly_wage
      print("Your yearly wage is $", yearly_wage)

      print("****************************************")
      print("Your yearly wage is $", yearly_wage, "\nWhich consists of 12 monthly payments of", monthly_wage)

input_wage = int(input("Please enter your wage: "))
wage_calculator(input_wage)

print("****************************************")

num_fruit_types = 2
num_apples = 3
num_bananas = 5
print("Number of apples", num_apples)
print(f"I have {num_fruit_types} types of fruit")
print