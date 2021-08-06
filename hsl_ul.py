"""the holy stone light unlimited version"""
"""a role-playing game"""
"""play : about 1 hour"""

import random
import pickle

ename=["","silver wolf","assasin","dark knight","fire lizard","ghost knight","dragon","giant lord","lesser devil","hell fire","heavy metal dragon"]
ehpmax=[0,20,50,100,200,300,1000,500,700,800,2000]
estr=[0,10,20,30,40,50,100,70,80,100,120]
epow=[0,10,20,30,40,50,100,70,80,100,120]
egold=[0,10,20,50,100,150,1000,500,700,1000,10000]
eexp=[0,10,30,50,70,100,1000,20000,30000,40000,100000]
weapon=["","dagger","axe","mace","short sword","sword","heavy mace","battle axe","dagger with jewels","giant axe","ichimonji sword"]
pow=[0,5,10,20,30,50,60,70,100,200,300]
wepg=[0,10,50,100,500,1000,2000,5000,10000,25000,50000]
armor=["","cloth","leather","chain mail","breast plate"]
mydef=[0,10,20,30,50]
amrg=[0,100,500,2000,5000]
lvl=[0,100,200,500,1000,2000,3000,4000,5000,7000,10000,100000,200000,400000,1000000,10000000]

class gamevals:

    def __init__(self):
        self.mapmode="off"
        self.myname="player"
        self.myhp=100
        self.myhpmax=100
        self.mystr=30
        """dex:dagger, mace, axe, sword"""
        self.mydex=[0,10,10,10,10]
        self.mywep=1
        self.myamr=1
        self.myluck=10
        self.mygold=100
        self.myexp=0
        self.mylvl=0
        self.mx=2
        self.my=2
        self.enum=0
        self.ehp=0
        self.gameflag=True
        self.bonusgame=False
        self.cmdmode="maze"
        self.gs=maze()

class gamestate:

    def __init__(self):
        self.map=[]

    def prompt(self,gv):
        if gv.mapmode=="on":
            for i in range(-2,3):
                str=""
                for j in range(-2,3):
                    if i==0 and j==0:
                        str=str+"O"
                    elif self.getm(gv.mx+j,gv.my+i)==1:
                        str=str+"+"
                    elif self.getm(gv.mx+j,gv.my+i)==2:
                        str=str+"?"
                    else:
                        str=str+"#"
                print(str)
        str=""
        if self.getm(gv.mx,gv.my-1)>=1:
            str=str+"north "
        if self.getm(gv.mx,gv.my+1)>=1:
            str=str+"south "
        if self.getm(gv.mx+1,gv.my)>=1:
            str=str+"east "
        if self.getm(gv.mx-1,gv.my)>=1:
            str=str+"west "
        print("you can go ["+str+"]")

    def report(self,gv):
        print()
        print("[report]")
        print("name:"+str(gv.myname))
        print("HP:"+str(gv.myhp)+"  STR:"+str(gv.mystr))
        print("weapon:"+str(weapon[gv.mywep])+", armor:"+str(armor[gv.myamr]))
        print("level:"+str(gv.mylvl)+" exp:"+str(gv.myexp))
        print("gold:"+str(gv.mygold))
        print()

    def getm(self,x,y):
        return self.map[y*12+x]

