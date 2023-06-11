from datetime import datetime

def Calculate_Age(birthdate):
    current_date = datetime.now()

    years_diff = current_date.year - birthdate.year
    months_diff = current_date.month - birthdate.month
    days_diff = current_date.day - birthdate.day

    if (current_date.year, current_date.month) < (birthdate.year, birthdate.month):
        years_diff -= 1

    if (current_date.month, current_date.day) < (birthdate.month, birthdate.day):
        months_diff -= 1

    return years_diff, months_diff, days_diff

birth_year = int(input('Enter the birth year: '))
birth_month = int(input('Enter the birth month: '))
birth_day = int(input('Enter the birth day: '))

birthdate = datetime(birth_year, birth_month, birth_day)

years, months, days = Calculate_Age(birthdate)

print(f'The age is {years} years, {months} months and {days} days ')