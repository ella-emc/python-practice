print("Body Mass Index Calculator and Evaluator")
print("For this to work, type in your weight in kilograms and height in meters below.")
weight = float(input("Weight in Kilograms: "))
height = float(input("Height in Meters: "))

bmi = weight // height ** 2
print("Your body mass index (BMI) is " + str(bmi))

if bmi < 18.5:
    print("Your BMI classification is Underweight.")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Your BMI classification is Normal.")
elif bmi >= 25.0 and bmi <= 29.9:
    print("Your BMI classification is Overweight.")
elif bmi >= 30.0 and bmi <= 34.9:
    print("Your BMI classification is Obese, Class I.")
elif bmi >= 35.0 and bmi <= 39.9:
    print("Your BMI classification is Obese, Class II.")
else:
    print("Your BMI falls under Extreme Obesity.")

print("The BMI classifications above were retrieved from the National Heart, Lung, and Blood Institute.")