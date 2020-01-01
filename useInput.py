message = input("Tell me something, and I will repeat it back to you: ")
print (message)

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
#prompt += "\nWhat is your age? " this doesn't work
name = input(prompt)
print(f"\nHello, {name}!")

#as numerical input
age = input("How old are you? ")

#to compare, we have first convert the string to a numerical value:.
#age = int(age)
#age >= 18

#try it yourself 7-1
rentalCar = input("What kind of car would you like to rent? ")
print(f"\nLet me see if I can find you a {rentalCar}.")

# 7-2
guests = input("How many people are in your group?")
guests = int(guests)

if guests >= 8:
    print("\nYou will have to wait to be seated.")
else:
    print("Your table is ready.")

#7-3
number = input("Enter a number. I'll tell you if it is a multiple of 10 or not: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThis number is a multiple of 10")
else:
    print(f"\nThis number is NOT a multiple of 10")

#while loop
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1












