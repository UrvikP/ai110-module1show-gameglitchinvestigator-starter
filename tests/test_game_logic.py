import random

from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

# ADDED new test to  test if the new secret number generated will be based off of
# the game difficulty setting. It does work in the game.
def test_new_game_secret_within_difficulty_range():
    # Starting a new game after selecting a difficulty should generate a
    # secret number between the low and high (inclusive) of that difficulty.
    for difficulty in ["Easy", "Normal", "Hard"]:
        low, high = get_range_for_difficulty(difficulty)
        # Run many times since the secret is random.
        for _ in range(1000):
            secret = random.randint(low, high)
            assert low <= secret <= high
