#!/usr/bin/env python
import datetime

# function calculate age from date of birth
# returns age
def calculateAge(day, month, year):
    birthDate = datetime.date(year, month, day)
    timeDiff = datetime.date.today() - birthDate
    return int(timeDiff.days/365)

# Function to get the Western zodiac sign from date of birth
# return sign
def zodiacSign(birthDay, birthMonth):
    sign = ""
    if ( (birthMonth == "01" and int(birthDay) >= 20) or (birthMonth == "02" and int(birthDay) <= 18) ):
        sign = "Aquarius"
    elif ( (birthMonth == "02" and int(birthDay) >= 19) or (birthMonth == "03" and int(birthDay) <= 20) ):
        sign = "Pisces"
    elif ( (birthMonth == "03" and int(birthDay) >= 21) or (birthMonth == "04" and int(birthDay) <= 19) ):
        sign = "Aries"
    elif ( (birthMonth == "04" and int(birthDay) >= 20) or (birthMonth == "05" and int(birthDay) <= 20) ):
        sign = "Taurus"
    elif ( (birthMonth == "05" and int(birthDay) >= 21) or (birthMonth == "06" and int(birthDay) <= 20) ):
        sign = "Gemini"
    elif ( (birthMonth == "06" and int(birthDay) >= 21) or (birthMonth == "07" and int(birthDay) <= 22) ):
        sign = "Cancer"
    elif ( (birthMonth == "07" and int(birthDay) >= 22) or (birthMonth == "08" and int(birthDay) <= 22) ):
        sign = "Leo"
    elif ( (birthMonth == "08" and int(birthDay) >= 23) or (birthMonth == "09" and int(birthDay) <= 22) ):
        sign = "Virgo"
    elif ( (birthMonth == "09" and int(birthDay) >= 23) or (birthMonth == "10" and int(birthDay) <= 22) ):
        sign = "Libra"
    elif ( (birthMonth == "10" and int(birthDay) >= 23) or (birthMonth == "11" and int(birthDay) <= 21) ):
        sign = "Scorpio"
    elif ( (birthMonth == "11" and int(birthDay) >= 22) or (birthMonth == "12" and int(birthDay) <= 21) ):
        sign = "Sagittarius"
    elif ( (birthMonth == "12" and int(birthDay) >= 22) or (birthMonth == "01" and int(birthDay) <= 19) ):
        sign = "Capricorn"

    return sign;


userList = [] # Initialize user list array
terminate = 0 # Initiase terminate, the progam will keep runing until terminate is set to 1

while terminate == 0:
    try:
        userId = input("Please enter your USER ID(2 digit number):")
        if userId == "end":
            break
        uId = int(userId)
        name   = input("Please enter your name:")
        dob    = input("Please enter your date of birth(DD/MM/YYYY):")
        
        #split the date of birth to extract the month, day and year
        splited    = dob.split('/')
        day   = splited[0]
        month = splited[1]
        year  = splited[2]
        #todo: implement some validation logic for date of birth

        #calculate the age of the user
        age    = calculateAge(int(day), int(month), int(year))
        #get Zodiac Sign
        sign = zodiacSign(day, month)

        # Push user information into user list array
        userList.append( [uId, name, dob, age, sign]);
    except ValueError:
        print('You have entered an invalid User ID')

#display all user in table format
print("UID\t Name\t D.o.b\t Age\t Western Zodiac\n")
for u in userList:
    uId     = u[0]
    uName   = u[1]
    uDob    = u[2]
    uAge    = u[3]
    uSign   = u[4]
    
    print(f'{uId:2d}  {uName:10} {uDob:12} {uAge:5} {uSign:15}')
