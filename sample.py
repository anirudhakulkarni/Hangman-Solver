# https://github.com/search?q=hangman+language%3A%22Jupyter+Notebook%22&type=Repositories
#!/usr/bin/env python

import numpy as np
import os, sys, random
import operator, functools, time
from collections import defaultdict, Counter
from operator import itemgetter
from pathos.multiprocessing import ProcessingPool as Pool

class Hangman(object):
    def __init__(self, filename, maxNumMisses=6):
        with open(filename, 'r') as f: 
            self.wordSet = {line.strip() for line in f}
        self.wordDict = defaultdict(set)
        for word in self.wordSet:
            self.wordDict[len(word)].add(word)
        self.maxNumMisses = maxNumMisses
    def getNumOfWords(self):
        return len(self.wordSet)
    def getRangeOfLength(self):
        return (min(self.wordDict), max(self.wordDict))
    def sampleAWord(self):
        return random.sample(self.wordSet, 1)[0]
    def getWordSet(self):
        return self.wordSet.copy()  # Make a copy of the set
    def getSetByLen(self, n):
        return self.wordDict[n].copy()  # Make a copy of the dict
    def getMaxNumMisses(self):
        return self.maxNumMisses

class Guess(object):
    def __init__(self, hm, toPrint=False):
        self.hangman, self.toPrint = hm, toPrint

    def input(self, word):
        self.word = wordmo
        self.numMisses, self.maxNumMisses = 0, self.hangman.getMaxNumMisses()
        self.charsGuessed, self.charsMissed = [], []
        self.charIndexDict = defaultdict(list)
        for index, char in enumerate(self.word):
            self.charIndexDict[char].append(index)
        self.n, self.nLeft = len(self.word), len(self.word)
        self.ws = self.hangman.getSetByLen(self.n)
        self.printString, self.newGuess = list('_' * self.n), ''
        self.charCountDict = Counter()
        return self

    # A private function doing one guess
    def __guess(self):
        # Only run when there's letters left for guessing
        if self.nLeft:
            if self.nLeft == self.n and self.numMisses == 0:
                char = random.choice('aei')  # The first guess is always from 'aei'
            else:
                items = self.charCountDict.items()
                if len(items) >= 10:
                    # Choose one of the top three most frequent characters with weights
                    top3 = sorted(items, key=itemgetter(1), reverse=True)[:3]
                    chars = [i[0] for i in top3]
                    n1, n2, n3 = [i[1] for i in top3]
                    n0 = n1 + n2 + n3
                    char = np.random.choice(chars, p=[n1/n0, n2/n0, n3/n0])
                else:
                    char = random.choice([i[0] for i in items])

            # Print the process of guessing
            print('guess: ' + char, self.word) if self.toPrint else None
            
            # char should be new
            assert char not in self.charsGuessed
            self.charsGuessed.append(char)
            self.newGuess = char
            self.__update()
        else:
            print("The word %s has been successfully guessed!" %(self.word))

    # A private function updating the member variables
    def __update(self):
        if self.newGuess in self.word:
            ind = self.charIndexDict[self.newGuess]
            self.nLeft -= len(ind)
            for i in ind: self.printString[i] = self.newGuess
            # Filter by letter and position            
            def f(x):
                return self.newGuess in x and all(list(map(lambda y: x[y] == self.newGuess, ind)))
            self.ws = set(filter(f, self.ws))
        else:
            self.numMisses += 1
            self.charsMissed.append(self.newGuess)
            self.ws = set(filter(lambda x: self.newGuess not in x, self.ws))
        
        # Add the newly guessed char into charsGuessed list
        self.charsGuessed.append(self.newGuess)

        # Generate new charCountDict for the new wordSet self.ws
        # self.charCountDict = sum(list(map(Counter, list(map(set, self.ws)))))
        self.charCountDict = sum(list(map(Counter, self.ws)), Counter())
        
        # Delete all the keys in the charsGuessed
        for i in self.charsGuessed:
            del self.charCountDict[i]

        # If toPrint is True, print the guessing process
        print(' '.join(self.printString) + ' missed: ' + ','.join(self.charsMissed)) if self.toPrint else None

    def __run(self):
        while self.nLeft and self.numMisses <= self.maxNumMisses:
            self.__guess()
        return True if self.nLeft == 0 else False

    def f(self, word):
        return self.input(word).__run()

def main(args):
    if len(args) in [2, 3]:
        filename = args[1]
        toPrint = bool(args[2]) if len(args) == 3 else False
    else:
        print("The correct format is: python hangman.py [True]")

    maxNumMisses = 6
    hm1 = Hangman(filename, maxNumMisses)
    ws = hm1.getWordSet()
    if toPrint:
        word = hm1.sampleAWord()
        g1 = Guess(hm1, toPrint)
        print(g1.f(word))
    else:
        g1 = Guess(hm1)
        p = Pool(8)
        start = time.time()
        result = p.map(g1.f, ws)
        print('Number of words tested: {:,d}'.format(hm1.getNumOfWords()))
        print('Number of words guessed correctly: {:,d}'.format(sum(result)))
        print('Correct Guesses (%): {:.1f}%'.format(sum(result)/len(result)*100))
        print('Time to run: {:.1f} seconds'.format(time.time() - start))

if __name__ == '__main__':