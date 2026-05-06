# Celsius convert to Fahrenheit
Celsius = float(input("Enter temperature in Celsius: "))
result = (Celsius * 9/5) + 32
print(f"{result: .1f}")

# Fahrenheit convert to Celsius
Fahrenheit = float(input("Enter temperature in Fahrenheit: "))
result = round (Fahrenheit - 32) * 5/9
print(f"{result: .1f}")