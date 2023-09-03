from colorama import Fore, init
import time
import json


init()


# colors
c = Fore.LIGHTCYAN_EX
g = Fore.LIGHTGREEN_EX
b = Fore.LIGHTBLUE_EX
r = Fore.LIGHTRED_EX
y = Fore.LIGHTYELLOW_EX
re = Fore.RESET


data = json.load(open("data.json"))


class Game():
    def start(self):

        global data

        print(data["title"])

        self.scene = data["startScene"]

        print("")
        input(y + "[+] Lets start..." + re)
        print("")

        self.showScene()


    def showScene(self):

        global data

        activScene = data["scenes"][self.scene]

        print(g + "[*] " + re + activScene["description"])
        print("")
        
        for index, choice in enumerate(activScene["choices"], 1):
            print(b + "[" + str(index) + "] " + re + choice["text"])

        print("")

        self.choice = int(input(y + "[+] Your choice: " + re))

        print("")

        if "outcome" in activScene["choices"][(self.choice - 1)]:
            outcome = activScene["choices"][(self.choice - 1)]["outcome"]
            print(c + "[*] " + re + outcome)

        else:
            self.destination = activScene["choices"][(self.choice - 1)]["destination"]

            self.scene = self.destination

            self.showScene()

Game().start()