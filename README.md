Day 1    12 sep 2025
# Strings - a string is a sequence of characters used to represent text. It is a widely used data type.
Eg - print("Hello World")
"Hello World" is a string of characters

#Different ways of printing string characters 
Using the same print function multiple times
print("Hello World")
print("Hello World")
print("Hello World")

Adding \n method
print("Hello World\n Hello World\n Hello World)
Helps to print multiple string characters using single print statement

#String concatenation - Combining different string characters and merging them into one

print("Hello" + "World)

#Input function
The print function helps to print the string input as output but the user cannot interact or respond to the output
So the Input function helps us do it.

input("What is Your Name? ")
>What is your name?  

# Comments 
By using # we can add notes or info about a particular line of code at any point of the program without it being consdired as a part of the code

#Program that prints no. of characters in a username
print(len(input("What is your name?")))
>Vishal
>6

#Python Variables

name = input("What is your name?")
print(name)

Here name is a variable so we can just use the variable name to print the input. 
Also we can use a variable name without using input function

#Using variable along with len function
name = input("What is your name? ")
length = len(name)
print(length)

To add space to a variable name we can use '_' using a space will give a syntax error

#Band name generator project

print("Welcome to my band name generator!") 
# The print function prints the Welcome message

print("Hello " + input("What is your name?\n "))
#The print function prints a Hello message along with the name of the User by using the input functiom
#The '\n' method helps to print the input message on the next line

city_name = input("What city you grew up in?\n ")
#The city_name is the name of the varibale that holds the input function

pet_name = input("What is the name of your pet?\n ")
#The pet_name is the name of the variable that holds the next input function

print("Your band name could be " + city_name + " " + pet_name)
#The print function prints the Band name message by calling the variable names 
# + method is used for concatenation of variable names & the double quotes is used to apply space between the generated name






