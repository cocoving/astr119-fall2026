# The Protocol (one page)

Before anything: **commit first.**

```
git add -A
git commit -m "before the agent"
```

Every time the agent writes code for you, before you move on:

1. **Explain it.** Write one sentence, in your own words, for each function.
2. **Predict.** Pick one concrete input and write down what the code will output.
3. **Run it.** Compare with your prediction. If they differ, one of you is wrong, and it is not always the agent.
4. **Ask one "why".** Pick the line you understand least and ask the agent what it does and why. Write the answer in your own words.
5. **Read the diff.** `git diff` shows exactly what the agent changed. If it changed something you did not ask for, say so and have it undo it.

Then commit again with a label that says what happened (`git commit -m "hw2: legpoly loop"`).

## Asking well

- Name the file. Say what output you expect. The agent cannot see your screen.
- Ask for one function, one change, one step at a time.
- If it proposes to change more than you asked, say no.
- If it proposes a branch, a new package, or a rewrite, say no and ask why it wanted to.

## What to expect on oral exams

Explain your code, trace it by hand, modify it live, describe your process. Everything above is practice for that.
