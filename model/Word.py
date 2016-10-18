class Word:

    def __init__(self, word, mean, assist=None):
        self.word = word
        self.mean = mean
        self.assist = assist

    def get_word(self):
        return self.word

    def get_mean(self):
        return self.mean

    def __str__(self):
        return "WORD:"+self.word+"("+self.mean+")"+"//"+self.assist

