# picklerobot

To run any program:

    $ python NAMEOFPROGRAM

Example:

    $ python allWordifications.py
    

numberToWords.py takes as input a string representing a US phone number and outputs the first possible combination of numbers and an English word in a phone number that can be typed on a US phone. 
Example usage:
number_to_words("00006270000")
returns 0-000-map-0000

wordsToNumber.py converts a phone number that includes letters/words into numbers
Example usage:
words_to_number("1-800-PAINTER")
returns 1-800-724-6837

allWordifications.py is almost identical to numberToWords.py, except it takes as input a string representing a US phone number and outputs all possible "wordified" phone numbers (all possible combinations of numbers and English words in the input).
