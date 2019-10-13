import json

data = {}
with open('words_dictionary.json') as json_file:
    data = json.load(json_file)




def number_to_words(input):
  input = str(input)
  #remove dashes
  input  = input.replace("-","")

  dict = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
  }



  result = ['']
  final = []
  # fill the result list with all the possible letter conversions of the phone number
  for i in range(len(input)):
    # if a number maps to letters
    if input[i] in dict.keys():
      # grab all the possible letters that the number can map to
      letters = dict[input[i]]

    else:
      letters = input[i]


    for j in range(len(result)):
      for k in range(len(letters)):
        result.append(result[j]+letters[k])

        #filter for only full length conversion (the returned array contains only letters and no numbers)
        if len(result[j]+letters[k]) == len(input):
          final.append(result[j]+letters[k])

  return final


def checkForWord(lst):
  for i in range(len(lst)):
    containsWord(lst[i])

def containsWord(str):

  for i in range(len(str)):
    return growingSubString(str[i:len(str)])


def growingSubString(str):

  for i in range(len(str)+1):
    # word must be longer than one character

    if len(str[0:i])>2 and str[0:i] in data.keys():
      print(str[0:i])

  return False








print(number_to_words("4355"))
lst = number_to_words("4355")
print(checkForWord(lst))
