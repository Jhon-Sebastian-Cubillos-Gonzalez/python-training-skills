def stones(number:int):
  """
  We are making n stone piles! The first pile has n stones.
  If n is even, then all piles have an even number of stones.
  If n is odd, all piles have an odd number of stones.
  Each pile must more stones than the previous pile but as few as possible.
  Write a Python program to find the number of stones in each pile.

  >>> stones(2)
  [2, 4]

  >>> stones(10)
  [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

  >>> stones(4)
  [4, 6, 8, 10]

  >>> stones(17)
  [17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
  """
  return [x for x in range(number, number + (number) * 2, 2)]

def ChecksubString(strlist:str):
  """
  Write a Python program to check the nth-1 string is a proper substring of nth
  string in a given list of strings.

  >>> ChecksubString(['a', 'abb', 'sfs', 'oo', 'de', 'sfde'])
  True

  >>> ChecksubString(['a', 'abb', 'sfs', 'oo', 'ee', 'sfde'])
  False

  >>> ChecksubString(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew'])
  False

  >>> ChecksubString(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew'])
  True

  >>> ChecksubString(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'amigos', 'amigos de alma'])
  True

  >>> ChecksubString(['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'amiguis', 'amigos de alma'])
  False
  """
  return True if strlist[-1].count(strlist[-2]) > 0 else False

def CountNumbers(numbers:int):
  """
  Write a Python program to test a list of one hundred integers between 0 and 999,
  which all differ by ten from one another. Return true or false.

  >>> CountNumbers([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990])
  True

  >>> CountNumbers([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 720, 740, 760, 780, 800, 820, 840, 860, 880, 900, 920, 940, 960, 980])
  False
  """
  
  if not len(numbers) == 100:
    return False
  
  for i in range(1,len(numbers)):
    if not numbers[i] - numbers[i - 1] == 10:
      return False
  
  return True

def SumCheck(numbers:int):
  """
  Write a Python program to check a given list of integers where the sum of
  the first i integers is i

  >>> SumCheck([0, 1, 2, 3, 4, 5])
  False

  >>> SumCheck([1, 1, 1, 1, 1, 1])
  True

  >>> SumCheck([2, 2, 2, 2, 2])
  False
  """
  return False if numbers[0] == 0 else sum(numbers[0:numbers[0]]) == numbers[0]

def Spliter(phrase:str):
  """
  Write a Python program to split a string of words separated by commas and
  spaces into two lists,words and separators.

  >>> Spliter('W3resource Python, Exercises.')
  [['W3resource', 'Python', 'Exercises.'], [' ', ', ']]

  >>> Spliter('The dance, held in the school gym, ended at midnight.')
  [['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]

  >>> Spliter('The colors in my studyroom are blue, green, and yellow.')
  [['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'], [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]
  """
  return [
    phrase.replace(', ',' ').replace(',',' ').split(' '),
    list(
      map(
        lambda j: ', ' if j == ',' else j ,
        [x for x in list(phrase.replace(', ',',')) if x in [',',' ']]
      )
    )
  ]

def DistinctValues(numbers:int):
  """
  Write a Python program to find list integers containing exactly four distinct
  values, such that no integer repeats twice consecutively among the first
  twenty entries.

  >>> DistinctValues([1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4])
  True

  >>> DistinctValues([1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3])
  False

  >>> DistinctValues([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
  False
  """
  return all([numbers[i] != numbers[i + 1] for i in range(10)]) and len(set(numbers)) == 4

def GetstrLen(strlist:str):
  """
  Write a Python program to find the lengths of a given list of non-empty strings.

  >>> GetstrLen(['cat', 'car', 'fear', 'center'])
  [3, 3, 4, 6]

  >>> GetstrLen(['cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''])
  [3, 3, 7, 5, 2, 4, 0]
  """
  return [len(x) for x in strlist]

def MaxWords(strlist:str):
  """
  Write a Python program find the longest string of a given list of strings.

  >>> MaxWords(['cat', 'car', 'fear', 'center'])
  'center'

  >>> MaxWords(['cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''])
  'shatter'
  """
  return max(strlist, key = len)

def FindConicidence(strtup:str):
  """
  Write a Python program find the strings in a given list containing a given substring.

  >>> FindConicidence([('ca',('cat', 'car', 'fear', 'center'))])
  ['cat', 'car']

  >>> FindConicidence([('o',('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))])
  ['dog', 'donut', 'todo']

  >>> FindConicidence([('oe',('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))])
  []
  """
  return list(
    filter(
      lambda x: x.count(strtup[0][0]) > 0,
      strtup[0][1]
    )
  )

