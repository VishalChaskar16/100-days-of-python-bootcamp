#Program to calculate tip

#printing welcome message
print("Welcome to my tip calculator!")

#creating a variable to store the input datatype and later convrting it as a float datatype to store decimal values
bill = input("What is your total bill in $?\n")
new_bill = float(bill)

#creating a variable to store input datatype and then converting it as int datatype to store numbers
tip = input("How much tip would you like to give? 10, 12 ,15\n")
new_tip = int(tip)

#Similar as above line of code
split = input("How many will to split the bill with?\n ")
new_split = int(split)

#Using the formula to first divide tip percentage with 100 then multiplying it with 100 then again adding it to the total bill value
bill_amount = new_tip / 100
new_amount = bill_amount *100
total_bill = new_amount + new_bill

#Splitting the bill by dividing total bill with the number of people
total_split = total_bill / new_split

#using the round function to round off the split bill to 2 decimal values
bill_round = round(total_split, 2)

#Using f-string to print string and int datatype together
print(f"Each person has to pay {bill_round}")


