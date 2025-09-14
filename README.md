Day 2 

Subscript - Pulling out a specific character from a set of strings is called substring
Eg - print("Hello" [4])
>o
The counting should always begin with zero

Integer datatype
For integer concatenation we can directly use the + sign without using "" 
Eg - print(123+345)
>468

Float datatype/ Floating point number
While using a value that has decimal value we cannot use the int function so we can use the float datatype 

Boolean datatype 
It has only two values True & False

we cannot use the len function with int datatype it can only be used with string datatype
Also we cannot concatenate strings and integers together while using print function

Type() function
This function is used to check the datatype of the input function stored by a variable name

Program to add two numbers
two_digit_number = input("Enter a two digit number\n")
first_number = two_digit_number[0]
second_number = two_digit_number[1]
result = int(first_number) + int(second_number)
print(result)

Mathematical operators
Priority order follows PEMDAS
() Parenthesis
** Exponential - 2**3 raise to
* Multiplication
+ Addition
- Subtraction

#Program to calculate the bmi of user
print("Welcome to BMI Calculator")
print("Hello " + input("What is your name?\n"))
weight = input("What is your weight in kg?\n")
height = input("What is your height in m?\n")
new_weight = int(weight)
new_height = float(height)
bmi = new_weight / (new_height ** 2)
new_bmi = int(bmi)
print(new_bmi)

round() function
Used to round off the obtained output

f-strings
Used to print all datatypes in a single print function 
weight = input("Enter your weight in kg\n")
height = input("Enter your height in m\n")
is_winning = True
print(f"Your weight is {weight} Your height is {height} You are winning is {is_winning}")

#Program that tells us how many days months weeks we have left if we live untill 90 years old.
age = input("What is your current age?\n")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days {weeks_remaining} weeks {months_remaining} months left") 

