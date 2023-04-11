import json
import random
import os
import urllib.request as req

class bcolors:
    green = '\033[92m' 
    yellow = '\033[93m' 
    red = '\033[91m' 
    RESET = '\033[0m' 

def creatdeta(url):
    request=req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read()
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    root1=root.find_all("li")
    data=list()
    for inf in root1:
        data+=[str(inf.a.string)]
    del data[0:10]
    return data

used_word=list()

def ifright(ans,guess,lv):
    iscorrect=0
    tmpstr=""
    for i in range(lv):
        if guess[i]==ans[i]:
            colora = bcolors.green + guess[i] + bcolors.RESET
            tmpstr += colora
            used_word[ord(guess[i])-97] = colora
            iscorrect+=1
        elif guess[i] in ans:
            colora = bcolors.yellow + guess[i] + bcolors.RESET
            tmpstr += colora
            used_word[ord(guess[i])-97] = colora
        else:
            tmpstr+=guess[i]
            used_word[ord(guess[i])-97] = bcolors.red + guess[i] + bcolors.RESET
    if iscorrect==lv:
        return "correct"
    else:
        return tmpstr

def play(ans,wincount,winstreak):
    notexist=False
    cnt=6
    guessrec=[""]
    used_word.clear()
    for i in range(ord("a"),ord("z")+1):
        used_word.append(chr(i))

    while True:
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()
        
        for i in range(1,7-cnt):
            print(guessrec[i])

        for i in range(cnt):
            for j in range(lv):
                print("□",end='')
            print()
        print()
        print("Win=",end='')
        print(int(wincount))
        print("Current Streak=",end='')
        print(int(winstreak))
        print("Enter stop to end the game")
        for i in range(13):
            print(used_word[i],end=' ')
        print()
        for i in range(13,26):
            print(used_word[i],end=' ')
        print()

        if notexist:
            print("The word is not available")

        x=input()
        if x in ["stop","0"]:
            return "stop"
        if x in data:
            cnt-=1
            tmp=ifright(ans,x,lv)
            if tmp=="correct":
                return "win"
            guessrec+=[tmp]
        else:
            notexist = True
        if cnt==0:
            clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            clearConsole()
            print("The answer is "+ans)
            any=input("Enter anything to continue")
            return "lose"

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clearConsole()
enter = True
while enter:
    lv=int( input("Enter length of the word(5 or 7):") )
    if lv==5:
        url="http://www.allscrabblewords.com/5-letter-words/"
    elif lv==7:
        url="http://www.allscrabblewords.com/7-letter-words/"
    else:
        print("Not Available\n")
        enter = True
        continue
    print("Please wait...")
    enter = False
data=creatdeta(url)

wincount=0
winstreak=0
while True :
    ans=random.choice(data)
    result=play(ans,wincount,winstreak)
    if result=="stop":
        break
    elif result=="win":
        wincount+=1
        winstreak+=1
    elif result=="lose":
        winstreak=0
    
