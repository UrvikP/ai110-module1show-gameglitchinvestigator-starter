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

I used Claude.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I asked the AI to explain why the game always stops with 1 attempt left. It clearly explained to me that that is because the attempt counter starts at 1 but the game logic is written as if it starts at 0. It then showed me a trace to follow along with the normal difficulty. The logic increments first AND THEN checks the number of attempts. WHich is why we always have 1 attempt leftover at the end of the game. The fix was to change line 96 to st.session_state.attempts = 0. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

While I was fixing the notfication that gives a proper hint on whether you inputed a number that's too high or low the AI was unable to catch that the return output would always return the wrong information. This is because "Too High" was paired with "GO HIGHER" instead of "GO LOWER" and vice versa.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I tested the game after each bug fix. I ran a full game after each bug fix to make sure it did what it was supposed to do.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I tested the New Game button and made sure I could actually play a new game by clicking it. The game status state was set to "playing" every time the new game button was clicked. THis is a change I added in. I also made sure the range that the secret number was generated from matched the difficulty setting ie, Easy difficulty would generate a number between 1 - 20. 
- Did AI help you design or understand any tests? How?
  Yes AI helped me by explaining the code and what each piece does. It helped me break down the problems and pinpoint where the bugs are. It also helped me understand alittle bit about the unit tests and help me desing the tests.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit reruns the runs the entire code. Session state allows us to target variables and store values for those variables while Streamlit runs the app multiple times. You can also target variables and assign them new values for each rerun, for example, reseting vaules to 0 or empty so that the next app/game session starts as if its a fresh start.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I Definetely want to make sure I utilze AI to understand code. Clause helped me understand what the code was doing and this helped me get a better grasp of which part of the code represented a specific piece of the game application.
- What is one thing you would do differently next time you work with AI on a coding task?
  Instead of having it implement everything for me, I would definetely ask it to guide me to do the impleemnt myself. I'm not sure if thats possible, but I will be trying it for the next set of exercises and prjects.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  At the end of the day, I still need to be the decision maker. I need to be the one to narrow the focus of the AI to a specific problem. The more specific I am, the better the AI is a thandling the task and resolving the issue. Likewise, it doesn't catch every thing because some errors ar enot about numbers and logic, its just common sense.