def NonNegative(number:int):
  """
  Write a Python program to create string consisting of the non-negative
  integers up to n inclusive.

  >>> NonNegative(4)
  '0 1 2 3 4'

  >>> NonNegative(15)
  '0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
  """
  return ' '.join([str(x) for x in range(number + 1)])

def FindInMatrix(matrix:int):
  """
  An irregular/uneven matrix, or ragged matrix, is a matrix that has a different
  number of elements in each row. Ragged matrices are not used in linear algebra,
  since standard matrix transformations cannot be performed on them, but they are
  useful as arrays in computing.Write a Python program to find the indices of all
  occurrences of target in the uneven matrix.

  >>> FindInMatrix([([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]),19])
  [[0, 4], [1, 0], [1, 3], [4, 1]]

  >>> FindInMatrix([([1, 2, 3, 2], [], [7, 9, 2, 1, 4]),2])
  [[0, 1], [0, 3], [2, 2]]
  """
  return [
    [r,l] for r, row in enumerate(matrix[0]) for l, n in enumerate(row) if n == matrix[1]
  ]

def SplitWords(word:str):
  """
  Write a Python program to split a given string (s) into strings if there is a
  space in the string, otherwise split on commas if there is a comma, otherwise
  return the list of lowercase letters with odd order (order of a = 0, b = 1, etc.)

  >>> SplitWords('a b c d')
  ['a', 'b', 'c', 'd']

  >>> SplitWords('a,b,c,d')
  ['a', 'b', 'c', 'd']

  >>> SplitWords('abcd')
  ['b', 'd']
  """
  return list(
    dict.fromkeys(
      list(
        word.replace(' ','')
      )
    )
  ) if word.count(' ') > 0 else list(
    dict.fromkeys(
      list(
        word.replace(',','')
      )
    )
  ) if word.count(',') > 0 else [
    word[i] for i in range(len(word)) if i % 2 == 1
  ]

def Increasing_Decreasing(numbers:int):
  """
  Write a Python program to determine the direction ('increasing' or 'decreasing')
  of monotonic sequence numbers.

  >>> Increasing_Decreasing([1, 2, 3, 4, 5, 6])
  'Increasing'

  >>> Increasing_Decreasing([6, 5, 4, 3, 2, 1])
  'Decreasing'

  >>> Increasing_Decreasing([19, 19, 5, 5, 5, 5, 5])
  'Not a monotonic sequence!'
  """
  return 'Increasing' if all(
    [numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)]
  ) else 'Decreasing' if all(
    [numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1)]
  ) else 'Not a monotonic sequence!'

def IsolatedLetter(strlist:str):
  """
  Write a Python program to check, for each string in a given list, whether the last
  character is an isolated letter or not. Return True or False.

  >>> IsolatedLetter(['cat', 'car', 'fear', 'center'])
  [False, False, False, False]

  >>> IsolatedLetter(['ca t', 'car', 'fea r', 'cente r'])
  [True, False, True, True]
  """
  return [x[-2] == ' ' and not x[-1] == ' ' for x in strlist]

def SumASCII(phrase:str):
  """
  Write a Python program to compute the sum of the ASCII values of the upper-case
  characters in a given string.

  >>> SumASCII('PytHon ExerciSEs')
  373

  >>> SumASCII('JavaScript')
  157
  """

  return sum(
    [ord(x) for x in phrase if x.isupper()]
  )

def IndexDrops(numbers:int):
  """
  Write a Python program to find the indices for which the numbers in the list drops.

  >>> IndexDrops([0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0])
  [1, 4, 6, 8, 10, 11, 15, 16, 18]

  >>> IndexDrops([1, 19, 5, 15, 5, 25, 5])
  [0, 2, 4, 6]

  >>> IndexDrops([6, 5, 4, 3, 2, 1])
  [1, 2, 3, 4, 5]
  """
  return [ x for x in range(len(numbers)) if numbers[x] < numbers[x - 1]]

def ListOfMax(numbers:int):
  """
  Write a Python program to create a list whose ith element is the maximum of
  the first i elements from a input list.

  >>> ListOfMax([0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0])
  [0, 0, 3, 8, 8, 9, 9, 14, 14, 14, 14, 14, 14, 17, 41, 41, 41, 41, 41, 41]

  >>> ListOfMax([6, 5, 4, 3, 2, 1])
  [6, 6, 6, 6, 6, 6]

  >>> ListOfMax([1, 19, 5, 15, 5, 25, 5])
  [1, 19, 19, 19, 19, 25, 25]
  """
  return [max(numbers[:i]) for i in range(1, len(numbers) + 1)]