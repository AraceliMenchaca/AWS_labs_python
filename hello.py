import json

filename = 'userName.json'
name = ''

# Check for a history file
try:
    with open(filename, 'r') as r:
        # load the user name from the file
        name = json.load(r)
    
except IOError:
    print("First-time login")

# Save the user's name to the history file
try:
    with open(filename, 'w',) as f:
        json.dump(name, f)
except IOError:
    print("There was a problem writing to the history file.")