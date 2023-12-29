from highscoringwords import HighScoringWords

def printLeaderboard(message, leaderboard, scores):
    print(f"\n{message}")
    for index, word in enumerate(leaderboard, start=1):
        print(f"{index}. {word} - Score: {scores[word]}")

def play_highscoringwords_game():

    # Build the leaderboard for the provided letters
    game = HighScoringWords()
    starting_letters = input("Enter a string of letters... For example = 'testing':\n\n").lower()
    leaderboard = game.build_leaderboard_for_letters(starting_letters)

    # Display the leaderboard
    printLeaderboard(f"Top scoring words from starting letters '{starting_letters}'", leaderboard, game.word_scores)

    # uncomment below line for wordslist leaderboard
    # printLeaderboard("Top scoring words from wordslist.txt:", game.leaderboard, game.word_scores)

if __name__ == "__main__":
    play_highscoringwords_game()