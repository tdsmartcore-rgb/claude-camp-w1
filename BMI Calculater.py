# Enter your height in meters
height = float (input ("Enter your height in meters (e.g. 1.65): "))

# Enter your weight in kg
weight = float (input (" Enter your weight in kg (e.g. 55): "))

#Calculate BMI
BMI = weight / (height * height)

#Show the results
print (f"Your BMI is {BMI: .1f}")

#Explain the results
if BMI < 18.5:
 print (" You are underweight")
elif BMI <25:
 print ("You are at normal weight")
elif BMI <30:
 print ("You are overweight")
else:
 print ("Obese")