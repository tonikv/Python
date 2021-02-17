"""
Make a program, which asks the user a string of integers, which can be separated by any character or characters (space, comma, semicolon etc.). 
The program will then calculate the sum, mean and median of the inputted values in 1-digit precision. 
E.g. valid input could be “1, 2, 3” and the sum would be 6, mean would be 2 and median would be 2. 
Or the valid input could be "123, -5 13;-1 and 10" and the sum would be 140, mean would be 28.0 and median would be 10.0.

Hint: Use regular expressions and look what services the standard library offers.
"""

import re
from statistics import median 

# Luetaan syöte käyttäjältä ja poimitaan syötteestä numerot eroteltuna millä tahansa merkillä. Etumerkki "-" hyväksytään jotta saadaan negatiiviset numerot.
numbers = input('give numbers separated with any character or characters: ')
numbers_array_str = re.findall(r'[-]?[0-9]+', numbers)

# jos ei ole annettu hyväksyttäviä syötteitä ilmoitetaan asiasta. Muutoin lasketaan ja tulostetaan arvot näytölle.
if len(numbers_array_str) == 0:
    print('You havent given any numbers. Cannot calculate')
else:
    numbers_array_int = [int(i) for i in numbers_array_str] # muokataan syöte luvuiksi laskelmia varten
    sum_result = sum(numbers_array_int)
    mean_result = sum_result / len(numbers_array_int)
    median_result = median(numbers_array_int)
    print('sum: ', sum_result)
    print('mean: ', "{:.1f}".format(mean_result)) # Näytetään yhden desimaalin tarkkudella. Voisi käyttää myös pyöristyksen tekevää round komentoa.
    print('median: ', "{:.1f}".format(median_result))