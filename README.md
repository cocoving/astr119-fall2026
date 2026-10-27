# ASTR-119 course repository (Fall 2026)

This is your working folder for ASTR-119, Introduction to Scientific Computing, at UC Santa Cruz. You cloned it into `astr119` in your home folder during setup. Everything you write for this course lives here, and git keeps a history of it.

## What is in it

| Folder or file | What it is for |
|---|---|
| `module-1/` | Setup and first scripts (Sep 24 to Oct 8). Your comet script, `quadratic.py`, HW1. HW1 is **AI-free.** |
| `module-2/` | Loops, lists, functions. Added the week of Oct 12. |
| `module-3/` | numpy arrays and tables. Added the week of Oct 26. |
| `module-4/` | Plotting and fitting. Added the week of Oct 26; the galaxy notebook and its catalog arrive later. |
| `module-5/` | How a language model works. Added the week of Nov 23. |
| `project/` | Your final project. Added when proposals open, the week of Nov 2. |
| `data/` | Shared data sets, if any are needed. |
| `docs/` | The Protocol on one page, the AI-use note template, how to export a transcript. |
| `environment.yml` | The list of Python packages the course uses. The setup guide used it to build the `astr119` environment. |
| `CLAUDE.md` | Rules the AI agent follows in this repository. Read it; do not edit it. |
| `.claude/settings.json` | Permission settings for the agent. Do not edit it. |

Folders for later modules appear in this repository when we reach them. To receive a new module, commit your work first (`git add -A`, then `git commit -m "before the pull"`), then run `git pull --no-rebase --no-edit`. (After you make your own copy on GitHub, the command is `git pull --no-rebase --no-edit upstream main`.) Each module folder has a README saying what goes in it and which starter files it contains. Starter files are named `*_starter.py`. Copy a starter to the name the assignment asks for (`poke_starter.py` to `poke.py`), and work on the copy, so you can always go back to the original.

## The git commands

From a terminal inside this folder, every time, in this order:

```
git status                          # what changed since the last snapshot?
git add -A                          # include everything in the next snapshot
git commit -m "before the agent"    # take the snapshot, with a label
```

A fourth command, `git push`, copies your snapshots to your own copy on GitHub. It works only after you have made that copy (the Canvas page "Your own copy on GitHub"; extra credit in HW2). Until then, the commit is enough.

Commit before you ask the agent for anything, after you finish a piece of homework that works, and at the end of every pod session. `git diff` shows what changed since the last commit; from October 8 on, that is how you read what the agent did.

## Working with the agent

The first two weeks, through Thursday October 8, are AI-free: no Claude Code, no other AI tool. HW1 (`module-1/poke.py` and the files it asks for) stays AI-free. After October 8 the agent is expected on most other work, under the Protocol in `docs/protocol.md`: commit first, read what it wrote, predict, run, ask one "why", read the diff. With every homework from HW2 on, you submit your exported transcript and a 150-word AI-use note (`docs/ai-use-note-template.md`).

## Where things are

- Course site: Canvas. The calendar there is the authority on dates.
- Questions: the course Slack. Help with installs: the discussion section, run by the TA.
- Setup guides for Mac and Windows: Canvas, Module 1.
