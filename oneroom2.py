"""The one room adventure v2.0 for Python command line"""
"""Drop command(featured on the previous version)
   will implement on the next version"""

import random

acceptable_verbs = ["look", "inventory", "search", "get", "open", "unlock", "move", "bend", "break", "inventory", "help", "set", "clean", "read"]

class GameObject:

    def look(self):
        raise NotImplementedError

    def get(self, game):
        if not is_possess(game, self):
            if self.align == "can not carry":
                print("重すぎて持てません。")
            else:
                game.place.objects.remove(self)
                game.inventory.objects.append(self)
                print("取りました！")
        else:
            print("すでに持っています。")

    def drop(self, game):
        pass

    def open(self, game):
        print("それは開けられません。")

    def unlock(self, game):
        print("意味がありません。")

    def search(self, game):
        print("何も見つかりませんでした。")

    def move(self, game):
        if self.align == "can not carry":
            print("金具で固定されています。")
        else:
            if not is_possess(game, self):
                print("位置をずらしました。")
                print("とくに意味はないようです。")
            else:
                print("持っている手を振ってみました。")
                print("とくに意味はないようです。")

    def bend(self, game):
        print("難しいようです。")

    def set(self, game):
        print("意味がありません。")

    def read(self, game):
        print("特になにも書いてありません。")

    def breaking(self, game):
        print("手を痛めてしまいますよ？")

    def clean(self, game):
        if is_possess(game, game.towel):
            print("少しきれいになった気がします。")
        else:
            print("拭く道具がありません。")

    def get_place(self, game):
        return game.position_query(self)

class Door(GameObject):

    def __init__(self):
        self.state = "locked"
        self.align = "can not carry"

    def name(self):
        return "door"

    def namejp(self):
        return "ドア"

    def look(self, game):
        print("金属製のドアです。")
        if self.state == "locked":
            print("鍵がかかっています。")
        else:
            print("鍵が開いています。")

    def unlock(self, game):
        if is_possess(game, game.key):
            if self.state == "locked":
                print("ドアの鍵が開きました！")
                self.state = "unlocked"
            else:
                print("すでに開いています。")
        else:
            print("鍵がありません。")

    def open(self, game):
        if game.door.state == "unlocked":
            print("ドアが開きました。")
            print("部屋を脱出するのに成功しました！")
            print("[game end]")
            game.is_run = False

    def breaking(self, game):
        print("金属製なので壊れません。")

class Dial(GameObject):

    def __init__(self):
        self.align = "can not move"

    def look(self, game):
        print("箱についているダイアルです。")

    def name(self):
        return "dial"

    def namejp(self):
        return "ダイアル"

    def get(self, game):
        print("箱に固定されています。")

    def move(self, game):
        self.get()

    def set(self, game):
        number = -1
        while number < 0:
            try:
                number = int(input("番号は："))
                if number == 753:
                    print("鍵が開きました！")
                    game.box.state = "unlock"
                elif number >= 0:
                    print("鍵は開きませんでした。")
                else:
                    print("番号は正の整数です。")
            except ValueError:
                print("数字を入力してください。")

class Key(GameObject):

    def __init__(self):
        self.align = "movable"

    def name(self):
        return "key"

    def namejp(self):
        return "鍵"

    def look(self, game):
        print("かわいらしい鍵です。")

    def drop():
        if is_possess(self):
            print("鍵を机の上に置きました。")
            """game.flag['key']='drop'"""

    def breaking(self, game):
        print("あなたは超能力者ですか？")

    def bend(self, game):
        self.breaking()

class Shelf(GameObject):

    def __init__(self):
        self.align = "can not carry"

    def name(self):
        return "shelf"

    def namejp(self):
        return "本棚"

    def look(self, game):
        print("本が詰まっています。")

    def search(self, game):
        print("面白そうな本はありません。")

class Bed(GameObject):

    def __init__(self):
        self.align = "can not carry"

    def name(self):
        return "bed"

    def namejp(self):
        return "ベッド"

    def look(self, game):
        if not is_visible(game, game.sheet):
            print("シーツ（sheet）がかぶせてあります。")
            appear(game, game.sheet)
        else:
            print("やわらかそうなベッドです。")

class Desk(GameObject):

    def __init__(self):
        self.align = "can not carry"
        """
        self.objects = []
        self.hidden_objects = [game.letter]
        """
    def name(self):
        return "desk"

    def namejp(self):
        return "机"

    def look(self, game):
        if not is_visible(game, game.letter):
           print("手紙(letter)が置いてあります。")
           appear(game, game.letter)
        else:
            print("ふつうの学習机です。")

    def search(self, game):
        if not is_visible(game, game.box):
            print("引き出しに小箱（box）がありました。")
            appear(game, game.box)
        else:
            print("ほかに変わったものはありません。")

    def open(self, game):
        self.search(game)

