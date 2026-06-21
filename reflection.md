# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  The first time I ran this game, I started by inputing my guess. It kept saying go higher until i ran out of attempts. However the game stopped early as I would always have 1 attempt left. I tried a different difficulty, in this case easy and it showed attempts left but when I checked the developer debugg info, the secret number was not between 1 - 20. The hints were definetely backwards, the game did not reset to reflect the difficulty level selected, and New Game button doesn't work.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 66| "Go HIGHER" | "Go LOWER" | none |

| New Game | Reset Game | Resets number of attempts, new secret number, does not reset history, score, submit guess button doesnt work | Game Over. Start a new game to try again |

| Easy | Set Attepmts to 6, set secret number to a value between 1 - 20 | Set attempts to 5, secret number did not change, game still ends with 1 attempt remaining | Out of attempts! The secret was 72. Score: -25 |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
