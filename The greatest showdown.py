number_one = float(input("Please enter your first number: "))
number_two = float(input("Please enter your second number: "))
number_three = float(input("Please enter your third number: "))

if number_one > number_two and number_one > number_three:
    largest = number_one
elif number_two > number_one and number_two > number_three:
    largest = number_two
else:
    largest = number_three
#Task 2
if number_one < number_two and number_one < number_three:
    smallest = number_one
elif number_two < number_one and number_two < number_three:
    smallest = number_two
else:
    smallest = number_three

print(f"The smallest number is {smallest} and the largest number is {largest}.")