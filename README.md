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

- [x] Describe the game's purpose.
  - The game challenges the player to guess a randomly generated secret number while receiving higher/lower hints after each guess.

- [x] Detail which bugs you found.
  - The high/low hints were reversed in check_guess().
  - Clicking New Game after winning or losing did not reset the game status correctly.

- [x] Explain what fixes you applied.
  - Fixed the hint logic so higher guesses return "Too High" and lower guesses return "Too Low".
  - Fixed New Game so it resets the status and attempts correctly.
  - Added a regression test to verify the New Game fix.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The game starts and generates a secret number.
2. The player enters a guess of 40.
3. The game returns "Too Low" and tells the player to guess higher.
4. The player enters a guess of 70.
5. The game returns "Too High" and tells the player to guess lower.
6. The player enters the correct number.
7. The game displays a win message and updates the score.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```text
============================= test session starts =============================
collected 5 items

tests/test_game_logic.py .....                                  [100%]

5 passed, 1 warning in 3.86s
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
