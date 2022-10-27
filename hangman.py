import random


class Words:
    def __init__(self) -> None:
        self.analyzed_words = {}
        self.words = []
        f = open('words.txt', 'r')
        for i in f.readlines():
            self.words.append(i.replace('\n', ''))
    
    def analyze(self):
        i = 1
        for word in self.words:
            word_properties = {}
            word_properties['word'] = word
            word_properties['len'] = len(word)
            self.analyzed_words[f'{i}'] = word_properties
            i += 1

    def gen(self, difficulty):
        words = []
        for word in self.analyzed_words.keys():
            words.append(self.analyzed_words[word])

        choosen_words = []
        if difficulty == 'new':
            for word in words:
                if word['len'] <= 3:
                    choosen_words.append(word['word'])
        elif difficulty == 'easy':
            for word in words:
                if word['len'] > 3 and len(word['word']) <= 6:
                    choosen_words.append(word['word'])
        elif difficulty == 'medium':
            for word in words:
                if word['len'] > 6 and len(word['word']) <= 12:
                    choosen_words.append(word['word'])
        elif difficulty == 'hard':
            for word in words:
                if  word['len'] > 12:
                    choosen_words.append(word['word'])
        else:
            return random.choice(words)['word']
        return random.choice(choosen_words)


class Hangman:
    def __init__(self, difficulty) -> None:
        self.diff = difficulty
        self.words = Words()
        self.words.analyze()

    def game(self):
        word = self.words.gen(difficulty=self.diff)
        print(len(word) * '___ ')
        blanks = []
        for i in range(0, len(word)):
            blanks.append('___ ')
        err = 4
        wrong_geusses = 0
        while wrong_geusses <= err:
            guess = input('Enter your guess: ')
            sep_word = list(word)
            while guess in sep_word:
                index = sep_word.index(guess)
                blanks[index] = guess
                sep_word[index] = ''
            result = ''
            for i in blanks:
                result += f'{i}  '
            if result.replace(' ', '') == word:
                print('\n\n ----- Congradulations! ----- \n\n')
                break
            print(result)
            

if __name__ == '__main__':
    print('\t ***** HANGMAN ***** \n\n')
    diff = input('Enter Difficulty(new, easy, medium, hard, or leave it blank for random): ')
    game = Hangman(diff)
    game.game()