class battle:

    def battle(self,gv):
        bsum=gv.mystr+estr[gv.enum]
        r=random.randint(0,bsum)
        if r<gv.mystr:
            print("you hit!")
            dmg=random.randint(0,pow[gv.mywep])
            gv.ehp=gv.ehp-dmg
            print(str(dmg)+" damages Enemy HP:"+str(gv.ehp))
            if gv.ehp<=0:
                print("you win!")
                print("you got "+str(eexp[gv.enum])+"exp and "+str(egold[gv.enum])+"gold")
                gv.myexp=gv.myexp+eexp[gv.enum]
                gv.mygold=gv.mygold+egold[gv.enum]
                gv.cmdmode="maze"
                if gv.enum==6:
                    print("you got the holy stone!")
                    print("*** game end ***")
                    gv.bonusgame=True
                    file=open('enddata','wb')
                    pickle.dump(gv,file)
                    file.close()
                    gv.gameflag=False
        else:
            print("enemy hits!")
            dmg=random.randint(0,epow[gv.enum])
            if mydef[gv.myamr]<dmg:
                dmg=dmg-mydef[gv.myamr]
                gv.myhp=gv.myhp-dmg
            else:
                dmg=random.randint(0,5)
                gv.myhp=gv.myhp-dmg
            print(str(dmg)+ " damages Your HP:"+str(gv.myhp))
            if gv.myhp<=0:
                print("you lose...")
                gv.cmdmode="maze"
                gv.gameflag=False
        return gv

    def encount(self,gv):
        while gv.cmdmode=="battle":
            print(ename[gv.enum]+" HP:"+str(gv.ehp))
            inp=""
            while inp!="f" and inp!="e":
                inp=input("f)ight or e)scape:")
                if inp=="f":
                    gv=self.battle(gv)
                if inp=="e":
                    r=random.randint(0,20)
                    if r<=gv.myluck:
                        print("you escaped.")
                        gv.cmdmode="maze"
                    else:
                        print("you failed to escape.")
                        gv=self.battle(gv)
        return gv

class maze(gamestate):

    def __init__(self):
        self.map=[
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,2,1,1,1,1,1,1,1,0,0,
            0,0,1,0,0,0,0,0,1,0,0,0,
            0,0,1,1,1,1,1,0,1,2,0,0,
            0,0,1,0,0,0,1,0,0,0,0,0,
            0,0,1,0,1,1,1,0,2,1,0,0,
            0,0,1,0,0,0,0,0,0,1,0,0,
            0,0,1,0,1,0,1,1,1,1,0,0,
            0,0,1,1,1,1,1,0,0,1,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0]
        self.bt=battle()

    def initmsg(self,gv):
        if gv.bonusgame:
            print("[hell]")
        else:
            print("[maze]")
        self.prompt(gv)
        if gv.mapmode=="off":
            print("nsew:move r:report o:open map g:save game")
        else:
            print("nsew:move r:report c:close map g:save game")

    def event(self,gv):
        if self.getm(gv.mx,gv.my)==2:
            if gv.mx==2 and gv.my==2:
                print("there is a ladder to overground.")
                print("u:go up")
                inp=input(">")
                if inp=="u":
                    gv.mx=9
                    gv.my=9
                    gv.gs=town()
            if gv.mx==9 and gv.my==4:
                if not(gv.bonusgame):
                    if gv.mylvl<=1:
                        gv.enum=1
                    elif gv.mylvl<=3:
                        gv.enum=2
                    elif gv.mylvl<=5:
                        gv.enum=3
                    elif gv.mylvl<=7:
                        gv.enum=4
                    else:
                       gv.enum=5
                else:
                    r=random.randint(7,9)
                    gv.enum=r
                print("monster is looming...")
                gv.ehp=ehpmax[gv.enum]
                gv.cmdmode="battle"
                gv=self.bt.encount(gv)
            if gv.mx==8 and gv.my==6:
                print("< dragon's nest! >")
                if not(gv.bonusgame):
                    gv.enum=6
                else:
                    gv.enum=10
                gv.ehp=ehpmax[gv.enum]
                gv.cmdmode="battle"
                gv=self.bt.encount(gv)
        else:
            r=random.randint(0,5)
            if r==1:
                print("enemy appears...")
                if not(gv.bonusgame):
                    gv.enum=random.randint(1,5)
                else:
                    gv.enum=random.randint(7,9)
                gv.ehp=ehpmax[gv.enum]
                gv.cmdmode="battle"
                gv=self.bt.encount(gv)
        return gv

    def cmdexe(self,cmd,gv):
        if cmd=="n" and self.getm(gv.mx,gv.my-1)>=1:
            gv.my=gv.my-1
        if cmd=="s" and self.getm(gv.mx,gv.my+1)>=1:
            gv.my=gv.my+1
        if cmd=="e" and self.getm(gv.mx+1,gv.my)>=1:
            gv.mx=gv.mx+1
        if cmd=="w" and self.getm(gv.mx-1,gv.my)>=1:
            gv.mx=gv.mx-1
        if cmd=="r":
            self.report(gv)
        if cmd=="c" and gv.mapmode=="on":
            gv.mapmode="off"
        if cmd=="o" and gv.mapmode=="off":
            gv.mapmode="on"
        if cmd=="g":
            file=open("hsdata",'wb')
            pickle.dump(gv,file)
            file.close()
            print("game saved.")
        if cmd=="bonusgame":
            gv.bonusgame=True
            file=open("enddata","wb")
            pickle.dump(gv,file)
            file.close()
            gv.bonusgame=False
        else:
            gv=self.event(gv)
        return gv

