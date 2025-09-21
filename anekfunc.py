"""Apologies, this code is hard to follow because of the use of numeric symbols. """

class gamevals:

    def __init__(self):

        self.njp=["","Mark(merchant)","Precious Metal","George(knight)","Old Gem","Map","Gem of Man","Maria(Princess)","Herb","Mineral","Robin(thief)","Gem of Forest","Dragon","Dragon's Nail","Gem of Dragon","Gem of God","Gem of Sky","Gem of Earth","Coin","Vulture","Antique Merchant","Farmer","Priest","",""]
        self.plname=["Can't go","Entrance of The Town","Public Square","Antique Market","Inn","Highway","Highway","Entarnce of the Village","Vegitable Field","Farm House","Wilderness","Wilderness","Ruin","Wilderness","Cave","Highway","Entrance of the Mountain","Forest Path","Mountain Path","Pass","Shrine","Nest of Vulture","Cliff Path","Top of the Mountain","Forest","Forest","Forest","Forest","Forest","Forest","",""]
        """pos:99=hidden 50=players possesion"""
        self.pos=[0,15,99,4,99,99,99,18,99,99,29,99,14,99,99,99,99,99,99,21,3,9,20,0]
        self.mapfw=[0,5,0,0,2,6,15,0,0,0,0,13,11,14,0,24,17,18,0,22,0,0,23,0,25,29,28,0,0,0,0,0]
        self.maprt=[0,2,3,0,0,0,7,8,9,0,6,10,0,0,0,16,0,0,19,20,0,22,0,0,0,0,25,26,0,0,0,0]
        self.maplt=[0,0,1,2,0,0,10,6,7,8,11,0,0,0,0,0,15,0,0,18,19,0,21,0,0,26,27,0,0,0,0]
        self.mapbk=[0,0,4,0,0,1,5,0,0,0,0,12,0,11,13,6,0,16,17,0,0,0,19,22,15,24,0,0,26,25,0,0]
        self.person=[0,1,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,1,1,0,0]
        self.pl=1
        self.gold=0
        self.gameflag=1
        self.mapdisp=False

def move(gs,func,dir):

    if func>0:
        print("You go "+str(dir)+".")
        gs.pl=func
    else:
        print("You can not go this direction.")

    return gs

def search(gs):

    if gs.pl==28 and gs.pos[10]==50 and gs.pos[11]==99:
        print("Robin found a (Gem of forest).")
        gs.pos[11]=50
    elif gs.pl==27 and gs.pos[7]==50 and gs.pos[8]==99:
        print("Maria found a (Herb).")
        gs.pos[8]=50
    elif gs.pl==22 & gs.pos[9]==99:
        print("You found a piece of (Mineral).")
        gs.pos[9]=50
    elif gs.pl==12 and gs.pos[10]==50 and gs.pos[4]==99:
        print("Robin found a (Old gem).")
        gs.pos[4]=50
    elif gs.pl==12 and gs.pos[10]==50 and gs.pos[2]==99:
        print("Robin found a piece of (Precious matal).")
        gs.pos[2]=50
    else:
        print("You can found nothing special.")
    if gs.pos[4]==50 and gs.pos[6]==50 and gs.pos[11]==50 and gs.pos[14]==50 and gs.pos[15]==50 and gs.pos[16]==50 and gs.pos[17]==50:
        print("You solve the game Anekgard!")
        gs.gameflag=0

    return gs

def report(gs):

    mes="Fellow:"
    for i in range(1,22):
        if gs.pos[i]==50 and gs.person[i]==1:
            mes=mes+ gs.njp[i]+" "
    print(mes)
    mes="Inventory:"
    for i in range(1,22):
        if gs.pos[i]==50 and gs.person[i]==0:
            mes=mes+gs.njp[i]+" "
    print(mes)
    mes="Coin  " + str(gs.gold) +""
    print(mes)

    return gs

def map(gs):

    print("[ Map ]") 
    print("       [North]:"+gs.plname[gs.mapfw[gs.pl]])
    print("[West]:"+gs.plname[gs.maplt[gs.pl]]+" [East]:"+gs.plname[gs.maprt[gs.pl]])
    print("       [South]:"+gs.plname[gs.mapbk[gs.pl]])

    return gs

