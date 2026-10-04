from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

from logic_utils import check_guess

APP_PATH = str(Path(__file__).resolve().parent.parent / "app.py")

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 23 and guess is 69, the next guess should be lower.
    result = check_guess(69, "23")
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, the next guess should be higher.
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

@pytest.mark.parametrize("end_status", ["lost", "won"])
def test_new_game_resets_status_after_game_over(end_status):
    # Regression: New Game used to leave status as "lost"/"won", so the app
    # kept showing "Game over" and st.stop() blocked any further guesses.
    at = AppTest.from_file(APP_PATH)
    at.session_state["status"] = end_status
    at.session_state["attempts"] = 5
    at.run()
    assert not at.exception
    assert len(at.error) == (1 if end_status == "lost" else 0)  # game-over banner shown

    new_game = next(b for b in at.button if b.label.startswith("New Game"))
    new_game.click().run()

    assert not at.exception
    assert at.session_state["status"] == "playing"
    assert at.session_state["attempts"] == 0
    assert len(at.error) == 0  # "Game over" message is gone