class Letter(GameObject):

    def __init__(self):
        self.state = "fine"
        self.align = "movable"

    def name(self):
        return "letter"

    def namejp(self):
        if self.state == "fine":
            return "手紙"
        else:
            return "くしゃくしゃの手紙"

    def look(self, game):
        if game.letter.state == "broken":
            print("くしゃくしゃになっています。")
        else:
            print("なにか書いてあります。")

    def read(self, game):
        if self.state == "fine":
            print("「この部屋から脱出せよ！」と書いてあります。")
        else:
            print("くしゃくしゃなので読めません。")

    def breaking(self, game):
        if self.state == "fine":
            print("手紙がくしゃくしゃになりました。")
            self.state = "broken"
        else:
            print("さらにくしゃくしゃにするのですか？")

class Towel(GameObject):

    def __init__(self):
        self.state = "not used"
        self.align = "movable"

    def name(self):
        return "towel"

    def namejp(self):
        return "タオル"

    def look(self, game):
        if self.state == "not used":
            print("普通のタオルです。")
        else:
            print("黒ずんでいます。")

    def breaking(self, game):
        print("ふにゃっと曲がりました。")

    def bend(self, game):
        self.breaking(game)

class Box(GameObject):

    def __init__(self):
        self.state = "locked"
        self.align = "can not carry"

    def name(self):
        return "box"

    def namejp(self):
        return "箱"

    def get(self, game):
        print("引き出しに固定されています。")

    def move(self, game):
        self.get(game)

    def look(self, game):
        if is_visible(game, game.box):
            if game.box.state == "locked":
                print("ダイアル(dial)式の鍵がかかっています。")
                if not is_visible(game, game.dial):
                    appear(game, game.dial)
            else:
                if not is_visible(game, game.key):
                    print("鍵（key）が入っています。")
                    appear(game, game.key)
                elif not is_on_place(game, game.key):
                    print("からっぽです。")
                print("鍵が開いています。")

class Window(GameObject):

    def __init__(self):
        self.state = "unclean"
        self.align = "can not carry"

    def name(self):
        return "window"

    def namejp(self):
        return "窓"

    def look(self, game):
        print("鍵がかかっています。")
        if self.state == "unclean":
            print("黒ずんだ色をしています。")
        else:
            print("７５３という文字が浮き出ています。")

    def clean(self, game):
        if is_possess(game, game.towel):
            if game.window.state == "unclean":
                print("窓がきれいになって文字が浮き出てきました。")
                game.window.state = "clean"
                game.towel.state = "used"
            else:
                print("これ以上きれいにはなりません。")
        else:
            print("拭く道具がありません。")

    def move(self, game):
        print("鍵がかかっていて動きません。")

    def open(self, game):
        self.move(game)

    def unlock(self, game):
        if is_possess(game, game.key):
            print("違う鍵のようです。")
        else:
            print("あなたは鍵を持っていません。")

    def breaking(self, game):
        print("強化ガラスなので割れません。")

class Clock(GameObject):

    def __init__(self):
        self.hour = 9
        self.min = 0
        self.sec = 0
        self.align = "can not carry"

    def name(self):
        return "clock"

    def namejp(self):
        return "時計"

    def get_time(self):
        if self.hour < 10:
            string1 = f"0{self.hour}"
        else:
            string1 = self.hour
        if self.min < 10:
            string2 = f"0{self.min}"
        else:
            string2 = self.min
        if self.sec < 10:
            string3 = f"0{self.sec}"
        else:
            string3 = self.sec
        string = f"{string1}:{string2}:{string3}"
        return string

    def tick(self):
        self.sec = self.sec + random.randint(10,50)
        if self.sec >= 60:
            self.sec = self.sec - 60
            self.min = self.min + 1
            if self.min >= 60:
                self.min = self.min - 60
                self.hour = self.hour + 1
                if self.hour >= 24:
                    self.hour = self.hour - 24

    def look(self, game):
        print(f"[{self.get_time()}]と表示されています。")

    def move(self, game):
        print("高いところにあるので手がとどきません。")

    def search(self, game):
        self.move(game)