def fight(gs):

    if gs.pl==14 and gs.pos[3]==50 and gs.pos[12]==14:
        print("Dragon flew away to avoid your attack.")
        print("It leaves a Nail of dragon and Gem of dragon.")
        gs.pos[12]=99
        gs.pos[13]=50
        gs.pos[14]=50
    if gs.pl==14 and gs.pos[3]!=50:
        print("Enemy defences!")
    if gs.pl==21:
        print("Enemy defences!")
    if gs.pl==3 or gs.pl==9 or gs.pl==10 or gs.pl==4 and gs.pos[3]==4 or gs.pl==15 and gs.pos[1]==15 or gs.pl==29 and gs.pos[10]==29 or gs.pl==18 and gs.pos[7]==18:
        print("You don't permitted to attack an innocent people.")
    if gs.pos[4]==50 and gs.pos[6]==50 and gs.pos[11]==50 and gs.pos[14]==50 and gs.pos[15]==50 and gs.pos[16]==50 and gs.pos[17]==50:
        print("You solve game Anekgard!")
        gs.gameflag=0

    return gs

def talk(gs):

    if gs.pl==3 and gs.pos[2]==50:
        print("You sell a Precious metal.")
        gs.pos[2]=0
        gs.gold=gs.gold+1
    if gs.pl==3 and gs.pos[8]==50:
        print("You sell a Herb.")
        gs.pos[8]=0
        gs.gold=gs.gold+1
    if gs.pl==3 and gs.pos[9]==50:
        print("You sell a Mineral.")
        gs.pos[9]=0
        gs.gold=gs.gold+1
    if gs.pl==3 and gs.pos[13]==50:
        print("You sell a Nail of dragon.")
        gs.pos[13]=0
        gs.gold=gs.gold+1
    if gs.pl==3 and gs.pos[1]==50 and gs.pos[6]==99 and gs.gold>0 and gs.pos[1]==50:
        print("You get a Gem of man with Mark's negotiation.")
        gs.pos[6]=50
        gs.gold=gs.gold-1
    if gs.pl==4 and gs.pos[3]==4:
        print("George join you.")
        gs.pos[3]=50
    if gs.pl==9 and gs.pos[17]==99 and gs.gold>0 and gs.pos[1]==50:
        print("You get a Gem of earth with Mark's negotiation.")
        gs.pos[17]=50
        gs.gold=gs.gold-1
    if gs.pl==15 and gs.pos[1]==15:
        print("Mark join you")
        gs.pos[1]=50
    if gs.pl==18 and gs.pos[7]==18:
        print("Maria join you.")
        gs.pos[7]=50
    if gs.pl==20 and gs.pos[15]==99 and gs.pos[7]==50:
        print("You get a Gem of god with Maria's negotiation.")
        gs.pos[15]=50 
    if gs.pl==21 and gs.pos[16]==99 and gs.pos[7]==50:
        print("You get a Gem of sky with Maria's negotiation.")
        gs.pos[16]=50
    if gs.pl==29 and gs.pos[10]==29:
        print("Robin join you.")
        gs.pos[10]=50
    if gs.pos[4]==50 and gs.pos[6]==50 and gs.pos[11]==50 and gs.pos[14]==50 and gs.pos[15]==50 and gs.pos[16]==50 and gs.pos[17]==50:
        print("You solve Game Anekgard !")
        gs.gameflag=0

    return gs

def cmdexe(gs,stginp):

    if stginp=="n":
        func=gs.mapfw[gs.pl]
        dir="north"
        gs=move(gs,func,dir)
    if stginp=="s":
        func=gs.mapbk[gs.pl]
        dir="south"
        gs=move(gs,func,dir)
    if stginp=="e":
        func=gs.maprt[gs.pl]
        dir="east"
        gs=move(gs,func,dir)
    if stginp=="w":
        func=gs.maplt[gs.pl]
        dir="west"
        gs=move(gs,func,dir)
    if stginp=="a":
        gs=fight(gs)
    if stginp=="r":
        gs=search(gs)
    if stginp=="t":
        gs=talk(gs)
    if stginp=="c":
        gs=report(gs)
    if stginp=="m":
        if gs.mapdisp==True:
            gs.mapdisp=False
        else:
            gs.mapdisp=True
    if stginp=="q":
        gs.gameflag=0

    return gs

def conds(gs):

    print("You are at the " + gs.plname[gs.pl])
    for i in range(1,21):
        if gs.pos[i]==gs.pl:
            print("There is "+gs.njp[i] + "")
    mes="You can go ["
    if gs.mapfw[gs.pl]>0:
        mes+= "north "
    if gs.maprt[gs.pl]>0:
        mes+= "east "
    if gs.maplt[gs.pl]>0:
        mes+= "west "
    if gs.mapbk[gs.pl]>0:
        mes+= "south "
    mes=mes+"]"
    print(mes)

gv=gamevals()
while gv.gameflag==1:
    if gv.mapdisp==True:
        map(gv)
    conds(gv)
    print("command[nsew r:research a:attack t:talk c:condition m:map q:quit game]")
    inp=input(":")
    gv=cmdexe(gv,inp)



