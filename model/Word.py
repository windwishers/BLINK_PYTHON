class Word:

    def __init__(self, deck, cate, word, mean, assist=""):
        self.deck = deck
        self.cate = cate
        self.word = word
        self.mean = mean
        self.assist = assist

    def get_word(self):
        return self.word

    def get_mean(self):
        return self.mean

    def __str__(self):
        return "WORD:"+self.word+"("+self.mean+")"+"//"+self.assist

    def __repr__(self):
        return self.__str__()

