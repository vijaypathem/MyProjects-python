'''
    An input box asks you to enter the name of a country.
When you type in your answer, the program tells you
what the capital city is. If the program doesn’t know,
it asks you to teach it the correct answer. The more
people use the program, the smarter it gets!

'''

from tkinter import Tk, simpledialog, messagebox

print('Ask the Expert - Capital cities of the countries')

root = Tk()
root.withdraw()

country_city = {}

def read_from_file():
    with open('MyProjects-python/Capital_Cities.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            country_city[country] = city

def write_to_file(country_name , city_name):
    with open('MyProjects-python/Capital_Cities.txt', 'a') as file:
        file.write('\n'+country_name+'/'+city_name)

read_from_file()

while True:
    query_country = simpledialog.askstring('Country','Type the name of a country:').capitalize()

    if query_country in country_city:
        result = country_city[query_country]
        messagebox.showinfo('Answer','The Capitl City Of '+ query_country + ' is ' + result + ' !')
    else:
        new_city = simpledialog.askstring('Teach Me','I don\'t know! '+'What is the capital city of '+query_country+' ?').capitalize()
        country_city[query_country]=new_city
        write_to_file(query_country, new_city)
        root.mainloop()
                      