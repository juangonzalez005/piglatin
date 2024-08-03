'''main program functions'''
vowels=["a","e","i","o","u"]
punctuation=[".",",","!","?"]
threeLetterCombinations= ["str", "thr", "spr", "sch", "scr", "shr", "spl", "squ", "str", "thr", "spr", "sch"]
twoLetterCombinations = ["bl", "br", "ch", "cl", "cr", "dr", "fl", "sw" "fr", "gl", "gr", "ph", "pl", "pr", "qu", "sc", "sh", "sk", "sl", "sm", "sn", "sp", "st", "th", "tr", "tw", "wh", "wr"]

#function CheckWords(wordlist) is the function that uses selection statements to see how each word in the list should be treated when translated 

def CheckWords(wordList):
  global punctuation
  for wordindex in range(len(wordList)):
    word = wordList[wordindex]
    lastCharacter = word[len(word)-1]
    if lastCharacter in punctuation:
      word = word[0:len(word)-1]
      word = PigLatinify(word)
      wordList[wordindex] = word + lastCharacter
    else:
      word = PigLatinify(word)
      wordList[wordindex] = word
    if wordindex == 0:
      wordList[0] = wordList[0].capitalize()

#function PigLatinify rotates the word left and adds "ay" to the end. if the word begins with a vowel, just add "ay" to it
def PigLatinify(string):
  global vowels
  global threeLetterCombinations
  global twoLetterCombinations

  for combi in threeLetterCombinations:
    if string.lower().startswith(combi):
      string = string[3:] + string[0:3] + "ay"
      return string.lower()
  for combi in twoLetterCombinations:
    if string.lower().startswith(combi):
      string = string[2:] + string[0:2] + "ay"
      return string.lower()

  if string[0].lower() not in vowels:
    string = string[1:] + string[0]
  return string.lower() + "ay"
    

'''simple helper functions'''
def buildstring(list): #converts array to string to help with manipulation
  finalstring=""
  for i in range(len(list)):
    finalstring = finalstring+list[i]
  return finalstring

def buildarray(string): #converts string to array to help with manipulation
  finalarray=[]
  for i in range(len(string)):
    finalarray.append(string[i])
  return finalarray

'''#main'''
sentence=input("Please input a complete sentence.\n")
wordList=sentence.split(" ")
#wordList is the list that holds each word from the sentence
CheckWords(wordList) #this checks each word for punctuation and then inside calls PigLatinify to translate
print("")
print("The translated PigLatin sentence is: ")
finalsentence=" ".join(wordList)
print(finalsentence)