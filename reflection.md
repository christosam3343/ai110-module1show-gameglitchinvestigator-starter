# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
When i first ran the game, it worked for the most part but I noticed multiple bugs
like the hint direction which were reversed and the second bug was that after losing
a game, upon clicking the new game button it did not fully reset the game state.
The "Game Over" message remained on the screen and prevented me from continuing until I refreshed the page.
- List at least two concrete bugs you noticed at the start  
1. The hint directions were reversed
2. After losing the game, clicking New Game did not fully reset the game state

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|--------|-------------------|-----------------|------------------------|
| Secret = 50, Guess = 60 | Show "Too High" and tell player to go lower | Showed the wrong hint direction | No console error |
| Lose the game and click New Game | Start a fresh game and allow guessing again | "Game Over" message remained and blocked gameplay | No console error |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used ChatGPT and Claude Code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Claude identified that st.session_state.status was not being reset when New Game was clicked. I tested the fix in Streamlit and confirmed the Game Over message disappeared.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
Claude suggested removing the FIXME comments after fixing the bugs. I kept them because the assignment requires documenting the bug locations.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I reran the game and tried to reproduce the bug. If the bug no longer happened, I considered it fixed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran python -m pytest. All 5 tests passed.
- Did AI help you design or understand any tests? How?
Yes. Claude generated a regression test for the New Game bug and explained what it was checking.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Yes. Claude generated a regression test for the New Game bug and explained what it was checking.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
I want to keep testing every fix immediately after making changes.
- What is one thing you would do differently next time you work with AI on a coding task?
I would review every AI-generated change more carefully before accepting it.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
It showed me that AI is useful for finding bugs, but I still need to test and verify the code myself.
