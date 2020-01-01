prompt = "\nTell me something: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit' :
    message = input(prompt)
    print(message)

prompt = "\nTell me something: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit' :
    message = input(prompt)

    if message != 'quit' :   #this is to prevent 'quit' from printing as a message
        print(message)

prompt = "\nTell me something and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True  #this is called a 'flag'
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

#continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)








