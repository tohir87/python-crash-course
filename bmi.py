#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Method to compute by lbs
def computeByLbs():
    weight = input("What is your weight (lbs): ")
    height = input("What is your height: (inches) ")
    bmi =  (float(weight)/pow(float(height), 2)) * 703 
    return bmi


# Method to compute by kg
def computeByKg():
    weight = input("What is your weight (kg): ")
    height = input("What is your height: (m) ")
    bmi =  float(weight)/pow(float(height), 2) 
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
print("your BMI is: ", bmi)
print("WHO category: ", category)


# In[ ]:





# In[ ]:




