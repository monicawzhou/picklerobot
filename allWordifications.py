
# allWordifications.py is almost identical to numberToWords.py, except it takes as input a string representing a US phone number and outputs all possible "wordified" phone numbers (all possible combinations of numbers and English words in the input).
import json

# the json data of a dictionary of english words is from https://github.com/dwyl/english-words
data = {}
with open('words_dictionary.json') as json_file:
    data = json.load(json_file)

# this algorithm is a variation on finding the powerset of a set and finds all character subsequences possible from the input string and then using a O(1) dictionary lookup, checks if every subsequence is a valid English word
def all_wordifications(input):
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

  lenArray = []
  startIdx = [0,1]
  # fill the result list with all the possible letter conversions of the phone number
  for i in range(len(input)):
    # if a number maps to letters
    if input[i] in dict.keys():
      # grab all the possible letters that the number can map to
      letters = dict[input[i]]

      #store the number of letters each digit can map to
      lenArray.append(len(letters))

    else:
      letters = input[i]
      #store the number of letters each digit can map to
      lenArray.append(len(letters))


    # the following is a variation on finding the powerset, it finds all the subsequences of all the possible letter conversions

    #determine the starting index to add the new letter to (this is the major difference from finding the powerset, the powerset adds a character to all the existing characters in the result array, this algorithm will only add if the preceding character is correct)
    idx = startIdx[i-1]

    if i > 1:
      sum = 0
      for n in range(i-2,-1,-1):
        product = 1
        for a in range(i-2,n-1,-1):
          product*= lenArray[a]
        sum+=product
      idx +=sum
      startIdx.append(idx)


    for j in range(len(result)):
      for k in range(len(letters)):
        if j==0 or j>= startIdx[i]:
          word = result[j]+letters[k]
          result.append(word)


          # assume minimum length of word must be 3
          if len(word) > 2 and word in data.keys():
            output = phoneNumberWithWord(input, i-len(word)+1, word)
            print(output)
            final.append(output)

  return final



# prints out a phone number with a word starting at index
def phoneNumberWithWord(number, index, word):

  str = number[0:index] + word + number[index+len(word):len(number)]
  # add dashes
  if(len(number)==11):
    str = '-'.join([str[:1], str[1:4], str[4:7], str[7:]])

  return str



print(all_wordifications("06690"))
print(all_wordifications("1-800-724-6837"))

