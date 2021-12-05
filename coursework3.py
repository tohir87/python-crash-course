#!/usr/bin/env python
import datetime

# function calculate age from date of birth
# returns age
def age(day, month, year):
    birthDate = datetime.date(year, month, day)
    timeDiff = datetime.date.today() - birthDate
    return int(timeDiff.days/365)

# Function to get the Western zodiac sign from date of birth
# return sign
def wt_zodiac(birthDay, birthMonth):
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
    else:
        sign = "Capricorn"

    return sign;

#A function to calculate the animal associated with a zodiac sign
def cn_zodiac(year):
    animal = 'rat';
    return animal;


def main():

    userList = [] # Initialize user list array
    terminate = 0 # Initiase terminate, the progam will keep runing until terminate is set to 1

    #Read input from text file
    userData = open("UserData.txt", "r")
    for line in userData:
        #split line by tab space
        userArray = line.split()
        if userArray[0] == 'UID':
            continue
        uId = userArray[0]
        name = userArray[1] + ' ' + userArray[2]
        dob = userArray[3]
        print(userArray)
            
        #split the date of birth to extract the month, day and year
        splited    = dob.split('-')
        day   = splited[2]
        month = splited[1]
        year  = splited[0]

        #calculate the age of the user
        userAge    = age(int(day), int(month), int(year))
        #get Zodiac Sign
        sign = wt_zodiac(day, month)
        #get the chinese zodiac sign
        cnZodiac = cn_zodiac(year)

        # Push user information into user list array
        userList.append( [uId, name, dob, userAge, sign, cnZodiac]);


    #display all user in table format
    print("UID\t Name\t D.o.b\t Age\t Western Zodiac\t Chinese Zodiac\n")
    for u in userList:
        uId     = u[0]
        uName   = u[1]
        uDob    = u[2]
        uAge    = u[3]
        uSign   = u[4]
        cnSign   = u[5]
        print(f'{uId:2}  {uName:10} {uDob:12} {uAge:5} {uSign:15} {cnSign:15}')

if __name__ == "__main__":
    main()
