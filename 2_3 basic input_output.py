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

## got bored and decided to have a little fun with it. textbook only had the above commented out code section which only printed the wage. 2.3.14 uses a simple version of this minus the function
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

## since i am done with this i am hard coding a value to not have to continue to input values every time i want to check the other print statements
##input_wage = int(input("Please enter your wage: "))
input_wage = 35
wage_calculator(input_wage)

print("****************************************")

num_fruit_types = 2
num_apples = 3
num_bananas = 5
print("Number of apples", num_apples)
print(f"I have {num_fruit_types} types of fruit") ## this section does not allow print formatting in the textbox. use normal print
print(num_apples,"apples and", num_bananas, "bananas")
print("I have:\n", num_apples, "apples") ## note \n command to print in new line was not mentioned until 2.3.9... kind of backwards here
print("****************************************")

pet ='dog'
pet_name = "Gerald"
age = "22"
print("You are", age, "years old.") ## answer to 2.3.7 textbox 1
print(pet_name, 'the', pet, 'is', age) ## answer to 2.3.7 textbox 2
print("****************************************")

##end='' extends the print statement because a single print prints on new lines.
# take this logic and based on output ran and answer 2.3.8 that has different prompt. the idea is the same
print("Hello there.", end=" ")
print("My name is...", end=" ")
print("Carl?")
print("****************************************")

## 2.3.9 newline in print statements
## \t is tabbing -- mentioned in the text above but i am totally not reading it
print('Name\tJob\n-------------')
print("Ann\tDeveloper\nJoe\tInfluencer")
print("****************************************")
## 2.3.10 - output simulator
country_name = "China"
print("The population of", country_name, "was 1.34 billion in 2021") ## prints one line
print("The population of", country_name, "in 2021:\n1.34 billion") ## prints two lines

print("****************************************")
##2.3.2 answers are simple keep the new line at the end of the output answers if you need to see it, copy code and paste.


#2.3.3: Read user input and print to output.
num1 = int(input("input a number: "))
num2 = int(input("input another number: "))

""" Your solution goes here """
num3 = int(input("do it again: "))
output = num1 * num2 * num3
print(num1,"*",num2, "*", num3, "=",output) ## answer is just output but for readability


print("****************************************")
#2.3.4 is a just a basic leet code style mini quiz - follow the instructions, it may be copy paste or not... lol
# 1
num_oranges = int(input('how many oranges do you have:')) ## when executing the line it needs readability so input a message for the user
print("oranges:", num_oranges)

print("****************************************")
#2
print("n   n")
print("nnnnn")
print("n   n")
print("nnnnn")
print("n   n")

print("****************************************")
#3 you're just forming a string with input don't forget the period.
num_cucumbers = int(input('how many cucumbers do you have:')) ## again this is for readability if coding side by side
print("My recipe needs", num_cucumbers, "cucumbers.")
print("****************************************")
#4 for me its taking in input
num_lemons = int(input("how many lemons did you buy:"))

print("Leo sold me", num_lemons, "+ 8 lemons, so", num_lemons + 8, "lemons.")

print("****************************************")
#5 it wanted me to assign inputted integers to 4 variables added prompts for the input request for readability.
side1 = int(input("side1:"))
side2 = int(input("Side2:"))
side3 = int(input("Side3:"))
side4 = int(input("Side4:"))
sum_of_sides = side1 + side2 + side3 + side4
print(sum_of_sides)
