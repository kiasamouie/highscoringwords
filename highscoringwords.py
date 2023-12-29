__author__ = 'kia'

# HOW TO PLAY!
# Call "py playhighscoringwords.py" via the terminal and you will be prompted to input starting letters

# Python version = 3.10.8
class HighScoringWords:
    MAX_LEADERBOARD_LENGTH = 100  # the maximum number of items that can appear in the leaderboard
    MIN_WORD_LENGTH = 3  # words must be at least this many characters long
    letter_values = {}
    valid_words = []

    def __init__(self, validwords='wordlist.txt', lettervalues='letterValues.txt'):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data
        :param validwords: a text file containing the complete set of valid words, one word per line
        :param lettervalues: a text file containing the score for each letter in the format letter:score one per line
        :return:
        """
        self.leaderboard = []
        self.word_scores = {}

        with open(validwords) as f:
            self.valid_words = f.read().splitlines()

        with open(lettervalues) as f:
            for line in f:
                (key, val) = line.split(':')
                self.letter_values[str(key).strip().lower()] = int(val)

    def build_leaderboard_for_word_list(self):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOAD_LENGTH words from the complete set of valid words.
        :return: The list of top words.
        """
        # Build valid_words leaderboard if empty in order to populate self.word_scores
        if not self.leaderboard:
            self.leaderboard = self._build_leaderboard()

    def build_leaderboard_for_letters(self, starting_letters):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words that can be built using only the letters contained in the starting_letters String.
        The number of occurrences of a letter in the startingLetters String IS significant. If the starting letters are bulx, the word "bull" is NOT valid.
        There is only one l in the starting string but bull contains two l characters.
        Words are ordered in the leaderboard by their score (with the highest score first) and then alphabetically for words which have the same score.
        :param starting_letters: a random string of letters from which to build words that are valid against the contents of the wordlist.txt file
        :return: The list of top buildable words.
        """
        # validate starting_letters
        if len(starting_letters) < self.MIN_WORD_LENGTH:
            exit(f"Starting letters must be at least {self.MIN_WORD_LENGTH} characters long. Please try again!")

        matched_words = []
        character_range = range(5,16)
        starting_letters = list(starting_letters)

        for word in self.valid_words:
            # Skip word when not betweeen 5-15 characters
            word_length = len(word)
            if word_length not in character_range:
                continue

            count = 0
            letters = list(word)
            for l in starting_letters:
                if l in letters:
                    # remove current letter from letters
                    letters.pop(letters.index(l))
                    count+=1

            # starting_letters = 'testing' - words like 'gents', 'ingest', 'inset' will match
            if count == word_length:
                matched_words.append(word)
        
        # validate if matches were found
        if not matched_words:
            exit("No matches found!")

        self.build_leaderboard_for_word_list()

        # Build leaderboard for matched_words given the user input starting_letters
        return self._build_leaderboard(words=matched_words, scores=self.word_scores)
    
    def _build_leaderboard(self, words=None, scores=None):
        '''
        Generic method to build leaderboard in descending score order first then alphabetically if scores are idential
        words (list): List of words to build the leaderboard
        scores (dict): Dictionary containing word scores
        Returns a sorted leaderboard (list)
        '''
        leaderboard = []
        lowest_score = 0

        # Assumed to be creating leaderboard for self.valid_words
        if words is None:
            words = self.valid_words

        for word in words:
            # Skip if the word is less than minimum word length
            if len(word) < self.MIN_WORD_LENGTH:
                continue
            
            # Build self.word_score on each iteration
            if scores is None:
                self.word_scores[word] = sum([self.letter_values[letter] for letter in word])

            # Leaderboard is avaiable, append this word and determine new lowest_score
            if len(leaderboard) < self.MAX_LEADERBOARD_LENGTH:
                leaderboard.append(word)
                lowest_score = min([self.word_scores[word] for word in leaderboard])
            
            # Leaderboard has reached limit but current word score is greater than lowest score
            elif self.word_scores[word] > lowest_score:
                # Determine new lowest score and remove from leaderboard, append current word to leaderboard
                current_scores = [self.word_scores[word] for word in leaderboard]
                lowest_score = min(current_scores)
                leaderboard.pop(current_scores.index(lowest_score))
                leaderboard.append(word)
        
        # Sort reversed leaderboard (descending) by word score then word string if scores are identical
        leaderboard.sort(key= lambda word: (self.word_scores[word], word), reverse=True)
        return leaderboard