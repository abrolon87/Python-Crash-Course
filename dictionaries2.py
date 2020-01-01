#dictionaries2
#p106
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []
#make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#show first 5
for alien in aliens[:5]:
    print(alien)
print("...")

#show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")

for alien in aliens[:3]:
    if alien['color'] == 'green':
         alien['color'] = 'yellow'
         alien['speed'] = 'medium'
         alien['points'] = 10


for alien in aliens[:5]:
    print(alien)
print("...")

for alien in aliens[0:3]:
    if alien['color'] == 'green':
         alien['color'] = 'yellow'
         alien['speed'] = 'medium'
         alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("...")

#list inside dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'olives', 'spinach'],
    }
#summerize order
print(f"You ordered a {pizza['crust']} crust pizza " #to break long line
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

print("...")
    

spoken_languages = {
    'jen': 'english',
    'sara': 'persian',
    'seamus': ['gaelic', 'english'], 
    'juan': ['spanish', 'english'],
    'mateo': 'spanish', 
    'milos': 'serbian',
    'farzad': 'persian', 
    'josh': ['english', 'french'],
    'damjan': ['serbian', 'german', 'english',  'spanish',  'arabic', 'polish', 'turkish', 'french'],

    }


for name, languages in spoken_languages.items():
    print(f"\n{name.title()} speaks:")
    for language in languages:
          print(f"\t{language.title()}")
#this way, the single languages get printed vertically because they are not in a list
#below is the corret format to print normally
spoken_languages = {
    'jen': ['english'],
    'sara': ['persian'],
    'seamus': ['gaelic', 'english'], 
    'juan': ['spanish', 'english'],
    'mateo': ['spanish'], 
    'milos': ['serbian'],
    'farzad': ['persian'], 
    'josh': ['english', 'french'],
    'damjan': ['serbian', 'german', 'english',  'spanish',  'arabic', 'polish', 'turkish', 'french'],

    }


for name, languages in spoken_languages.items():
    print(f"\n{name.title()} speaks:")
    for language in languages:
          print(f"\t{language.title()}")
#prints normal

#dictionaries inside dictionaries
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")










         
