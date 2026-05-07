import random
import string

# Get user preferences
length = int(input("How long shoud the password be? "))
use_numbers = input("Include numbers? ")
use_symbols = input("Include symbols? ")

# Build the charactor pool
characters = string.ascii_letters

if use_numbers == "yes":
    characters += string.digits

if use_symbols == "yes":
    characters += string.punctuation

# Generate the password
password = ""

for i in range(length):
    password += random.choice(characters)

# Show the results
print(f"\n Your generated password is: {password}")
print(f"Password length: {length} characters")