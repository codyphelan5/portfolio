import random

my_password = 0
PASSWORD_LENGTH = 4
LOWER_CHARACTER = 50
UPPER_CHARACTER = 120
systems = [
    {"system_name": "Bank of America", "user_id": "henryru@hotmail.com", "password": ""},
    {"system_name": "Toys R US", "user_id": "bobmur@hotmail.com", "password": ""}
    ]

for system in systems:
    for _ in range(PASSWORD_LENGTH):
        system["password"] += chr(random.randint(LOWER_CHARACTER, UPPER_CHARACTER))
print(systems)
found = False
tries = 0
while not found:
    matching_password = ""

    for _ in range(PASSWORD_LENGTH):
        matching_password += chr(random.randint(LOWER_CHARACTER, UPPER_CHARACTER))
    for system in systems:
        tries += 1

        if matching_password == system["password"]:
            print(matching_password, tries)
            found = True
            break
        else:
            print("Keep trying")



#create a variable at the top called "my password" and let the program see how long it takes to guess ur password.
#start simple with small words first
