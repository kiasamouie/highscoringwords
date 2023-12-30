You are provided with two text files:

a vocabulary file wordlist.txt containing English words.
a file letterValues.txt showing a score for each letter in the English alphabet.
For the purposes of this challenge, a word in the vocabulary file has a total score which is the sum of the scores for all the letters that make up the word. So for example: the word cabbage has a score of 14 points: C3 + A1 + B3 + B3 + A1 + G2 + E1 = 14.

The objective of this coding challenge is twofold:

to create a leaderboard of the 100 highest scoring words in English based on the words in the wordlist.txt file. Words should be ordered in descending order with the highest scoring first. If several words have the same score they should be ordered alphabetically.

to create a leaderboard of the valid words that can be created from a supplied String of random letters. For example for the random String deora, some of the valid words are: road; read; and adore. The length of the random String may vary but can be assumed to be in the range of 5-15 characters. Again, words should be ordered in descending order with the highest scoring first. If several words have the same score they should be ordered alphabetically.

Some skeleton Python code is provided for the exercise. Please implement the empty methods, and create additional code as required. A HighScoringWords class with two unimplemented functions matching the numbered objectives above is in the file highscoringwords.py

def build_leaderboard_for_word_list(self):

def build_leaderboard_for_letters(self, starting_letters):

Add your code to the highscoringwords.py file. Although writing code to assemble the correct leaderboards is the highest priority, your code may also be benchmarked for performance.

YOUR CODE SHOULD THEREFORE BE OF PRODUCTION QUALITY!!!