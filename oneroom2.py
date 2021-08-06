"""one room adventure for python command line"""

import random

class clockobj:

    def __init__(self):
        self.min=0
        self.hour=9
        self.sec=0

    def gettime(self):
        if self.hour<10:
            stg1="0"+str(self.hour)
        else:
            stg1=str(self.hour)
        if self.min<10:
            stg2="0"+str(self.min)
        else:
            stg2=str(self.min)
        if self.sec<10:
            stg3="0"+str(self.sec)
        else:
            stg3=str(self.sec)
        stg=""+stg1+":"+stg2+":"+stg3
        return stg

    def tick(self):
        self.sec=self.sec+random.randint(10,50)
        if self.sec>=60:
            self.sec=self.sec-60
            self.min=self.min+1
            if self.min>=60:
                self.min=self.min-60
                self.hour=self.hour+1
                if self.hour>=24:
                    self.hour=self.hour-24

class advobj:

    def __init__(self):
        self.state_poss=['hidden','appear','get','drop']
        self.state_locks=['locked','unlocked']
        self.state_usables=['usable','broken']

    def appear(self):
        self.state_pos='appear'

    def get(self):
        self.state_pos='get'

    def breakobj(self):
        self.state_usable='broken'

class gamevals:

    def __init__(self):
        self.gameflag=True
        self.flag={'key':'hidden','door':'locked',
                   'window':'unclean','box':'hidden',
                   'letter':'hidden','towel':'hidden','sheet':'hidden'}
        self.clock=clockobj()

def initmsg(gv):
     print("あなたは部屋にいます")

