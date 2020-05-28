from math import *
from datetime import *
responses=["Welcome to smart calculator","My name is AlexCalci","Thank you!!!!","sorry i am unable to process your request"]
def extract_numbes_from_text(text):
    _list=[]
    for t in text.split(" "):
        try:
             if type(eval(t))==int or type(eval(t))==int:
               _list.append(eval(t)) 
        except:
            pass
    return _list
def HCF(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1
def LCM(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
def percent1(a,b):
    return (b*(a/100))
def nat(n):
    l=[]
    x=range(1,n+1)
    for i in x:
        l.append(i)
    return l    
def evod(n):
    if n%2==0:
        return("It is an even number!")
    else:
        return ("It is a odd number!")
def prime(n):
    if n==2:
        return("Prime number")
    else:    
     x=range(2,ceil(n/2)+1)
     for i in x:
        if n%i==0:
            return("It is not a prime number!")
        else:
         return("It is a prime number!")
def sin1(n):
    return (sin(radians(n)))
def cos1(n):
    return (cos(radians(n)))
def tan1(n):
    return (tan(radians(n)))
def cot1(n):
    return (1/(tan(radians(n))))
def sec1(n):
    return (1/(cos(radians(n))))
def cosec1(n):
    return (1/(sin(radians(n))))
def add1(a,b):
    return (a+b)
def sub1(a,b):
    return (a-b)
def mul1(a,b):
    return (a*b)
def div1(a,b):
    return (a/b)
def mod1(a,b):
    return (a%b)
def comp(a,b):
    if a==b:
        return "equal"
    print("Not equal and greater number is")
    return a if a>b else b
def power(a,b):
    return pow(a,b)
def endcal():
    print(responses[2])
    input("Press any key to exit")
    exit()
def myname():
    print(responses[1])
def sorry():
    print(responses[3])
def greet():
    print("Hi i am your smart calculator AlexCalci")
def fine():
    print("I am fine thank you!! Hope you are doing great!")
def date():
    t=datetime.now()
    print(t.strftime("%d(%A) %m(%B), %Y"))
def time():
    t=datetime.now()
    print(t.strftime("%I:%M:%S:%p"))
operations={"ADD":add1,"ADDITION":add1,"PLUS":add1,"MINUS":sub1,"SUB":sub1,"SUBTRACTION":sub1
            ,"SUBTRACT":sub1,"MUL":mul1,"MULTIPLY":mul1,"DIVIDE":div1,"DIVISION":div1,"DIVISIBLE":div1,
            "DIV":div1,"MOD":mod1,"MODULOUS":mod1,"POW":power,"POWER":power,"TO THE POWER":power,
            "GREATER":comp,"SMALLER":comp,"COMPARE":comp,"MATCH":comp,"BIGGER":comp,
            "LARGER":comp,"EQUAL":comp,"HCF":HCF,"LCM":LCM,"PERCENT":percent1,"PERCENTAGE":percent1}
singleops={"EVEN":evod,"ODD":evod,"NATURAL":nat,"PRIME":prime,"SIN":sin1,"COS":cos1,"TAN":tan1,"COT":cot1,"SEC":sec1,
           "COSEC":cosec1}
commands={"NAME":myname,"NICK NAME":myname,"STOP":endcal,"EXIT":endcal,"CLOSE":endcal,"END":endcal
          ,"HI":greet,"HELLO":greet,"HOW":fine,"TIME":time,"DATE":date,"DAY":date,"MONTH":date,"YEAR":date,"BY":endcal}
