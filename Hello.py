#imports
import Module

firstName = "Gopikiran"
lastName = "Lakkoju"
length = len(firstName)
array = [23, 43, 45, 65, 67, 89]
array.append(69)
array.remove(89)
if firstName is "Gopikiran":
    print("Yay got it!")
else:
    print(":(")
for nos in range(10, 20, 2):
    print(nos)
i = 0
while i < length:
    print(firstName[i])
    i += 1

magicNo = 48


def findNumbersDivisibleBy4():
    for o in range(100):
        if o % 4 is 0:
            print(o, "is the magic no")

#findNumbersDivisibleBy4()

def bitcoin_to_inr(btc):
    final = btc * 435
    print(final)

bitcoin_to_inr(45.3)

def get_gender(gender = 'Unkown'):
    if gender is 'f':
        print("Female")
    elif gender is 'm':
        print("Male")
    else:
        print(gender)

get_gender("m")

def params_method(*params):
    # considering params to be int/string
    for p in params:
        print(p)

params_method(3, 4, 5, 7, 46, 7)

def unpackObject(age, gender, ethnic):
    print(age +" "+ gender +" with "+ ethnic)

person = ["32", "Male", "Caucasian"]
# *means the object would be unpacked based on arguments and values supplied subsequently
unpackObject(*person)

if 'Male' in person:
    print("Exists")
else:
    print("Does not exists")
# index print from dictionary
friends = {'Gopikrain': 'Good', 'Sanjay': 'Cool', 'Robert': 'Naughty ass', 'Sandeep': 'Conservative', 'Jany': 'Opposite of commitment'}

print(friends['Sandeep'])

# looping through dictionary <key, value> pair
for k, v in friends.items():
    print(k + ' ' + v)

Module.printSomething("How is everything")