def cmdexe(cmd,gv):
    if cmd=="look":
        print("机（desk）があります")
        print("窓（window）があります")
        print("本棚（shelf）があります")
        print("ドア（door）があります")
        print("ベッド（bed）があります")
        print("時計（clock）があります")
        if gv.flag['key']=='appear' or gv.flag['key']=='drop':
            print("鍵（key）があります")
        if gv.flag['sheet']=='appear':
            print("シーツ（sheet）があります")
        if gv.flag['box']!='hidden':
            print("箱（box）があります")
        if gv.flag['letter']=='appear' or gv.flag['letter']=='drop':
            print("手紙（letter）があります")
        if gv.flag['letter']=='broken_drop':
            print("くしゃくしゃの手紙があります")
        if gv.flag['towel']=='appear' or gv.flag['towel']=='drop':
            print("タオル（towel）があります")
    elif cmd=="help":
        print("使用可能コマンド：")
        print("look, get, search, inventory, open, use, move, bend,")
        print("set, push, type, unlock, read, break, clean, drop,")
        print("コマンドは［動詞］または［動詞＋名詞］")
        print("look, search desk, など")
        print("lookで部屋全体の情報が出ます")
        print("look xxx でオブジェクトについての説明（ヒント）が出ます")
    elif cmd=="i" or cmd=="inventory" or cmd=="inv":
        stg=""
        have=0
        if gv.flag['key']=='get':
            stg=stg+"鍵（key）、"
            have=1
        if gv.flag['towel']=='get':
            stg=stg+"タオル（towel）、"
            have=1
        if gv.flag['letter']=='get':
            stg=stg+"手紙（letter）、"
            have=1
        if gv.flag['letter']=='broken':
            stg=stg+"くしゃくしゃの手紙、"
            have=1
        if have>0:
            print(str(stg)+"を持っています")
        else:
            print("何も持っていません")
    elif cmd=="hello":
        print("こんにちは！")
    elif cmd=="how do you do" or cmd=="how do you do?" or cmd=="howdy":
        print("元気だよ！ゲームをがんばろう！")
    elif cmd=="look clock":
        print("["+gv.clock.gettime()+"]と表示されています")
    elif cmd=="move clock" or cmd=="search clock":
        print("高いところにあるので手がとどきません")
    elif cmd=="drop key" and gv.flag['key']=='get':
        print("鍵を机の上に置きました。")
        gv.flag['key']='drop'
    elif cmd=="look shelf":
        print("本が詰まっています")
    elif cmd=="look letter":
        if gv.flag['letter']=='broken' or gv.flag['letter']=='broken_drop':
            print("くしゃくしゃになっています")
        else:
            print("なにか書いてあります")
    elif cmd=="look sheet":
        print("普通のシーツです")
    elif cmd=="search shelf":
        print("面白そうな本はありません")
    elif cmd=="look desk":
        if gv.flag['letter']=='hidden':
            print("手紙（letter）があります")
            gv.flag['letter']='appear'
        if gv.flag['letter']=='drop':
            print("手紙（letter）があります")
        if gv.flag['key']=='drop':
            print("鍵（key）があります")
        if gv.flag['towel']=='drop':
            print("タオル（towel）があります")
        if gv.flag['letter']=='broken_drop':
            print("くしゃくしゃの手紙（letter）があります")
    elif cmd=="get letter":
        if gv.flag['letter']=='appear' or gv.flag['letter']=='drop':
            print("手紙を取りました！")
            gv.flag['letter']='get'
        elif gv.flag['letter']=='broken_drop':
            print("くしゃくしゃの手紙を取りました")
            gv.flag['letter']='broken'
        else:
            print("どこにも見当たりません")
    elif cmd=="read letter" and gv.flag['letter']!='hidden':
        if gv.flag['letter']=='get':
            print("「この部屋から脱出せよ！」と書いてあります")
        elif gv.flag['letter']=='broken':
            print("くしゃくしゃなので読めません。")
        else:
            print("あなたは持っていません")
    elif cmd=="drop letter":
        if gv.flag['letter']=='get':
            print("手紙を机の上に置きました")
            gv.flag['letter']='drop'
        elif gv.flag['letter']=='broken':
            print("くしゃくしゃの手紙を机の上に置きました")
            gv.flag['letter']='broken_drop'
        else:
            print("あなたは持っていません")
    elif cmd=="search desk" or cmd=="open desk":
        if gv.flag['box']=="hidden":
            print("引き出しに小箱（box）がありました")
            gv.flag['box']='locked'
        else:
            print("ほかに変わったものはありません")
    elif cmd=="get box" or cmd=="move box":
        print("引き出しに固定されています")
    elif cmd=="look box" and gv.flag['box']!='hidden':
        if gv.flag['box']=='locked':
            print("ダイアル式の鍵がかかっています")
        elif gv.flag['key']=='appear':
            print("鍵（key）が入っています")
        else:
            print("からっぽです")
    elif cmd=="look window":
        print("鍵がかかっています")
        if gv.flag['window']=='unclean':
            print("黒ずんだ色をしています")
        else:
            print("７５３という文字が浮き出ています")
    elif cmd=="look door":
        print("金属製のドアです。")
        print("鍵がかかっています")
    elif cmd=="look key" and gv.flag['key']!='hidden':
        print("かわいらしい鍵です")
    elif cmd=="look bed":
        print("シーツ（sheet）がかぶせてあります")
        gv.flag['sheet']='appear'
    elif cmd=="search bed":
        print("とくになにもありません")
    elif cmd=="get sheet":
        print("大きすぎて持ち運ぶには大変そうです")
    elif cmd=="move sheet":
        if gv.flag['towel']=='hidden':
            print("タオル（towel）がありました")
            gv.flag['towel']='appear'
    elif cmd=='look towel' and gv.flag['towel']!='hidden':
        if gv.flag['window']=='unclean':
            print("普通のタオルです。")
        else:
            print("黒ずんでいます")
    elif cmd=="get towel":
        if gv.flag['towel']=='appear' or gv.flag['towel']=='drop':
            print("タオルを取りました！")
            gv.flag['towel']='get'
        elif gv.flag['towel']=='get':
            print("すでに持っています")
        else:
            print("どこにも見当たりません")
    elif cmd=="drop towel":
        print("タオルを机の上に置きました")
        gv.flag['towel']='drop'
    elif cmd=="use towel" or cmd=="clean window" or cmd=="clean up window":
        if gv.flag['towel']=='get':
            if gv.flag['window']=='unclean':
                print("窓がきれいになって文字が浮き出てきました")
                gv.flag['window']='clean'
            else:
                print("これ以上きれいにはなりません")
        else:
            print("拭くものを持っていません")
    elif cmd=="set 753" or cmd=="753" or cmd=="push 753":
        if gv.flag['box']=='locked':
            print("箱の鍵が開きました")
            gv.flag['box']='unlocked'
            gv.flag['key']='appear'
        elif gv.flag['box']=='unlocked':
            print("すでに箱は空いています")
        else:
            print("なにを意味しているのですか？")
    elif cmd=="get key":
        if gv.flag['key']=='appear' or gv.flag['key']=='drop':
            print("鍵を取りました！")
            gv.flag['key']='get'
        else:
            print("すでに持っています")
    elif cmd=="unlock door":
        if gv.flag['key']=='get':
            if gv.flag['door']=='locked':
                print("ドアの鍵が開きました！")
                gv.flag['door']='unlocked'
            else:
                print("すでに開いています")
        else:
            print("鍵がありません")
    elif cmd=="open door" and gv.flag['door']=='unlocked':
        print("ドアが開きました。")
        print("部屋を脱出するのに成功しました！")
        print("[game end]")
        gv.gameflag=False
    elif cmd=="break window":
        print("強化ガラスなので割れません")
    elif cmd=="break door":
        print("金属製なので壊れません")
    elif cmd=="break desk" or cmd=="break shelf" or cmd=="break bed":
        print("手を痛めてしまいますよ？")
    elif cmd=="break letter":
        if gv.flag['letter']=='get':
            print("手紙がくしゃくしゃになりました")
            gv.flag['letter']='broken'
        elif gv.flag['letter']=='broken' or gv.flag['letter']=='broken_drop':
            print("さらにくしゃくしゃにするのですか？")
        else:
            print("あなたは持っていません")
    elif cmd=="break key" or cmd=="bend key":
        print("あなたは超能力者ですか？")
    elif cmd=="break towel" or cmd=="bend towel":
        print("ふにゃっと曲がりました")
    elif cmd=="move bed" or cmd=="move desk" or cmd=="move shelf":
        print("金具で固定されています")
    elif cmd=="move window" or cmd=="open window":
        print("鍵がかかっていて動きません")
    elif cmd=="open door":
        if gv.flag['door']=='locked':
            print("鍵がかかっていて動きません")
    else:
        print("それはできません。")
    return gv

gv=gamevals()
print("ワンルームアドベンチャー for python-cmd")
print("2020 tenkey aikoukai")
print("helpで説明文が表示されます")
while gv.gameflag:
    initmsg(gv)
    inp=input("command:")
    gv=cmdexe(inp,gv)
    gv.clock.tick()
