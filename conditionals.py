cars = ['audi', 'bmw', 'volkswagen', 'mercedes']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

if car != cars:
    print('non-German')

cars == 'bmw' and 'volkswagen'
    
banned_users = ['muhammad', 'ahmed', 'abdul', 'sayeed']
user = 'enis'

if user not in banned_users:
    print(f"Welcome to our group, {user.title()}!")

age = [2, 13, 40, 72]

for age in age:
    if age  <= 12:
        print('Your admission is free!')
    elif age > 12 and age < 18:
        print('Please pay $5 for admission.')
    elif age >= 65:
        print('You get a senior discount!')
    else:
        print('Please pay $10 for admission')


alien_color = 'green'

if alien_color == 'green':
    print('You earned 5 points!')
else:
    print('You lose')

alien_color = ['green', 'yellow', 'red', 'blue']

for alien_color in alien_color:
    if alien_color == 'yellow':
        print('You just earned 10 points!')
    if alien_color == 'red':
        print('You just earned 15 points!')    
    if alien_color == 'green':
        print('You just earned 5 points!')
    if alien_color == 'blue':
        print('You just earned 20 points!') #all if statements print with this loop
else:
    print("Don't shoot your friends!") # keep else out of the if block to avoid double printing

alien_color = ['green', 'yellow', 'red', 'blue']

for alien_color in alien_color:
    print(f"{alien_color.title()} alien down!")

print("\nVICTORY!")

alien_color = []

if alien_color:
    for alien_color in alien_color:
        print(f"{alien_color.title()} alien down!")
else:
    print("\nNo aliens in sight.")



user_ids = ['admin', 'amy', 'damjan', 'katie',  'alyssa', 'amanda', 'wendy']

if user_ids:
    for user_ids in user_ids:
        if user_ids == 'admin':
            print("\nHello Admin, would you like to see a status report?")
        else:
            print(f"Welcome back {user_ids.title()}! Would you like to check your inbox?")
else:
    print("\nWe need members!")


#checking usernames
current_users = ['dodo123', 'laShyGirlX3', 'mousyX4', 'elBajaPanty718',  'texasGangsta420']
new_users = ['laShyGirlX3', 'elCubanoEnMiami', 'lonelychicanorte', 'tuSexyPapi', 'elbajapanty718']

for i in range(0, len(current_users)):
    current_users[i] = current_users[i].lower()
for i in range(0, len(new_users)):
    new_users[i] = new_users[i].lower()
    
for new_users in new_users:
    if new_users in current_users:
        print('\nSorry, that username is already taken!')
    else:
        print(f'\n{new_users} is available.')

for value in range(1, 10):
    if value == 1:
        print("\n1st")
    elif value == 2:
        print("\n2nd")
    elif value == 3:
        print("\n3rd")
    else:
        print(f"\n{value}th")








#dictionaries

    














