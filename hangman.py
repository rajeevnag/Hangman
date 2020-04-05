def printWord(word,letters):
    endResult = ''
    for i in word.lower():
        if letters[i] == True:
            endResult += i
        else:
            endResult += ' _ '
    print(endResult)

def getLength(word,letters):
    num = 0
    for i in word.lower():
        if letters[i] == True:
            num += 1
    return num

def populateSet(lettersInWord,word):
    for c in word:
        if c not in lettersInWord:
            lettersInWord.add(c)

def checkIfInWord(c,lettersInWord):
    if c not in lettersInWord:
        return False
    return True

from urllib.request import urlopen as urlReq
from bs4 import BeautifulSoup as soup
url_of_words = "https://www.ef.edu/english-resources/english-vocabulary/top-1000-words/"

uClient = urlReq(url_of_words)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
wordsHtml = page_soup.body.find("div",{"class":"field-item even"})
wordsHtml = wordsHtml.find_all('p')[1]
wordsHtml = wordsHtml.get_text()

list_of_words = list(wordsHtml.split('\n\t'))

from random import seed
from random import random

currWord = str()

while len(currWord) < 3:  #get at least a word of size 4 to make game more fun
    random_num = float(random() * (len(list_of_words)-1)) 
    currWord = list_of_words[int(random_num)]
    
print('Welcome to Hangman')

word = currWord
#intialize list of letters to add to dictionary
letters = list()
dictionary = dict()
for c in "abcdefghijklmnopqrstuvwxyz":
    letters.append(c)

for i in letters:
    dictionary[i] = False


length = getLength(word,dictionary)
print('You get 5 chances to guess correctly')
printWord(word,dictionary)
mistakes = int(len(wordsHtml)*1.5)

lettersInWord = set()
#populate lettersInWord
populateSet(lettersInWord,word)

while(length != len(word) and mistakes != 0):
    print('Enter a character')
    c = input()
    yesNo = checkIfInWord(c,lettersInWord)
    if yesNo == False: #the letter is not in the word
        mistakes -=1
        print('You have ' + str(mistakes) + ' chances left')

    dictionary[c.lower()] = True
    printWord(word,dictionary)
    length = getLength(word,dictionary)
if mistakes != 0:
    print("Congrats, you've won!")
else:
    print("Sorry, you've failed...")
    print("Your word was: " + word)
    print()