""" 
    Make a simple dictionary application, which can save the dictionary in JSON format.
    The user can search words from the dictionary. If the word is found, it displays the translation. 
    if the word is not found, the program displays "Word not found. Please input a definition". 
    If user submits a definition, it adds a new word to this dictionary. 
    There should be a way to exit the application e.g. input an empty string.

    When the application is started it checks if the file containing the dictionary exists and will try to load the dictionary. 
    If loading fails, it starts with an inbuilt default dictionary, which might contain just few words. 
    The application must save the dictionary, including newly added words, when the user exits the application.
"""

import json

base_data = {"cat" : "kissa", "dog" : "koira", "mouse": "hiiri", "blue" : "sininen"};

# tutkitaan onko json tiedosto olemassa -> mikäli löytyy se ladataan ja palautetaan käyttäjälle
# jos tiedostoa ei löydy -> palautetaan käyttäjälle ohjelman sisäinen pikkusanakirja
def load_data():
    try:
        with open('data.json') as infile:
            data = json.load(infile)
            print('Dictionary loaded!')
            return data
    except OSError:
        print('Dictionary not loaded! Using inbuilt default dictionary')
        return base_data;

def save_data(file_to_save):
    try:
        with open('data.json', 'w') as outfile:
            json.dump(file_to_save, outfile, sort_keys=True, indent=4)
    except (OSError, ValueError):
            print('Could not save to file!')

# kysytään sanaa - mikäli tämä löytyy sanakirjasta -> tulostetaan käännös.
# jos sana ei ole sanakirjassa -> pyydetään antamaan käännös sanalle ja lisätään se sanakirjaan ja tallennetaan
def find_translation(dictionary_eng_fin):
    found_word = False;
    input_word = input('What word?: ')
    for key in dictionary_eng_fin.keys():
        if key == input_word:
            found_word = True
            print('Word', input_word, 'translation:',dictionary_eng_fin[key])
    if not found_word:
        definition = input('Word not found. Please input a definition: ')
        dictionary_eng_fin[input_word] = definition
        save_data(dictionary_eng_fin) #Tämä varmentaa tallennuksen, mikäli ohjelma suljetaan käyttöliittymän ulkopuolelta.

def text_ui(dictionary_eng_fin):
    print('English to Finnish dictionary')
    while True:
        print('Commands:');
        print('1 - Find translation');
        print('2 - Close program');
        input_word = input('Give command: ')
        if input_word == '1':
            find_translation(dictionary_eng_fin)
        if input_word == '2':
            print('Recording information and closing program')
            save_data(dictionary_eng_fin) 
            break;

# Käynnistä ohjelma
text_ui(load_data())