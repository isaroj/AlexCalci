import sys
sys.path.append("/pyprojects/")
import pyprojects
from pyprojects.mathy import *
print(responses[0])
print(responses[1])
while True:
 print()
 text=input("Ask question to AlexCalci: ")
 try:
     print(eval(text))
     continue
 except:   
  for word in text.split(" "):
     if word.upper() in operations.keys():
         try:
             l=extract_numbes_from_text(text)
             r=operations[word.upper()](l[0],l[1])
             print(r)
         except:
             print("Something is wrong!! Please retry!")
         finally:
             break
     elif word.upper() in commands:
         commands[word.upper()]()
         break
     elif word.upper() in singleops.keys():
             l1=extract_numbes_from_text(text)
             r1=singleops[word.upper()](l1[0])
             print(r1)    
 else:
      sorry()
            
