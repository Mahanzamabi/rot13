#Import Libery
from time import sleep
from colorama import Fore,init

# debug colorama bug in windows

init()
#Get Text
print(Fore.CYAN+'') # add cyan color to input text
mytext = input('Enter Text:')

mytext = mytext.lower()

#Create Main Variable
Alphabet ='abcdefghijklmnopqrstuvwxyzabcdefghijklm'

listmaindata = []

listAlphabet = list(Alphabet)

# Funtion rot13 for decode and encode rot 13 text or main text

def rot13(text):
    for char in text:
        try:
            indexmychar = Alphabet.index(char)

            listmaindata.append(listAlphabet[indexmychar+13])
        except ValueError:
            listmaindata.append(char)
# run rot 13 funtion for add data to listmaindata 

rot13(mytext)         

#convert listmaindata to text 

maindata = ''.join(listmaindata)


print(Fore.GREEN+'Your Converted Text:',end=' ')
#Flush My Text
for char in maindata:
    print(char,end='')
    sleep(0.2)