class Sheet(GameObject):

    def __init__(self):
        self.align = "can not carry"

    def name(self):
        return "sheet"

    def namejp(self):
        return "シーツ"

    def look(self, game):
        print("普通のシーツです。")

    def move(self, game):
        if not is_visible(game, game.towel):
            print("タオル（towel）がありました。")
            appear(game, game.towel)
        else:
            print("ほかにはなにも見あたりません。")

class Place:

    def description(self):
        pass

    def look(self, game):
        self.description()
        for i in self.objects:
            print(f"{i.namejp()}({i.name()})があります。")

class Room(Place):

    def __init__(self, game):
        self.objects = [game.desk, game.door, game.window, game.shelf, game.clock, game.bed]
        self.hidden_objects = [game.key, game.letter, game.towel, game.box, game.sheet, game.dial]

    def description(self):
        print("あなたは部屋にいます。")

class Inventory(Place):

    def __init__(self, game):
        self.objects = []

class Game:

    def __init__(self):

        self.is_run = True

        self.door = Door()
        self.window = Window()
        self.clock = Clock()
        self.shelf = Shelf()
        self.desk = Desk()
        self.key = Key()
        self.bed = Bed()
        self.box = Box()
        self.towel = Towel()
        self.sheet = Sheet()
        self.letter = Letter()
        self.dial = Dial()

        self.inventory = Inventory(self)
        self.room = Room(self)

        self.scenes = [self.room]
        self.place = self.room

    def position_query(self, object):
        scene = None
        for i in self.scenes:
            if object in i.objects:
                return i
        return scene
        if object in self.inventory.objects:
            return self.inventory

def is_visible(game, object):
    if object.get_place(game) in [game.place, game.inventory]:
        return True
    else:
        return False

def is_possess(game, object):
    if object in game.inventory.objects:
        return True
    else:
        return False

def is_on_place(game, object):
    if object in game.place.objects:
        return True
    else:
        return False

def appear(game, object):
    game.place.hidden_objects.remove(object)
    game.place.objects.append(object)

def description(game):
    game.place.description()

def parse(stmt):
     omit_words = ["the", "a", "my", "own", "up", "at"]
     sliced_stmt = stmt.split()
     for i in omit_words:
         while i in sliced_stmt:
             sliced_stmt.remove(i)
     if len(sliced_stmt) > 2:
         print("入力文が長すぎます。")
         return None, None
     elif len(sliced_stmt) == 2:
         return sliced_stmt[0], sliced_stmt[1]
     elif len(sliced_stmt) == 1:
         return sliced_stmt[0], None
     else:
         return  None, None

def command_execute(command, game):
    verb, noun = parse(command)
    if verb in acceptable_verbs:
        if noun == None:
            if verb == "look":
                game.place.look(game)
            elif verb == "inventory":
                if game.inventory.objects == []:
                   print("あなたは何も持っていません。")
                else:
                    print("あなたは、")
                    for i in game.inventory.objects:
                        print(f"{i.namejp()}({i.name()})")
                    print("を持っています。")
            elif verb == "help":
                print("使用可能コマンド：")
                print("look, get, search, inventory, open, move, bend,")
                print("set, unlock, read, break, clean,")
                print("コマンドは［動詞］または［動詞＋名詞］")
                print("look, search desk, など")
                print("lookで部屋全体の情報が出ます。")
                print("look xxx でオブジェクトについての説明（ヒント）が出ます。")
            """
            elif verb == "north":
                game.place = game.place.north(game)
            """
        else:
            visible_objects = game.place.objects + game.inventory.objects
            is_find_object = False
            for i in visible_objects:
                if noun == i.name():
                    is_find_object = True
                    if verb == "look":
                        i.look(game)
                    elif verb == "get":
                        i.get(game)
                    elif verb == "open":
                        i.open(game)
                    elif verb == "unlock":
                        i.unlock(game)
                    elif verb == "break":
                        i.breaking(game)
                    elif verb == "bend":
                        i.bend(game)
                    elif verb == "search":
                        i.search(game)
                    elif verb == "move":
                        i.move(game)
                    elif verb == "clean":
                        i.clean(game)
                    elif verb == "set":
                        i.set(game)
                    elif verb == "read":
                        i.read(game)
            if not is_find_object:
                print(f"{noun} は見あたりません。")
    else:
        if not(verb == None):
            print(f"{verb} することはできません。")

game = Game()
print("ワンルームアドベンチャー ver 2.0 for python-cmd")
print("2025 Tenkey Aikoukai")
print("helpで説明文が表示されます。")
while game.is_run:
    game.place.description()
    command = input("Enter command please : ")
    command_execute(command, game)
    game.clock.tick()


