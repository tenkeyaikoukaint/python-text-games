class gamestate:

    def __init__(self):
        self.gameflag=True
        self.sc=sc_start()
        self.flag={
            "takoball":"shop",
            "anchor":"off",
            "rifle":"drop",
            "boat":"drop",
            "treasure":"drop"
        }

class scene:

    def initmsg(self, gs):
        pass

    def cmdexe(self, cmd, gs):
        pass

class sc_start:

    def initmsg(self, gs):
        print("あなたは港にいます。")
        print("1-船に乗る　2-家に帰る")

    def cmdexe(self, cmd, gs):
        if cmd==1:
            print("あなたは船に乗りました。")
            gs.sc=sc_deck()
        elif cmd==2:
            print("あなたは家に帰って寝ました。")
            print("ゲームオーバー")
            gs.gameflag=False
        return gs

class sc_deck(scene):

    def initmsg(self, gs):
        print("あなたは船の甲板にいます。")
        print("1-操舵室に行く　2-船を降りる")

    def cmdexe(self, cmd, gs):
        if cmd==1:
            print("操舵室に入ります。")
            gs.sc=sc_cabin()
        elif cmd==2:
            print("船を降ります。")
            gs.sc=sc_start()
        return gs

class sc_cabin(scene):

    def initmsg(self, gs):
        print("あなたは操舵室にいます。")
        print("赤と青のボタンがあります。")
        print("マニュアルがあります。")
        print("1-赤のボタンを押す　2-青のボタンを押す　3-マニュアルを読む")

    def cmdexe(self, cmd, gs):
        if cmd==1:
            print("船が自爆しました！")
            print("ゲームオーバー")
            gs.gameflag=False
        elif cmd==2:
            print("船が発進しました。")
            gs.sc=sc_sea()
        elif cmd==3:
            print("赤ボタン：自爆　青ボタン：発進")
            print("と書いてあります。")
        return gs

class sc_sea(scene):

    def initmsg(self, gs):
        print("あなたは外洋に出ました。")
        print("1-右に進む　2-左に進む　3-前進")

    def cmdexe(self, cmd, gs):
        if cmd==1:
            print("船が進みます。")
            gs.sc=sc_island()
        elif cmd==2:
            print("船が進みます。")
            gs.sc=sc_kraken()
        elif cmd==3:
            print("渦潮に巻き込まれて船が沈みました。")
            print("ゲームオーバー")
            gs.gameflag=False
        return gs

class sc_island(scene):

    def initmsg(self, gs):
        print("あなたは島に立ち寄りました。")
        if gs.flag["takoball"]=="shop":
            print("おじさんがたこ焼きを売っています。")
            print("1-たこ焼きを買う2-戻る")
        else:
            print("おじさんがにこにこしています。")
            print("1-戻る")

    def cmdexe(self, cmd, gs):
        if gs.flag["takoball"]=="shop" and cmd==2 or gs.flag["takoball"]=="get" and cmd==1:
            print("元来た航路に戻ります。")
            gs.sc=sc_sea()
        elif gs.flag["takoball"]=="shop" and cmd==1:
            print("たこ焼きを買いました！")
            gs.flag["takoball"]="get"
        return gs

class sc_kraken(scene):

    def initmsg(self, gs):
        print("あなたは外洋を航行しています。")
        print("あなたの目の前に大ダコがいます。")
        if gs.flag["takoball"]=="get":
            print("1-進む　2-戻る　3-たこ焼きをあげる")
        else:
            print("1-進む　2-戻る")

    def cmdexe(self, cmd, gs):
        if cmd==1:
            print("大ダコが邪魔をしています。")
        elif cmd==2:
            print("戻りました。")
            gs.sc=sc_sea()
        elif cmd==3 and gs.flag["takoball"]=="get":
            print("大ダコがショックで海に沈んでいきます。")
            print("")
            print("海をすすんでいきます。")
            gs.sc=sc_harbour()
        return gs

class sc_harbour(scene):

    def initmsg(self, gs):
        print("あなたは宝島に着きました。")
        print("1-いかりをおろす　2-上陸する")

    def cmdexe(self, cmd, gs):
        if cmd==1:
            print("船のいかりをおろしてから上陸します。")
            gs.flag["anchor"]="on"
            gs.sc=sc_forest()
        elif cmd==2:
            print("島に上陸します。")
            gs.sc=sc_forest()
        return gs

class sc_forest(scene):

    def initmsg(self, gs):
        print("あなたはジャングルを歩いています。")
        print("小屋があります。")
        print("1-入る　2-入らない")

    def cmdexe(self, cmd, gs):
        if cmd==1:
            print("小屋に入りました。")
            gs.sc=sc_hut()
        elif cmd==2:
            print("あなたは嵐に遭い持ち物をすべて失ってしまいました。")
            print("ゲームオーバー")
            gs.gameflag=False
        return gs

