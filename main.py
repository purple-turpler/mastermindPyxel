import pyxel
class App:
    def __init__(self):
        pyxel.init(600, 700, title="Mastermind", fps=60, quit_key=pyxel.KEY_Q) #Parameters for screen
        self.colorReference = {
            "grey": 13,
            "white": 7,
            "blue": 12,
            "yellow": 10,
            "orange": 9,
            "purple": 2,
            "red": 8,
            "green": 11}
        self.gameStatus = 0
        self.password = []
        self.currentGuess = []
        self.prevousGuesses = []
        pyxel.run(self.update, self.draw) #Run function that takes

    def displayInterface(self, prevousGuesses, guess):
        pyxel.text(pyxel.width/2 - 25,10,"MASTERMIND",7)
        pyxel.rect(0,0,pyxel.width*0.15,pyxel.height,13)
        pyxel.rect(pyxel.width-(pyxel.width*0.15),0,pyxel.width*0.15,pyxel.height,13)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(1) #Clear screen
        self.displayInterface(self.prevousGuesses,self.currentGuess)

App()