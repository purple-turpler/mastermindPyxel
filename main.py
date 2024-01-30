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
        self.currentGuess = [0,0,0,0]
        self.guesses = [[8,11,2,12],[7,7,11,8],[0,0,2,0]]
        self.status = 10
        pyxel.run(self.update, self.draw) #Run function that takes

    def displayInterface(self):
        #Basic UI
        pyxel.rect(0,0,pyxel.width*0.15,pyxel.height,13)
        pyxel.rect(pyxel.width-(pyxel.width*0.15), 0, pyxel.width*0.15, pyxel.height, 13)
        pyxel.rect(pyxel.width*0.15, pyxel.height-100, pyxel.width*0.7,100, 0)
        pyxel.rect(pyxel.width*0.15, 0, pyxel.width*0.7, 100, 0)
        pyxel.text(pyxel.width/2 - 25,10,"MASTERMIND",7)

        #Custom UI based on previous guesses => conditional rendering
        currentPos = 0
        colorSwitch = False
        for guess in self.guesses:
            if self.status >= 0: 
                print(guess)
                self.status-=1
            pyxel.rect(pyxel.width*0.15, pyxel.height-(150+currentPos), pyxel.width*0.7, 50, 5+colorSwitch)
            xPos = 75
            for color in guess:
                pyxel.rect(pyxel.width*0.15 + xPos, pyxel.height-(150+currentPos-12.5), 25, 25, color)
                xPos += 75
            currentPos+=50
            colorSwitch = not colorSwitch

    def update(self):
        pass

    def draw(self):
        pyxel.cls(1) #Clear screen
        self.displayInterface()

App()