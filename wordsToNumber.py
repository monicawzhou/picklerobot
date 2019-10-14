# wordsToNumber.py converts a phone number that includes letters/words into numbers
#
# Example usage:
# print words_to_number("1-800-PAINTER")
# returns 1-800-724-6837


# takes an input a string representing a phone number that includes words/letters and converts it into all numeric digits
def words_to_number(str):
  #remove dashes
  str  = str.replace("-","")
  dict = {'A': '2', 'B': '2', 'C': '2',
          'D': '3', 'E': '3', 'F': '3',
          'G': '4', 'H': '4', 'I': '4',
          'J': '5', 'K': '5', 'L': '5',
          'M': '6', 'N': '6', 'O': '6',
          'P': '7', 'Q': '7', 'R': '7', 'S': '7',
          'T': '8', 'U': '8', 'V': '8',
          'W': '9', 'X': '9', 'Y': '9', 'Z': '9'}

  converted = ""

  # iterate over phone number and if a character in the dictionary is present, convert it to a number
  # otherwise leave it unmodified
  for i in range(len(str)):
    if str[i] in dict.keys():
      converted += dict[str[i]]
    else:
      converted += str[i]

  # add dashes
  if(len(converted)==11):
    converted = '-'.join([converted[:1], converted[1:4], converted[4:7], converted[7:]])

  return converted


print words_to_number("1-800-PAINTER")

