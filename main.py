'''main program functions'''
vowels=["a","e","i","o","u"]
#function checkwords(wordlist) is the function that uses selection statements to see how each word in the list should be treated when translated
def checkwords(wordlist):
  for wordindex in range(len(wordlist)): #loop through the list of words
    lastcharacter=wordlist[wordindex][len(wordlist[wordindex])-1]#store the last character
    if lastcharacter=="," or lastcharacter==";" or lastcharacter=="." or lastcharacter=="!" or lastcharacter=="?" or lastcharacter==":":#this ensures that punctuation does not move in the word
      punctuation=lastcharacter
      wordlist[wordindex]=wordlist[wordindex].replace(punctuation, "")
      wordlist[wordindex]=piglatinify(wordlist[wordindex])
      wordlist[wordindex]+=punctuation
    else: #for normal words, just translate
        wordlist[wordindex]=piglatinify(wordlist[wordindex])
    if wordindex==0:#first word should be translated and capitalized
      wordlist[wordindex]=wordlist[wordindex].capitalize()
  #print(wordlist)

#function piglatinify rotates the word left and adds "ay" to the end. if the word begins with a vowel, just add "ay" to it
def piglatinify(string):
  global vowels
  if string[0].lower() not in vowels:
    wordarray=buildarray(string)
    firstletter=wordarray.pop(0)
    wordarray.append(firstletter)
    return buildstring(wordarray)+"ay"
  else:
    return string+"ay"

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
checkwords(wordList) #this checks each word for punctuation and then inside calls piglatinify to translate
print("")
print("The translated PigLatin sentence is: ")
finalsentence=" ".join(wordList)
print(finalsentence)