#GNU nano 6.2                                                                         sub2.py
import requests
import os
END = "\033[0m"
RED = "\033[0;31m"
BLUE = "\033[0;34m"
GREEN = "\033[0;32m"
os.system("clear")
print(GREEN,"-"*64)
print("""

   .dMMMb  dMP dMP dMMMMb
  dMP" VP dMP dMP dMP"dMP
  VMMMb  dMP dMP dMMMMK"
dP .dMP dMP.aMP dMP.aMF
VMMMP"  VMMMP" dMMMMP"

    dMMMMb  dMP .dMMMb  .aMMMb  .aMMMb  dMP dMP dMMMMMP dMMMMb
   dMP VMP amr dMP" VP dMP"VMP dMP"dMP dMP dMP dMP     dMP.dMP
  dMP dMP dMP  VMMMb  dMP     dMP dMP dMP dMP dMMMP   dMMMMK"
 dMP.aMP dMP dP .dMP dMP.aMP dMP.aMP  YMvAP" dMP     dMP"AMF
dMMMMP" dMP  VMMMP"  VMMMP"  VMMMP"    VP"  dMMMMMP dMP dMP


""")
print("created by Max Johnson")
print("-"*64)
print("[+] 1 scan with buildin wordlist")
print("[+] 2 scan with your own wordlist")

def op1():
        print("enter your domain without http , https , www ")

        domain = input("[+] enter :")

#        wordlist = ["support","about","ftp","m","account"]
        wordlist = open("sub.txt").read()
        w2 = wordlist.splitlines()
        os.system("clear")
        print(GREEN,"-"*65)
        print("""

   .dMMMb  dMP dMP dMMMMb
  dMP" VP dMP dMP dMP"dMP
  VMMMb  dMP dMP dMMMMK"
dP .dMP dMP.aMP dMP.aMF
VMMMP"  VMMMP" dMMMMP"

    dMMMMb  dMP .dMMMb  .aMMMb  .aMMMb  dMP dMP dMMMMMP dMMMMb
   dMP VMP amr dMP" VP dMP"VMP dMP"dMP dMP dMP dMP     dMP.dMP
  dMP dMP dMP  VMMMb  dMP     dMP dMP dMP dMP dMMMP   dMMMMK"
 dMP.aMP dMP dP .dMP dMP.aMP dMP.aMP  YMvAP" dMP     dMP"AMF
dMMMMP" dMP  VMMMP"  VMMMP"  VMMMP"    VP"  dMMMMMP dMP dMP


""")
        print("-"*65)
        print("Max Johnson")
        for i in w2:
                dom = (f"https://{i}.{domain}")
                try:
                        requests.get(dom)
                except Exception as ex:
                        #pass
                        print(RED,"not found ",dom)
                else:
                        print(GREEN,"[+]",dom)
opn = str(input("enter your choice : "))
#__________________________________________


def op2():
    os.system("ls")
    wordlist = input("enter your wordlist path : ")
    print("-"*64)
    print("created by max johnson")
    print("simple subdomain finder")
    print("-"*64)
    domain = input("enter you domain without https , www : ")

    os.system("clear")
    w = open(wordlist).read()
    ws = w.splitlines()
    print("-"*65)
    print("""

   .dMMMb  dMP dMP dMMMMb
  dMP" VP dMP dMP dMP"dMP
  VMMMb  dMP dMP dMMMMK"
dP .dMP dMP.aMP dMP.aMF
VMMMP"  VMMMP" dMMMMP"

    dMMMMb  dMP .dMMMb  .aMMMb  .aMMMb  dMP dMP dMMMMMP dMMMMb
   dMP VMP amr dMP" VP dMP"VMP dMP"dMP dMP dMP dMP     dMP.dMP
  dMP dMP dMP  VMMMb  dMP     dMP dMP dMP dMP dMMMP   dMMMMK"
 dMP.aMP dMP dP .dMP dMP.aMP dMP.aMP  YMvAP" dMP     dMP"AMF
dMMMMP" dMP  VMMMP"  VMMMP"  VMMMP"    VP"  dMMMMMP dMP dMP


""")
    print("Max Johnson")
    print("-"*65)
    for i in ws:
       dom = (f"https://{i}.{domain}")
       try:
         requests.get(dom)
       except Exception as ex:
        #pass
        print(RED,"not found",dom)
       else:
         print(GREEN,"[+]",dom)

#-‐---------------‐--------------------------------------------------------

try:

        if opn=="1":
                op1()
        elif opn=="2":
                op2()
        else:
                print("you have entered worng option")

except FileNotFoundError:
        print("No such txt file")

print("good bye")
