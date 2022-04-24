""" The is in integration project designed to test
calculate the BMR needed for weight loss. It will request
and return values needed for calculations. It gives the
possibility to use either imperial or metric system for
calculation. There is still much I want to add. When time
also I will rewrite and create a program that operates
more efficiently."""

__author__ = "Fausto Beato"


def get_sex(sex):
    """
Here the function is set to allow the user to decide
which sex they will be inputting information as. The
choice is between male and female. The function will
users input and if it's and x for male or a y for
female it will return the value for the next function
    :param sex: variables are used for the proper calculator
    :return: returning value for requesting function
    """
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
        except ValueError:
            print("Invalid input. Try again.")


def get_metric():
    """
    This function will be utilizing values for calculations using the metric
    system. The values centimeters for height and kilograms for weight. the 
    values are compiled to determine BMR for either male or female. It will 
    break down the values to what is needed daily
    """
    print("\n\nBefore we continue I need to know if you are a male or female.")
    print("I utilize the Harris-Benedict BMR formula for my calculations.\n")
    sex = input("Please choose [x] for male and [y] for female: ")
    sex = sex.lower()
    get_sex(sex)
    age = int(input("Annnnd... What's your age? "))
    get_age(age)
    male = "x"
    female = "y"
    if sex == male:
        # Your basal metabolism rate is produced through the following basal 
        # metabolic rate formula: https://www.garnethealth.org/
        height = float(input("What is your height in cm? "))
        weight = float(input("What is your weight in kg? "))
        bmr_male = 88.362 + (13.397 * weight) + (4.799 * height) - (
                    5.677 * age)
        print("As a male to maintain your current weight you need: ",
              format(bmr_male * 7, '.2f'), "calories weekly")
        weekly_m_bmr = bmr_male * 7
        calories = int(3500)
        print("There are 3500 calories in a lb")
        cal_def = (weekly_m_bmr - calories) / 7
        print("To lose 1 lb a week: ", format(cal_def, '.2f'), "daily.")
    if sex == female:
        height = float(input("What is your height in cm? "))
        weight = float(input("What is your weight in kg? "))
        bmr_female = 447.593 + (9.247 * weight) + (3.098 * height) - (
                    4.330 * age)
        print("Female BMR: ", format(bmr_female, '.2f'))
        print("As a female to maintain your current weight you need: ",
              format(bmr_female * 7, '.2f'), "calories weekly")
        weekly_f_bmr = bmr_female * 7
        calories = int(3500)
        print("There are 3500 calories in a lb")
        cal_def = (weekly_f_bmr - calories) / 7
        print("To lose 1 lb a week: ", format(cal_def, '.2f'), "daily.")


def get_imperial():
    """
    This function will be utilizing values for calculations using the imperial
    system. The values; inches for height and pounds for weight. The values
    are compiled to determine BMR for either male or female. It will break down
    the value to what is needed daily
    """
    print("\n\nBefore we continue I need to know if you are a male or female.")
    print("I utilize the Harris-Benedict BMR formula for my calculations.\n")
    sex = input("Please choose [x] for male and [y] for female: ")
    sex = sex.lower()
    get_sex(sex)
    age = int(input("Annnd... What's your age? "))
    get_age(age)
    male = "x"
    female = "y"
    if sex == male:
        # Your basal metabolism rate is produced through the following basal 
        # metabolic rate formula: https://www.garnethealth.org/
        height = float(
            input("What is your height in inches? "))
        weight = float(input("What is your weight in lbs? "))
        bmr_male = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
        print("Male BMR: ", format(bmr_male, '.2f'))
        print("As a male to maintain your current weight you need: ",
              format(bmr_male * 7, '.2f'), "calories weekly")
        weekly_m_bmr = bmr_male * 7
        calories = int(3500)
        print("There are 3500 calories in a lb")
        cal_def = (weekly_m_bmr - calories) / 7
        print("To lose 1 lb a week: ", format(cal_def, '.2f'), "daily.")
    if sex == female:
        height = float(input("What is your height in inches? "))
        weight = float(input("What is your weight in lbs? "))
        bmr_female = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
        print("Female BMR: ", format(bmr_female, '.2f'))
        print("As a female to maintain your current weight you need: ",
              format(bmr_female * 7, '.2f'), "calories weekly")
        weekly_f_bmr = bmr_female * 7
        calories = int(3500)
        print("There are 3500 calories in a lb")
        cal_def = (weekly_f_bmr - calories) / 7
        print("To lose 1 lb a week burn ", format(cal_def, '.2f'), ", daily.")


def measure_sys(choice):
    """
    Here the function is trying to determine whether to calculate
    using the metric system or imperial system. The 2 use a different
    values to determine BMR.
    :param choice: the 'choice' will be returned to utilize the proper
    calculator
    :return: returning the choice
    """
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
        except ValueError:
            print("Invalid input. Try again.")


def get_age(age):
    """
    Getting the users age to utilize for calculations. The age has
    to be more than 0. Here it will test the values until it has the
    value necessary to continue.
    :param age: what is the age of the user
    :return: the age of the user
    """
    x = False
    while not x:
        try:

            if age <= 0:
                print("Testing the womb?")
            elif age > 0:
                print("Thank you, let's continue.")
                return age
        except ValueError:
            print("Invalid input. Try again.")


def get_user():
    """
Getting users name and information for a greeting. An attempt at making
the program feel inviting.
    """
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print('\nHello,', first_name, last_name, ', lets lose some weight!')


def main():
    """
Welcomes to the integration. Gets the users name and continues
to get information for calculations. Within the main function there
it will decide which measuring system to use and continue until the
end of the calculations are completed. A disclaimer should be
presented for the safety of the user.
    """
    print("Welcome to my integration project.\n")
    get_user()
    print("\nLet's get personal")
    print("I will be asking a series of information for my calculations")

    print('\n')
    print("Which measuring system to you prefer?")
    choice = input("Enter [i]for imperial or [m]for metric: ")
    choice = choice.lower()
    measure_sys(choice)
    for i in range(1):
        if choice == "m":
            get_metric()
        else:
            get_imperial()

    disclaimer = open('disclaimer.txt')
    md = disclaimer.read()
    print(md)


if __name__ == '__main__':
    main()
