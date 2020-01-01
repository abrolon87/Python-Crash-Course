#dictionaries

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']

print(f"You just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']} and is worth {alien_0['points']} points.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

#move alien to the right
#determine how far based on alien current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

#change the speed
alien_0['speed'] = 'fast'

#removing key:value pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# dictionary of similar objects
spoken_languages = {
    'jen': 'english',
    'sara': 'persian',
    'seamus': 'gaelic',
    'juan': 'spanish',
    }

language = spoken_languages['sara'].title()
print(f"Sara speaks {language}.")

spoken_languages['seamus'] #returns 'gaelic'

lang_val = spoken_languages.get('jen')
print(lang_val) #returns 'english'

lang_val = spoken_languages.get('mike', 'no language given')
print(lang_val) #returned None. Now returns 'no language given'
#when trying to access values that may not exist, use .get() method instead of []

#try it yourself
#6-1
person = {'firstName': 'saddam', 'lastName': 'akbarov', 'city': 'weymouth', 'state': 'massachusetts', 'age': '29'}
print(person['city'])
print(person)

for k, v in person.items():
    print(f"\nK: {k}")
    print(f"V: {v}")

#6-3
newVocab = {
    'dictionary': 'a collection of key-value pairs',
    'key': 'a key is connected to a value',
    'del': 'used to remove key-value pairs',
    }

for key, value in newVocab.items():
    print(f"\n{key}: {value}")


#looping through dictionaries

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


spoken_languages = {
    'jen': 'english',
    'sara': 'persian',
    'seamus': 'gaelic', 
    'juan': 'spanish',
    'mateo': 'spanish', 
    'milos': 'serbian',
    'farzad': 'persian',
    'josh': 'english',
    'damjan': 'serbian',

    }

for name, lang in spoken_languages.items():
    print(f"\n{name.title()} speaks {lang.title()}.")
#outputs both key and value

for name in spoken_languages.keys():
    print(name.title())
    
#looping speficially through keys is default behavior so
    #for name in spoken_languages: would give the same result.


friends = ['sara', 'juan']
for name in spoken_languages.keys():
    print(name.title())

    if name in friends:
        lang = spoken_languages[name].title()
        print(f"\tHi {name.title()}! I see you speak {lang}!")

if 'damjan' not in spoken_languages.keys():
    print("\nDamjan, please list your languages!")

for name in sorted(spoken_languages.keys()):
    print(f"\n{name.title()}, thank you for listing your languages.")

#looping through values in a dictionary
print("\nWe have speakers of the following languages:")
for lang in spoken_languages.values():
    print(lang.title())

print("\nWe have speakers of the following languages:")
for lang in set(spoken_languages.values()):
    print(lang.title())

rivers = {
    'amazon': 'south america',
    'dunav': 'eastern europe',
    'mississippi': 'united states',
    }

for river, country in rivers.items():
    print(f"\nThe {river.title()} River flows through {country.title()}.")
          




