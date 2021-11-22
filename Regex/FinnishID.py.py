'''
Make a Python program, which can validate if the input string is a valid Finnish id number. 
You must calculate that the checksum is correct. Also output the birthdate of the person in format day.month.year 
and tell the gender (male/female) See https://fi.wikipedia.org/wiki/Henkil%C3%B6tunnus
'''
import re

check_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
        9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'H',
        17: 'J', 18: 'K', 19: 'L', 20: 'M', 21: 'N', 22: 'P', 23: 'R', 24: 'S',
        25: 'T', 26: 'U', 27: 'V', 28: 'W', 29: 'X', 30: 'Y'}

while True:
    id_number = input('Give Finnish id number: ')
    check_valid_first_step = re.match('^[0-9]{6}(-)?(a)?(A)?(\+)?[A-Za-z0-9]{4}$', id_number)
    if not check_valid_first_step:
        print('Not valid id - input is missing something or something is mispelled')
        continue
    else:
        #Collect information from id number for further validation
        separate_id = id_number.split(id_number[6])
        day_month_year = re.findall('..', separate_id[0])
        id_end = re.findall('.{1,3}', separate_id[1])
        individual_number = id_end[0]
        check_character = id_end[1].upper()
        birthdate_individual_number = int(separate_id[0] + individual_number)
        individual_number = int(individual_number) #convert to number for testing purposis

        check_number = round(((birthdate_individual_number / 31) % 1) * 31)
        if check_table[check_number] != check_character:
            print('Not valid id - identity code is wrong')
            continue

        #Is male or female?
        if individual_number % 2 == 0:
            gender = 'female'
        else : 
            gender = 'male'

        #Born in 18 or 19 or 20 century? 
        if id_number[6] == '+':
            century = '18'
        elif id_number[6] == '-':
            century = '19'
        else:
            century = '20'

        day = day_month_year[0]
        month = day_month_year[1]
        year = century + day_month_year[2]

        print(day, '.', month, '.', year)
        print('Gender: ', gender)
