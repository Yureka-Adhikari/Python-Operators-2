weight = float(input("Enter your weight in kg: "))
height= float(input("Enter your height in meters: "))

bmi= weight/(height**2)

print(f"Your BMI is {bmi}")

if bmi <= 18.4:
    print("You are underweight")
elif bmi <= 24.9:
    print("You are Healthy")
elif bmi <= 29.9:
    print("You are Over Weight")
elif bmi <= 34.9:
    print("You are Severely Over Weight")
elif bmi <= 39.9:
    print("You are obese")
else:
    print("You are Severely Obese.")