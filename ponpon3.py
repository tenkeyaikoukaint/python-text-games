
from enum import auto, Enum
from dataclasses import dataclass

class Scene:

    def description(self, game):
        raise NotImplementedError

    def command_execute(self, command, game):
        raise NotImplementedError

class Product(Enum):
    shop = auto()
    get = auto()

class Switch(Enum):
    on = auto()
    off = auto()

class Tool(Enum):
    drop = auto()
    get = auto()

@dataclass
class Game:
    is_run : bool
    scene : Scene()
    takoball : Product
    anchor : Switch
    rifle : Tool
    boat : Tool
    treasure : Tool

class Start(Scene):

    def description(self, game):
        print("あなたは港にいます。")
        print("1-船に乗る　2-家に帰る")

    def command_execute(self, command, game):
        if command == 1:
            print("あなたは船に乗りました。")
            game.scene = Deck()
        elif command == 2:
            print("あなたは家に帰って寝ました。")
            print("ゲームオーバー")
            game.is_run = False
        return game

class Deck(Scene):

    def description(self, game):
        print("あなたは船の甲板にいます。")
        print("1-操舵室に行く　2-船を降りる")

    def command_execute(self, command, game):
        if command == 1:
            print("操舵室に入ります。")
            game.scene=Cabin()
        elif command == 2:
            print("船を降ります。")
            game.scene=Start()
        return game

class Cabin(Scene):

    def description(self, game):
        print("あなたは操舵室にいます。")
        print("赤と青のボタンがあります。")
        print("マニュアルがあります。")
        print("1-赤のボタンを押す　2-青のボタンを押す　3-マニュアルを読む")

    def command_execute(self, command, game):
        if command == 1:
            print("船が自爆しました！")
            print("ゲームオーバー")
            game.is_run=False
        elif command == 2:
            print("船が発進しました。")
            game.scene = Sea()
        elif command == 3:
            print("赤ボタン：自爆　青ボタン：発進")
            print("と書いてあります。")
        return game

class Sea(Scene):

    def description(self, game):
        print("あなたは外洋に出ました。")
        print("1-右に進む　2-左に進む　3-前進")

    def command_execute(self, command, game):
        if command == 1:
            print("船が進みます。")
            game.scene = Island()
        elif command == 2:
            print("船が進みます。")
            game.scene=Kraken()
        elif command == 3:
            print("渦潮に巻き込まれて船が沈みました。")
            print("ゲームオーバー")
            game.is_run = False
        return game

class Island(Scene):

    def description(self, game):
        print("あなたは島に立ち寄りました。")
        if game.takoball == Product.shop:
            print("おじさんがたこ焼きを売っています。")
            print("1-たこ焼きを買う2-戻る")
        else:
            print("おじさんがにこにこしています。")
            print("1-戻る")

    def command_execute(self, command, game):
        if game.takoball == Product.shop and command == 2 or \
            game.takoball == Product.get and command == 1:
            print("元来た航路に戻ります。")
            game.scene=Sea()
        elif game.takoball == Product.shop and command == 1:
            print("たこ焼きを買いました！")
            game.takoball = Product.get
        return game

class Kraken(Scene):

    def description(self, game):
        print("あなたは外洋を航行しています。")
        print("あなたの目の前に大ダコがいます。")
        if game.takoball == Product.get:
            print("1-進む　2-戻る　3-たこ焼きをあげる")
        else:
            print("1-進む　2-戻る")

    def command_execute(self, command, game):
        if command == 1:
            print("大ダコが邪魔をしています。")
        elif command == 2:
            print("戻りました。")
            game.scene=Sea()
        elif command == 3 and game.takoball == Product.get:
            print("大ダコがショックで海に沈んでいきます。")
            print("")
            print("海をすすんでいきます。")
            game.scene=Harbour()
        return game

class Harbour(Scene):

    def description(self, game):
        print("あなたは宝島に着きました。")
        print("1-いかりをおろす　2-上陸する")

    def command_execute(self, command, game):
        if command == 1:
            print("船のいかりをおろしてから上陸します。")
            game.anchor = Switch.on
            game.scene =Forest()
        elif command == 2:
            print("島に上陸します。")
            game.scene = Forest()
        return game

class Forest(Scene):

    def description(self, game):
        print("あなたはジャングルを歩いています。")
        print("小屋があります。")
        print("1-入る　2-入らない")

    def command_execute(self, command, game):
        if command == 1:
            print("小屋に入りました。")
            game.scene = Hut()
        elif command == 2:
            print("あなたは嵐に遭い持ち物をすべて失ってしまいました。")
            print("ゲームオーバー")
            game.is_run = False
        return game

