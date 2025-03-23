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
# create a function  to convert the cleaned sentence into list of morse code
def conversion_to_morse(phrase):
    morse_list=[]
    for char in phrase:
        if char== ' ': 
            morse_list.append('//') # Mark word seperation (7 units)
        else:
            morse_list.append(morse_dictionnary[char]) # Add morse code for the character
            morse_list.append('///') # Add letter separation (3 unit)
        #delete the last  character in the list.
    if len(morse_list)> 0 and morse_list[-1] == '///': #this checks if the list is not empty and the last character in the list is ///.
            morse_list.pop()#if so, this will delete de last character from the list to avoid extra separator at end.
    return morse_list

cleaned_phrase= cleaned_input(phrase)
result= conversion_to_morse(cleaned_phrase)
print(result)

