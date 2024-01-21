import unittest
from highscoringwords import HighScoringWords

class TestHighScoringWords(unittest.TestCase):

    def start_game(self):
        game = HighScoringWords(validwords='test_wordlist.txt', lettervalues='letterValues.txt')
        game.leaderboard = game.build_leaderboard_for_word_list()
        return game

    def test_build_leaderboard_for_word_list(self):
        game = self.start_game()
        self.assertIsInstance(game.leaderboard, list)
        self.assertLessEqual(len(game.leaderboard), game.MAX_LEADERBOARD_LENGTH)
        for word in game.leaderboard:
            self.assertIn(word, game.valid_words)

    def test_build_leaderboard_for_letters_no_matches(self):
        game = self.start_game()
        with self.assertRaises(ValueError) as context:
            game.build_leaderboard_for_letters('abcd')

        self.assertEqual(str(context.exception), "No matches found!")

    def test_build_leaderboard_for_letters_invalid_input(self):
        game = self.start_game()
        with self.assertRaises(SystemExit):
            game.build_leaderboard_for_letters('ab')

if __name__ == '__main__':
    unittest.main()