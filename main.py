import random as rand
import secrets
from ast import literal_eval

print("1. Encrypt")
print("2. Decrypt")

encryptDecrypt = int(input())


def encrypt():

   encryptText = input("Text to encrypt: ")

   i = 0
   key = []

   #loops to generate a 32 bit integer and put it in a list
   while i < 32:
       key.append(rand.randint(1,9))
       i+=1

   keyList = []

   #puts key into a str 
   for element in key:
       keyList.append(str(element))
   
   keyStr = ''.join(keyList)

   #writes key to text file (maybe put it in the file itself somehow?)
   f = open("key.txt", "w")
   f.write(keyStr)

   #convert input text to list of characters
   encryptList = list(encryptText)

   i = 0
   encryptNum = []

   #converts the text into numerical values
   for len in encryptList:
       encryptNum.append(ord(encryptList[i]))
       i+=1

   i = 0
   j = 0
   final = []

   for len in encryptNum:
       if j > 32:
           j = 0
       final.append(hex(encryptNum[i] * key[j]))
       i+=1
       j+=1

   finalStr = " ".join(final)

   f2 = open("output.txt", "w")
   f2.write(finalStr)

def decrypt():

   decryptString = input("what to decrypt: ")
   #add file import

   decryptList = decryptString.split()

   f3 = open("key.txt", "r")
   key = f3.read()
   keyList = list(map(int, str(key)))

   i = 0

   decryptNum = []

   for len in decryptList:
       j = decryptList[i]
       decryptNum.append(int(j, 16))
       i+=1

   i = 0
   j = 0

   numList = []
   finalList = []

   for len in decryptList:

       if j > 31:
           j = 0

       numList.append(int(decryptNum[i] / keyList[j]))
       finalList.append(chr(numList[i]))
       i+=1
       j+=1

   final = "".join(finalList)
   print(final)
