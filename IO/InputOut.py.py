"""
Make a program, which asks URL from the user. 
If the URL can be opened, write the URL contents into a local file path defined by the user. 
Use binary mode and check that file writing succeeds. The program should not fail if given URL cannot be found.
"""

from urllib.request import urlopen, URLError, HTTPError
import pickle

# Kysytään käyttäjältä osoitetta kunnes oikeassa muodossa ja saavutettava osoite löytyy
def read_url():
    while True:
        url = input('Give URL address: ')
        try:
            with urlopen(url) as response:
                data = response.read()
                return data
        except ValueError as e:
            print('error: ', e)
        except URLError as e:
            print('error: ', e)
        except HTTPError as e:
            print('error: ', e)
        
def save_data(data):
    while True:
        file_path = input('Give file path for saving: ') + 'file' # Käyttäjän haluama tallennuspolku
        try:
            with open(file_path, "wb") as outfile: # tallenetaan tiedosto binaarimuodossa
                pickle.dump(data, outfile)
                print('file saved to', file_path)
                break
        except OSError as e:
            print('error: ', e)

#Ohjelman ajo
save_data(read_url())