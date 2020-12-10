class TextContainer:
    def __init__(self):
        self.color = "red"
        self.word = "P"
        self.active = False

    def check(self,word):
        self.active = True
        return self.word == word

    def update(self):
        if self.active:
            render("P.png")
        else:
            render("wait.png")
        # render()