class Hut(Scene):

    def description(self, game):
        print("あなたは小屋にいます。")
        print("外は嵐のようです。しばらくここでやりすごします。")
        print("ライフルがあります。")
        print("1-ライフルを取る　2-そのままにする")

    def command_execute(self, command, game):
        if command == 1:
            print("あなたはライフルを取りました。")
            print("嵐がおさまったようです。外にでます。")
            game.rifle = Tool.get
            game.scene = Forest2()
        elif command == 2:
            print("嵐が止んだようなので外に出ます。")
            game.scene = Forest2()
        return game

class Forest2(Scene):

    def description(self, game):
        print("あなたはジャングルにいます。")
        print("目の前にオオヤマネコがいます。")
        if game.rifle == Tool.get:
            print("1-ライフルを使う 2-逃げる")
        else:
            print("1-逃げる")

    def command_execute(self, command, game):
        if game.rifle == Tool.get and command == 2 or \
            game.rifle == Tool.drop and command == 1:
            print("あなたはなすすべもなくオオヤマネコに襲われました。")
            print("ゲームオーバー")
            game.is_run = False
        elif game.rifle == Tool.get and command == 1:
            print("空中に向けて発砲すると、オオヤマネコは逃げてゆきました。")
            print("先に進みます。")
            game.scene = Lighthouse()
        return game

class Lighthouse(Scene):

    def description(self, game):
        print("あなたは灯台の前にいます。")
        print("1-二階に行く　2-地下に行く")

    def command_execute(self, command, game):
        if command == 1:
            print("二階に行きます。")
            game.scene=Lighthouse2F()
        elif command == 2:
            print("地下に行きます。")
            game.scene=LighthouseBF()
        return game

class Lighthouse2F(Scene):

    def description(self, game):
        print("あなたは灯台の二階にいます。")
        if game.boat == Tool.drop:
            print("ゴムボートがあります。")
            print("1-ゴムボートを取る　2-戻る")
        else:
            print("1-戻る")

    def command_execute(self, command, game):
        if game.boat == Tool.drop and command == 2 or \
            game.boat == Tool.get and command == 1:
            print("灯台の入り口に戻ります。")
            game.scene = Lighthouse()
        elif game.boat == Tool.drop and command == 1:
            print("ゴムボートを取りました！")
            game.boat = Tool.get
        return game

class LighthouseBF(Scene):

    def description(self, game):
        print("あなたは灯台の地下にいます。")
        if game.treasure == Tool.drop:
            print("財宝がありました！")
            print("1-財宝を取って進む　2-戻る")
        else:
            print("1-進む　2-戻る")

    def command_execute(self, command, game):
        if command == 1:
            if game.treasure == Tool.drop:
                print("財宝を手に入れて地下を進みます。")
                game.treasure = Tool.get
            else:
                print("地下を進みます。")
            game.scene = UnderGroundLake()
        elif command == 2:
            print("灯台の前に戻ります。")
            game.scene=Lighthouse()
        return game

class UnderGroundLake(Scene):

    def description(self, game):
        print("あなたは地底湖のほとりにいます。")
        if game.boat == Tool.get:
            print("1-ボートに乗る　2-戻る")
        else:
            print("1-進む　2-戻る")

    def command_execute(self, command, game):
        if command == 2:
            print("地下を戻ります。")
            game.scene=LighthouseBF()
        elif command == 1:
            if game.boat == Tool.get:
                print("ボートに乗って地底湖を渡ります。")
                game.scene=OverGround()
            else:
                print("冷たくて泳げそうにありません。")
        return game

class OverGround(Scene):

    def description(self, game):
        print("あなたは海上に出ました。")
        if game.anchor == Switch.on:
            print("船が見えました！")
            print("あなたは財宝を手にし、島をあとにします。")
            print("ゲームエンド")
        else:
            print("停泊していた船は")
            print("嵐で流されてしまったようです。")
            print("最後の最後であなたは運に見放されました。")
            print("ゲームオーバー")
        print("0-ゲームを終わる")

    def command_execute(self, command, game):
        game.is_run = False
        return game


game=Game(True, Start(), Product.shop, Switch.off, Tool.drop, Tool.drop, Tool.drop)
print("ポンポン船アドベンチャー")
print("2021 tenkey aikoukai")
while game.is_run:
    game.scene.description(game)
    try:
        command = int(input("command:"))
        game = game.scene.command_execute(command, game)
    except ValueError:
        print("数字を入力してくださいね！")
