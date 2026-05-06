# Ask for the user's name
name = input("Hello, what is your name? ")

# Greetings to the user
print(f"Pleasure to meet you, {name}")

#Ask for the user's age
age = int(input ("How old are you? "))

# Output the message templete at age range
if age <18:
 print ("You are a bit too young to buy our product. Please returen when you are 18 years old.")
elif age > 18:
 print("Welcome to our wine world. Explore our exceptional red and white wine. \n Click the bell in the top right to follow us and stay updated on our latest releases.")