#!/usr/bin/env python
# Student Name: ***** ********
# Student Number: *******


# Method to compute BMI by imprerial unit
def computeByLbs():
    # request for user weight
    weight = input("What is your weight (lbs): ")
    # request for user height
    height = input("What is your height: (inches) ")
    # calculate the bmi using the imperial formula
    bmi =  (float(weight)/pow(float(height), 2)) * 703 
    print(f'Your weight is: {weight} lbs')
    print(f'Your height is: {height} inches')
    return bmi


# Method to compute by metric Unit
def computeByKg():
    # request for user weight
    weight = input("What is your weight (kg): ")
    # request for user height
    height = input("What is your height: (m) ")
    # calculate the bmi using the metric formula
    bmi =  float(weight)/pow(float(height), 2) 
    # print the weight adn height on the screen
    print(f'Your weight is: {weight} kg')
    print(f'Your height is: {height} m')
    return bmi

#ask user for which method
print("What kind of method do you prefer? 1 for KG or 2 for lbs")
method = input("select method: ")
if (int(method) == 1):
    bmi = computeByKg()
else:
    bmi = computeByLbs()

#Determine the BMI category
if (bmi < 18.5):
    category = "Underweight"
elif(bmi >= 25 and bmi <= 30):
    category = "Underweight"
elif(bmi > 30):
    category = "Obese"
else:
    category = "Normal"
        
# print out the BMI
print(f'your BMI is: {bmi:.2f}')
print("WHO category: ", category)


# In[ ]:





# In[ ]:




