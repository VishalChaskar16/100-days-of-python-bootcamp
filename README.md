Day 3

Conditional if else statement - we can use if else statement to print a piece of code based on a condition

Modulo operation - % - It is used to divide 2 numbers to get a remainder

Nested if else statement - Once the first if condition is passed we can add another if statement so this way we can use multiple conditions to identify

Elif statement - We can use it to add multiple conditions at once after the if statement and once all elif conditoons / statements are written we can then use the elif statement

#Rollercoaster age condition program

print("Welcome to my rollercoaster")
height = int(input("What is your height in cm "))

if height > 120:
    print("You can enjoy the rollercoaster")
else:
    print("You need to grow taller to ride the rollercoaster")


Nested if else statement
height = float(input("Enter your height in cm "))
age = int(input("Enter your age "))

if height > 120:
    print("You can ride the rollercoaster")
    if age > 18:
            print("You can ride & You have to pay 12$ ")
    else:
            print("You can ride & You have to pay 7$")
else:
    print("You cannot ride the rollercoaster")

Elif statement
height = float(input("Enter your height in cm "))
age = int(input("Enter your age "))

if height > 120:
    print("You can ride the rollercoaster")
    if age > 18:
            print("You can ride & You have to pay 12$ ")
    elif age < 12:
            print("You can ride and you have to pay 5$")
    elif age >12 <18:
            print("You have to pay 7$")
else:
    print("You cannot ride the rollercoaster")

#BMI 2.0 program

height = float(input("Enter your height in m "))
weight = float(input("Enter your weight in kg "))

bmi = weight / height ** 2
new_bmi = round(bmi)
if new_bmi <18.5 :
    print(f"Your bmi is {new_bmi} , you are underweight")
elif bmi  <25 :
    print(f"Your bmi is {new_bmi} , you have normal weight")
elif bmi <30 :
    print(f"Your BMI is {new_bmi} , you are overweight")
elif bmi <35 :
    print(f"Your BMI is {new_bmi} , you are obese")
elif bmi >35 :
    print(f"Your BMI is {new_bmi} , you are clinically obese")
else :
    print("Invalid input")

