#Creating  is a dictionnary that hold a a morse code
morse_dictionnary={
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--','x': '-..-', 'y': '-.--',
    'z': '--..', '0': '-----','1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'

}
# Prompt the user to enter a sentence 
phrase = input('Enter a sentence: ')

# clean input by converting lower case and removing invalid characters to match the dictionnary keys.
def cleaned_input(phrase):
    phrase= phrase.lower()
    new_phrase= ''
    # loop through each characters in the phrase and filter valid ones
    for char in phrase:
        if char in morse_dictionnary:
            # if so, add valid character to new_phrase
            new_phrase += char

    return new_phrase
