

name = "another_nltk"


from nltk.stem import PorterStemmer

class Test(PorterStemmer):
    def __init__(self):
        super().__init__()

    def stem(self, word):
        return super().stem(word)

    def next(self):
        return super().next()


stemmer = PorterStemmer()
testing = Test()
 
print(stemmer.stem('working'))
print(testing.stem('working'))
print(name)