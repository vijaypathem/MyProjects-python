from datetime import datetime

def Calculate_Age(birthdate):
    current_date = datetime.now()
    age = current_date.year - birthdate.year

    if(current_date.month, current_date.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age


birth_year = int(input("Enter the birth year : "))
birth_month = int(input("Enter the birth month : "))
birth_day = int(input("Enter the birth day : "))

birthdate = datetime(birth_year, birth_month, birth_day)

age = Calculate_Age(birthdate)

print(f"The age is: {age}")