class sc_hut(scene):

    def initmsg(self, gs):
        print("あなたは小屋にいます。")
        print("外は嵐のようです。しばらくここでやりすごします。")
        print("ライフルがあります。")
        print("1-ライフルを取る　2-そのままにする")

    def cmdexe(self, cmd, gs):
        if cmd==1:
            print("あなたはライフルを取りました。")
            print("嵐がおさまったようです。外にでます。")
            gs.flag["rifle"]="get"
            gs.sc=sc_forest2()
        elif cmd==2:
            print("嵐が止んだようなので外に出ます。")
            gs.sc=sc_forest2()
        return gs

class sc_forest2(scene):

    def initmsg(self,gs):
        print("あなたはジャングルにいます。")
        print("目の前にオオヤマネコがいます。")
        if gs.flag["rifle"]=="get":
            print("1-ライフルを使う 2-逃げる")
        else:
            print("1-逃げる")

    def cmdexe(self, cmd, gs):
        if gs.flag["rifle"]=="get" and cmd==2 or gs.flag["rifle"]=="drop" and cmd==1:
            print("あなたはなすすべもなくオオヤマネコに襲われました。")
            print("ゲームオーバー")
            gs.gameflag=False
        elif gs.flag["rifle"]=="get" and cmd==1:
            print("空中に向けて発砲すると、オオヤマネコは逃げてゆきました。。")
            print("先に進みます。")
            gs.sc=sc_lighthouse()
        return gs

class sc_lighthouse(scene):

    def initmsg(self,gs):
        print("あなたは灯台の前にいます。")
        print("1-二階に行く　2-地下に行く")

    def cmdexe(self, cmd, gs):
        if cmd==1:
            print("二階に行きます。")
            gs.sc=sc_lh2f()
        elif cmd==2:
            print("地下に行きます。")
            gs.sc=sc_lhbf()
        return gs

class sc_lh2f(scene):

    def initmsg(self, gs):
        print("あなたは灯台の二階にいます。")
        if gs.flag["boat"]=="drop":
            print("ゴムボートがあります。")
            print("1-ゴムボートを取る　2-戻る")
        else:
            print("1-戻る")

    def cmdexe(self, cmd, gs):
        if gs.flag["boat"]=="drop" and cmd==2 or gs.flag["boat"]=="get" and cmd==1:
            print("灯台の入り口に戻ります。")
            gs.sc=sc_lighthouse()
        elif gs.flag["boat"]=="drop" and cmd==1:
            print("ゴムボートを取りました！")
            gs.flag["boat"]="get"
        return gs

class sc_lhbf(scene):

    def initmsg(self, gs):
        print("あなたは灯台の地下にいます。")
        if gs.flag["treasure"]=="drop":
            print("財宝がありました！")
            print("1-財宝を取って進む　2-戻る")
        else:
            print("1-進む　2-戻る")

    def cmdexe(self, cmd, gs):
        if cmd==1:
            if gs.flag["treasure"]=="drop":
                print("財宝を手に入れて地下を進みます。")
                gs.flag["treasure"]="get"
            else:
                print("地下を進みます。")
            gs.sc=sc_uglake()
        elif cmd==2:
            print("灯台の前に戻ります。")
            gs.sc=sc_lighthouse()
        return gs

class sc_uglake(scene):

    def initmsg(self, gs):
        print("あなたは地底湖のほとりにいます。")
        if gs.flag["boat"]=="get":
            print("1-ボートに乗る　2-戻る")
        else:
            print("1-進む　2-戻る")

    def cmdexe(self, cmd, gs):
        if cmd==2:
            print("地下を戻ります。")
            gs.sc=sc_lhbf()
        elif cmd==1:
            if gs.flag["boat"]=="get":
                print("ボートに乗って地底湖を渡ります。")
                gs.sc=sc_overground()
            else:
                print("冷たくて泳げそうにありません。")
        return gs

class sc_overground(scene):

    def initmsg(self,gs):
        print("あなたは海上に出ました。")
        if gs.flag["anchor"]=="on":
            print("船が見えました！")
            print("あなたは財宝を手にし、島をあとにします。")
            print("ゲームエンド")
        else:
            print("停泊していた船は")
            print("嵐で流されてしまったようです。")
            print("最後の最後であなたは運に見放されました。")
            print("ゲームオーバー")
        print("0-ゲームを終わる")

    def cmdexe(self, cmd, gs):
        gs.gameflag=False
        return gs


gs=gamestate()
print("ポンポン船アドベンチャー")
print("2021 tenkey aikoukai")
while gs.gameflag:
    gs.sc.initmsg(gs)
    try:
        cmd=int(input("command:"))
        gs=gs.sc.cmdexe(cmd,gs)
    except ValueError:
        print("数字を入力してくださいね！")
