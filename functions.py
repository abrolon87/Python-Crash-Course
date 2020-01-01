#functions
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

#greet user by name
def greet_user(username):
    print(f"Hello, {username.title()}!")

greet_user('amanda')

#8-1
def display_message():
    print("I'm learning about functions")

display_message()

#8-2
def favorite_book(title):
    print(f"My favorite book is {title.title()}.")

favorite_book('harry potter')

def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('cat', 'tiger')
describe_pet('dog', 'bruno')
#order matters

#keyword arguements
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type = 'hamster', pet_name = 'harry')

# default values

def describe_pet(pet_name, animal_type = 'dog'): #notice the order is changed here
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name = 'willie')

#8-3
def make_shirt(size, text):
    print(f"\nsize {size}.")
    print(f"{text.title()}.")

make_shirt('medium', 'proud to be python!')

#8-4
def make_shirt(text, size = 'large'):
    print(f"\nsize {size}.")
    print(f"{text.title()}.")

make_shirt('i love python!')

#8-5
def describe_city(city, country = 'bosnia'): 
    print(f"\n{city.title()} is in {country.title()}.")

describe_city('sarajevo')
describe_city('banja luka')
describe_city('belgrade', country = 'serbia') #python ignores defaunt value is clearly stated

#returning a value
def get_formatted_name(first_name, last_name):
    """return a full name, neatly formatted"""
    full_name = f"\n{first_name} {last_name}" #put \n here
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#making an argument optional
def get_formatted_name(first_name, middle_name, last_name):
    full_name = f"\n{first_name} {middle_name} {last_name}" #put \n here
    return full_name.title()

musician = get_formatted_name('mary', 'j.', 'blige')
print(musician)

def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('mile', 'kitic')
print(musician)
musician = get_formatted_name('nedeljko', 'baja', 'bajic')
print(musician)

def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('mile', 'kitic')
print(musician)

def build_person(first_name, last_name, age = None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('mile', 'kitic', age = 61)
print(musician)


#functions with while loops
def get_formatted_name(first_name, last_name):
    full_name = f"\n{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':  #these breaks avoid infinite loops
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

def city_country(city, country):
    print(city.title(), country.title())

city_country('ankara,', 'turkey')
city_country('belgrade,', 'serbia')
city_country('sarajevo,', 'bosnia')


def make_album(artist, album, tracks = None):
    album = {'artist': artist, 'album': album}
    if tracks:
        album['tracks'] = tracks
    return album

albums = make_album('elton john', 'candle in the wind')
print(albums)















