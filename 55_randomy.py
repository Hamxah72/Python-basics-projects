from random import randint
import random

answer_list = []

global our_states
our_states = [
        "Adamawa", "Bauchi", "Borno", "Gombe", "Taraba", "Yobe", "Kano", "Kaduna", "Katsina", "Jigawa", "Kebbi", "Sokoto", "Zamfara" 
    ]

global our_state_capitals
our_state_capitals = {
    "Adamawa":"Yola",
    "Bauchi":"Bauchi",
    "Borno":"Maiduguri",
    "Gombe":"Gombe",
    "Taraba":"Jalingo",
    "Yobe":"Damaturu",
    "Kano":"Kano",
    "Kaduna":"Kaduna",
    "Katsina":"Katsina",
    "Jigawa":"Dutse",
    "Kebbi": "Birnin Kebbi",
    "Sokoto":"Sokoto",
    "Zamfara":"Gusau"
}

# Generate random number
global rando
rando = randint(0, len(our_states)-1)

# print(our_states[rando])
# print(our_state_capitals[our_states[rando]])

answer = our_states[rando]

'''
# Add our first random selection to our answer_list list
answer_list.append(our_states[rando])

# Remove answer from list
our_states.remove(our_states[rando])

# Shuffle our original list
random.shuffle(our_states)

# Randomly select our next state
rando = randint(0, len(our_states)-1)
answer_list.append(our_states[rando])


# Remove 2nd answer from list
our_states.remove(our_states[rando])

# Shuffle our original list
random.shuffle(our_states)

# Randomly select our 3rd state
rando = randint(0, len(our_states)-1)
answer_list.append(our_states[rando])

print(answer_list)
print(answer)
'''

count = 1

while count < 4:
    rando = randint(0, len(our_states)-1)

    # If 1st selection, make it our answer
    if count == 1:
        answer = our_states[rando]

    # Add our 1st selection to a new list
    answer_list.append(our_states[rando])

    # Remove from old list
    our_states.remove(our_states[rando])

    # Shuffle original list
    random.shuffle(our_states)


    count += 1

print(answer_list)
print(answer)
random.shuffle(answer_list)
print(answer_list)

print(our_state_capitals[answer])