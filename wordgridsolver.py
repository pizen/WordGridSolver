#!/usr/bin/python

import sys
import getopt
import itertools
import random

words = []

def load_words():
    with open('Words/Words/en.txt', 'r') as f:
        for line in f:
            if len(line.strip()) == 4:
                words.append(line.strip())

def count_letters(s):
    counts = {}
    for letter in s:
        if letter not in counts:
            counts[letter] = 0
        counts[letter] += 1
    return counts

def find_solution(grid):
    possible = []

    grid_counts = count_letters(grid)

    for word in words:
        match = True
        for letter in word:
            if letter not in grid:
                # Exclude words with letters not in the grid
                match = False
                break
        if match:
            word_counts = count_letters(word)
            for letter in word_counts:
                if word_counts[letter] <= grid_counts[letter]:
                    # Only include words that can be made with the letters
                    # in the grid
                    possible.append(word)
                    break

    random.shuffle(possible)

    # Loop through the possible solutions looking for an answer
    # This is brute force and could probably be made more efficient
    for solution in itertools.combinations(possible, 4):
        if grid == ''.join(sorted(''.join(solution))):
            print solution
            break

def main(argv=None):
    if argv is None:
        argv = sys.argv

    load_words()
    for grid in argv[1:]:
        if len(grid) == 16:
            find_solution(''.join(sorted(grid.lower())))

if __name__ == "__main__":
    sys.exit(main())