#Leap year program
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print(" Not a Leap Year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

Multiple if staetements -  To check if the second condition is true even if the first condition is false 

Rollercoaster program with multiple if statement 
height = int(input("Enter your height in cm "))

if height > 180:
    print("You can ride the rollercoaster")
    age = int(input("Enter your age "))
    
    if age < 12:
        bill = 5
        print("You have to pay 5$ ")

    elif age <18:
        bill = 7
        print("You have to pay 7$ ")

    elif age > 18:
        bill = 12
        print("You have to pay 12$")

    wants_photo = input("Do you want a photo Y or N: ")
    bill += 3

    print(f"Your total bill is {bill}$ ")

else:
    print("You need to grow taller to ride to the rollercoaster")

#Program to calculate pizza charges
print("Welcome to Vishal Pizza hub ")

size = input("What size pizza do you want S M or L ")
add_pepperoni = input("Do you want pepperoni Y or N ")
extra_cheese = input("Do you want extra cheese Y or N ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is {bill}$")

Logical operators and , or , not - 
and → Returns True if both conditions are true, otherwise False.
or → Returns True if at least one condition is true, otherwise False.
not → Reverses the result; returns True if the condition is false, and False if it’s true.

#Program to add an elif statement to make the ride free for people between age 45 - 55
height = int(input("Enter your height in cm "))

if height > 180:
    print("You can ride the rollercoaster")
    age = int(input("Enter your age "))
    
    if age < 12:
        bill = 5
        print("You have to pay 5$ ")

    elif age <18:
        bill = 7
        print("You have to pay 7$ ")
    elif age >=45 and age <=55:
        bill = 0
        print("Have a free ride on us!")

    elif age > 18:
        bill = 12
        print("You have to pay 12$")

    wants_photo = input("Do you want a photo Y or N: ")
    if wants_photo =="Y":
        bill += 3

    print(f"Your total bill is {bill}$ ")

else:
    print("You need to grow taller to ride to the rollercoaster")

##Love calculator program
print("Welcome to My Love Calculator!")
## creating two variables to take name input as string
name1 = input("Enter your name: ")
name2 = input("Enter partners name: ")

##concatenating both strings to make it lower case
combined_string = name1 + name2

## creating a new variable to use the lower() function to convert all string characters to lowercase letters using above concatenated variable
lowercase_string = combined_string.lower()

##using the count() function to count number of times a string letter from word true is repeated in the input variable
t = lowercase_string.count("t")
r = lowercase_string.count("r")
u = lowercase_string.count("u")
e = lowercase_string.count("e")

## concatenating all count() function variable and concatenating them to get the value of the input name
true = t + r + u + e 

##using the count() function to count number of times a string letter from word love is repeated in the input variable
l = lowercase_string.count("l")
o = lowercase_string.count("o")
v = lowercase_string.count("v")
e = lowercase_string.count("e")

## concatenating all count() function variable and concatenating them to get the value of the input name
love = l + o + v + e

## converting the variable datatype from string to integer 
love_score = int(str(true) + str(love))

if (love_score <10) or (love_score >90):
    print(f"Your love score is {love_score}, you both are like coke and mentoes")

elif (love_score >= 40 ) and (love_score <= 50):
    print(f"Your string is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")


Treasure Island game
from turtle import right


print('''
                   ,.ood888888888888boo.,
              .od888P^""            ""^Y888bo.
          .od8P''   ..oood88888888booo.    ``Y8bo.
       .odP'"  .ood8888888888888888888888boo.  "`Ybo.
     .d8'   od8'd888888888f`8888't888888888b`8bo   `Yb.
    d8'  od8^   8888888888[  `'  ]8888888888   ^8bo  `8b
  .8P  d88'     8888888888P      Y8888888888     `88b  Y8.
 d8' .d8'       `Y88888888'      `88888888P'       `8b. `8b
.8P .88P            """"            """"            Y88. Y8.
88  888                                              888  88
88  888                                              888  88
88  888.        ..                        ..        .888  88
`8b `88b,     d8888b.od8bo.      .od8bo.d8888b     ,d88' d8'
 Y8. `Y88.    8888888888888b    d8888888888888    .88P' .8P
  `8b  Y88b.  `88888888888888  88888888888888'  .d88P  d8'
    Y8.  ^Y88bod8888888888888..8888888888888bod88P^  .8P
     `Y8.   ^Y888888888888888LS888888888888888P^   .8P'
       `^Yb.,  `^^Y8888888888888888888888P^^'  ,.dP^'
          `^Y8b..   ``^^^Y88888888P^^^'    ..d8P^'
              `^Y888bo.,            ,.od888P^'
                   "`^^Y888888888888P^^'"
                        
      ''')

print("Welcome to Vishal Treasure Island")
print("Your mission is to find the treasure")

## Creating a variable choice1 that will take the input as 2 choices Left or Right
## Using the \ helps to escape the string in word 'You're' and sees the whole input as text
## Using the lower() function to ensure the input entered by the user is converted to lowercase to avoid error

choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right". ').lower()

## Here instead of using 'right' as Game over we kept it in else statement as blank so that even if the user gives any other response other than left or write it will still give game over as ouput 
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
    if choice2 == "wait":
        choice3 = input("You arrived at the island unharmed. There is a house with 3 doors. One red one yellow one blue. Which color do you choose? ").lower()
        if choice3 == ("red"):
            print("Its a room full of fire. Game over.")
        elif choice3 == ("yellow"):
            print("Its a room full of manhunters. Game over. ")
        elif choice3 == ("blue"):
            print("You found the treasure. You Won!!!")
        else:
            print("You chose a door that doesn't exists. Game over.")

    else:
        print("You got attacked by a zombie. Game over. ")
else:
    print("You fell into a hole. Game over.")