class maze2f(maze):

    pass

class maze3f(maze):

    pass

class town(gamestate):

    def __init__(self):
        """weapon shop, armor shop, healer, oracle"""
        self.map=[
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,1,1,1,1,1,1,2,0,0,
            0,0,0,1,0,0,0,0,0,0,0,0,
            0,0,0,1,0,2,1,1,0,2,0,0,
            0,0,0,1,0,0,0,1,0,1,0,0,
            0,0,0,1,1,1,1,1,1,1,0,0,
            0,0,0,0,0,0,0,1,0,1,0,0,
            0,0,0,2,1,1,1,1,0,2,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0,
            0,0,0,0,0,0,0,0,0,0,0,0]

    def initmsg(self,gv):
        print("[town]")
        self.prompt(gv)
        if gv.mapmode=="off":
            print("nsew:move r:report l:sleep on the road o:open map")
        else:
            print("nsew:move r:report l:sleep on the road c:close map")

    def cmdexe(self,cmd,gv):
        if cmd=="n" and self.getm(gv.mx,gv.my-1)>=1:
            gv.my=gv.my-1
        if cmd=="s" and self.getm(gv.mx,gv.my+1)>=1:
            gv.my=gv.my+1
        if cmd=="e" and self.getm(gv.mx+1,gv.my)>=1:
            gv.mx=gv.mx+1
        if cmd=="w" and self.getm(gv.mx-1,gv.my)>=1:
            gv.mx=gv.mx-1
        if cmd=="r":
            self.report(gv)
        if cmd=="c" and gv.mapmode=="on":
            gv.mapmode="off"
        if cmd=="o" and gv.mapmode=="off":
            gv.mapmode="on"
        if cmd=="l":
            print("hp full recovered.")
            gv.myhp=gv.myhpmax
            r=random.randint(1,5)
            if r==1:
                r2=random.randint(1,3)
                if r2==1:
                    r3=random.randint(1,gv.mygold)
                    print(str(r3)+"gold was stolen.")
                    gv.mygold=gv.mygold-r3
                elif r2==2:
                    print("your weapon was stolen.")
                    gv.mywep=1
                else:
                    print("your armor was stolen.")
                    gv.myamr=1
        if gv.mx==5 and gv.my==5:
            shop="weapon"
            gv=self.shopdo(gv,shop)
        if gv.mx==3 and gv.my==9:
            shop="armor"
            gv=self.shopdo(gv,shop)
        if gv.mx==9 and gv.my==5:
            shop="healer"
            gv=self.shopdo(gv,shop)
        if gv.mx==9 and gv.my==3:
            shop="oracle"
            gv=self.shopdo(gv,shop)
        if gv.mx==9 and gv.my==9:
            print("there is a ladder to underground")
            print("d:go down")
            inp=input(">")
            if inp=="d":
                gv.mx=2
                gv.my=2
                gv.gs=maze()
        return gv

    def shop(self):
        pass

    def shopdo(self,gv,shop):
        """like haskell's io monad(chain)"""
        if shop=="weapon":
            print("[weapon shop]")
            print("hi, adventurer! what do you need?")
            stg=""
            if gv.bonusgame==False:
                wnum=8
            else:
                wnum=11
            for i in range(1,wnum):
                stg=stg+str(i)+":"+str(weapon[i])+"("+str(wepg[i])+"g) "
            print(str(stg))
            print("other:exit")
            inp=input(">")
            try:
                ninp=int(inp)
                if (ninp>=1 and ninp<=7) or (gv.bonusgame and ninp>=8 and ninp<=10):
                    if gv.mygold>wepg[ninp]:
                        print("you got "+str(weapon[ninp]))
                        gv.mygold=gv.mygold-wepg[ninp]
                        gv.mywep=ninp
                    else:
                        print("too expensive to buy")
                else:
                    print("see you next time.")
            except ValueError:
                print("you have input not a number thus exit the shop.")
        if shop=="healer":
            print("[healer]")
            print("oh...welcome. do you need help?")
            print("h:heal l:level up other:exit")
            inp=input(">")
            if inp=="h":
                hgold=(gv.mylvl+1)*20
                print(str(hgold)+" gold. OK?(y or other)")
                inp=input(">")
                if inp=="y":
                    if gv.mygold>=hgold:
                        print("your hp reaches max point.")
                        gv.myhp=gv.myhpmax
                    else:
                        print("your gold is not enough.")
                else:
                    print("good bye.")
            if inp=="l":
                if gv.mylvl<=14:
                    if gv.myexp>=lvl[gv.mylvl+1]:
                        gv.mylvl=gv.mylvl+1
                        print("level up!")
                        print("now your level is:"+str(gv.mylvl))
                        gv.myhpmax=gv.myhpmax+50
                        gv.myhp=gv.myhpmax
                        gv.mystr=gv.mystr+5
                    else:
                        print("you need "+str(lvl[gv.mylvl+1]-gv.myexp)+"exp to next level.")
                else:
                    print("you already became the sword master.")
        if shop=="oracle":
            print("[oracle]")
            print("welcome, adventurer.")
            print("f:fortunetelling m:magic charm other:exit")
            inp=input(">")
            if inp=="f":
                if gv.mywep==1:
                    print("you must get stronger weapon.")
                elif gv.mylvl<=1:
                    print("be careful with fire lizard and ghost knight!")
                elif gv.mylvl<=2:
                    print("do you find monster room?")
                else:
                    print("do you find dragon's nest? it is a goal.") 
            elif inp=="m":
                print("1000 gold payment for 1 luck point.")
                print("OK?(y or other)")
                inp=input(">")
                if inp=="y":
                    if gv.mygold>=1000:
                        print("your luck goes up.")
                        gv.myluck=gv.myluck+1
                        print("now your luck point is:"+str(gv.myluck))
                    else:
                        print("you have not enough gold.")
            else:
                print("good luck.")
        if shop=="armor":
            print("[armor shop]")
            print("hello! we have good stuff.")
            stg=""
            for i in range(1,5):
                stg=stg+str(i)+":"+armor[i]+"("+str(amrg[i])+"g) "
            print(str(stg))
            print("other:exit")
            inp=input(">")
            try:
                ninp=int(inp)
                if ninp>=1 and ninp<=4:
                    if gv.mygold>amrg[ninp]:
                        print("you got "+str(armor[ninp]))
                        gv.myamr=ninp
                    else:
                        print("too expensive to buy")
                else:
                    print("see you again!")
            except ValueError:
                print("you have input not a number thus exit the shop.")
        return gv

gv=gamevals()
gv.gs=maze()
print("l:load game other:new game")
inp=input(">")
if inp=="secretgame":
    try:
        file=open("enddata",'rb')
        gv=pickle.load(file)
        print("welcome to hell.")
    except FileNotFoundError:
        print("you do not end this game, so now we start a normal game.")
        gv.myname=input("type your name:")
elif inp=="l":
    try:
        file=open("hsdata",'rb')
        gv=pickle.load(file)
    except FileNotFoundError:
        print("I can not find save data thus start a new game")
        gv.myname=input("type your name:")
else:
    gv.myname=input("type your name:")
while gv.gameflag:
    gv.gs.initmsg(gv)
    inp=input("command:")
    gv=gv.gs.cmdexe(inp,gv)

