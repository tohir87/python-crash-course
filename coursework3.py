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
def cn_zodiac(birth_year):
    if birth_year % 12 == 0:
        zodiac_animal = 'Monkey'
    if birth_year % 12 == 1:
        zodiac_animal = 'Rooster'
    if birth_year % 12 == 2:
        zodiac_animal = 'Dog'
    if birth_year % 12 == 3:
        zodiac_animal = 'Pig'
    if birth_year % 12 == 4:
        zodiac_animal = 'Rat'
    if birth_year % 12 == 5:
        zodiac_animal = 'Ox'
    if birth_year % 12 == 6:
        zodiac_animal = 'Tiger'
    if birth_year % 12 == 7:
        zodiac_animal = 'Rabbit'
    if birth_year % 12 == 8:
        zodiac_animal = 'Dragon'
    if birth_year % 12 == 9:
        zodiac_animal = 'Snake'
    if birth_year % 12 == 10:
        zodiac_animal = 'Horse'
    if birth_year % 12 == 11:
        zodiac_animal = 'Sheep'

    return zodiac_animal;


def writeToFile(userList):
    f = open("zodiac.txt", "w")

    #Write all user in table format in a txt file
    print("Writing user data to zodiac.txt")
    f.write("UID\t Name\t D.o.b\t Age\t Western Zodiac\t Chinese Zodiac\n")
    for u in userList:
        uId     = u[0]
        uName   = u[1]
        uDob    = u[2]
        uAge    = u[3]
        uSign   = u[4]
        cnSign   = u[5]
        f.write(f'{uId:2}  {uName:10} {uDob:12} {uAge:5} {uSign:15} {cnSign:15}')
        f.write("\n")

    f.close()
    print("Operation completed successfully")

# Main function. This is the entry point of the program
def main():

    userList = [] # Initialize user list array
    terminate = 0 # Initiase terminate, the progam will keep runing until terminate is set to 1

    #Read input from text file
    print("\nReading data from userData.txt file")
    userData = open("UserData.txt", "r")
    for line in userData:
        #split line by tab space
        userArray = line.split()
        if userArray[0] == 'UID':
            continue
        uId = userArray[0]
        name = userArray[1] + ' ' + userArray[2]
        dob = userArray[3]
            
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
        cnZodiac = cn_zodiac(int(year))

        # Push user information into user list array
        userList.append( [uId, name, dob, userAge, sign, cnZodiac])
        print ("processing...")

    writeToFile(userList) # call the function to write the result to file

if __name__ == "__main__":
    main()
