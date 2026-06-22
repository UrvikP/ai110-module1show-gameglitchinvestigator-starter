# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose. The games purpose is to correctly guess the number. You have a range and a limited number of tries to gues correctly, the Less guesses you need to get the number, the more points you're awarded.
- [ ] Detail which bugs you found.
I found a bug in the Check_guess function which continued to give the wrong hints. It turned out that there was an error that would convert the integer into a string in app.py. I deleted that portion that was converting it into a stirng, I also refactored the check_guess function after the corrections.
I also found an error with the attempts variable, which was intialized to 1 when the code was running as if it was supposed to initialized to 0 at the beginning. Simplly change it to 0 and that resolved the issue of the game ending with 1 more attempt left.
I found an inssue with the New Game button. It wouldn't work, also it wouldnt generate a new number based on the setting of the difficulty. It would not reset the history so you still had the history of the old game you played. I used Claude AI to add a few lines to fix this issue. I also refactored the get_range_for_difficulty function.
I tested all these fixes by playing the game and testing these features. I didn't really understand the unit test portion, and I did get an error. I felt that I didn't need the unit in my case because I manually tested the project, but I do understand the importance of creating unit tests to make sure parts of your code work the way they should.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Default difficulty setting is Normal. Select a different difficulty if you want and then click New game to reflect that difficulty otherwise continue with game.
2. User enter 75
3. Game returns Too High, Go Lower
4. User enters 40
5. Game returns Too Low, Go Higher
6. Score gets updated (score will not be correct as this function was not fixed)
7. Game ends after correct guess or no more attemps
8. User has an option of selecting another difficulty and clicking new game to play again.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
My tests did not work, running into some problems. Will try to get them resolved.

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
