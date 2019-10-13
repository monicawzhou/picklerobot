def numberToWords(input):
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
        # append letters only to the first element of the result list ('') and previous digit (not to everything currently in the result list)
        if i>0 and input[i-1] in dict.keys():
          lenPrev = len(dict[input[i-1]])
        else:
          lenPrev = 1
        lengthOfPrevDigit = len(letters)*lenPrev
        if j==0 or j>= (len(result)-lengthOfPrevDigit):
          print("result len", len(result))
          print(lengthOfPrevDigit)
          print(len(result)-lengthOfPrevDigit)

          result.append(result[j]+letters[k])
          print(result)
        #filter for only full length conversion (the returned array contains only letters and no numbers)
        if len(result[j]+letters[k]) == len(input):
          final.append(result[j]+letters[k])

  return final




print(numberToWords("2-3-4"))
