#Fausto Beato
#Date 03/25/2022
#Description: This programs offers a weight loss plan

def getSex(sex):
    male = "x"
    female = "y"
    known = False
    while not known:
        try:  
            sex = sex.lower()
            if sex == "x":
                print("You have chosen male.")
                return male
            elif sex == "y":
                print("You have chosen female.")
                return female
            else:
                print("Invalid input. Try again.")
        except:
            print("Invalid input. Try again.")
            
def getMetric():
        print("\n\nBefore we continue I need to know if you are a male or female.")
        print("I utlize the Harris-Benedict BMR formula for my calculations.\n")
        sex = input("Please choose [x] for male and [y] for female: ")
        sex = sex.lower()
        getSex(sex)
        age = int(input("Annnnd... What's your age? "))
        getAge(age)
        male = "x"
        female = "y"
        if sex == male:
#Your basal metabolism rate is produced through the following basal metablic rate formula: https://www.garnethealth.org/
            height = float(input("What is your height in cm? "))#I have converted height into a float to utilize decimal
            weight = float(input("What is your weight in kg? "))
            bmr_male = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
            print("As a male to maintain your current weight you need: ", format(bmr_male * 7,'.2f'),"calories weekly")
            weekly_mBMR = bmr_female * 7
            calories = int(3500)
            print("There are 3500 calories in a lb")
            calDef = (weekly_mBMR - calories) / 7
            print("To lose 1 lb a week: ", format(calDef, '.2f'),"daily.")
        if sex == female:
            height = float(input("What is your height in cm? ")) #I have converted height into a float to utilize decimal
            weight = float(input("What is your weight in kg? "))
            bmr_female = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
            print("Female BMR: ",format(bmr_female,'.2f'))
            print("As a female to maintain your current weight you need: ", format(bmr_female * 7,'.2f'),"calories weekly")
            weekly_fBMR = bmr_female * 7
            calories = int(3500)
            print("There are 3500 calories in a lb")
            calDef = (weekly_fBMR - calories) / 7
            print("To lose 1 lb a week: ", format(calDef, '.2f'),"daily.")


def getImperial():
        print("\n\nBefore we continue I need to know if you are a male or female.")
        print("I utlize the Harris-Benedict BMR formula for my calculations.\n")
        sex = input("Please choose [x] for male and [y] for female: ")
        sex = sex.lower()
        getSex(sex)
        age = int(input("Annnnd... What's your age? "))
        getAge(age)
        male = "x"
        female = "y"
        if sex == male:
#Your basal metabolism rate is produced through the following basal metablic rate formula: https://www.garnethealth.org/
            height = float(input("What is your height in inches? ")) #I have converted height into a float to utilize decimal
            weight = float(input("What is your weight in lbs? "))
            bmr_male = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age) #this is Harris-Benedict formula for BMR
            print("Male BMR: ", format(bmr_male,'.2f'))
            print("As a male to maintain your current weight you need: ", format(bmr_male * 7,'.2f'),"calories weekly")
            weekly_mBMR = bmr_male * 7
            calories = int(3500)
            print("There are 3500 calories in a lb")
            calDef = (weekly_mBMR - calories) / 7
            print("To lose 1 lb a week: ", format(calDef, '.2f'),"daily.")
        if sex == female:
            height = float(input("What is your height in inches? ")) #I have converted height into a float to utilize decimal
            weight = float(input("What is your weight in lbs? "))
            bmr_female = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
            print("Female BMR: ",format(bmr_female,'.2f'))
            print("As a female to maintain your current weight you need: ", format(bmr_female * 7,'.2f'),"calories weekly")
            weekly_fBMR = bmr_female * 7
            calories = int(3500)
            print("There are 3500 calories in a lb")
            calDef = (weekly_fBMR - calories) / 7
            print("To lose 1 lb a week burn ", format(calDef, '.2f'),", daily.")
          
          



def measureSys(choice):
    metric = "m"
    imperial = "i"
    x = False
    while not x:
        try:
            
            choice = choice.lower()
            if choice == "i":
                print("You have chosen imperial.")
                return imperial
            elif choice == "m":
                print("You have chosen metric.")
                return metric
            else:
                print("Invalid input. Try again.")
        except:
            print("Invalid input. Try again.")
            

    
def getAge(age):
    x = False
    while not x:
        try:
            
            if age <= 0:
                print("Testing the womb?")
            elif age > 0:
                print("Thank you, let's continue.")
                return age
        except:
            print("Invalid input. Try again.")
            
def getUser():
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    print('\nHello,', firstName, lastName, ', lets lose some weight!')

def main():
    print("Welcome to my integration project.\n")
    getUser()
    print("\nLet's get personal")
    print("I will be asking a series of information for my calculations")
    
    print('\n')
    print("Which measuring system to you prefer?")
    choice = input("Enter [i]for imperial or [m]for metric: ")
    choice = choice.lower()
    measureSys(choice)
    for i in range (1):
        if choice == "m":
            getMetric()
        else:
            getImperial()
    
    disclaimer = open('disclaimer.txt')
    md = disclaimer.read()
    print (md)
    
    
main()
