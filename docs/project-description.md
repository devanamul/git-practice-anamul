# Project Description

## Overview

**Git Practice — Anamul** is a small Python project created to practice the
core Git and GitHub workflows used in everyday development.

The code itself is intentionally simple so the focus stays on version
control rather than on program logic.

## Goals

- Initialize a repository and make a first commit
- Write a `.gitignore` to keep unwanted files out of version control
- Create a feature branch, work on it, and merge it back into `main`
- Delete a branch once it has been merged
- Make small, focused commits with clear messages
- Configure a remote and push the work to GitHub

## What the Program Does

`src/main.py` is the entry point. It prints the author's name and today's
date, then demonstrates the calculator functions defined in `src/utils.py`.

## Modules

### `src/main.py`

Entry point. Prints the name, the current date, and the result of each
calculator function.

### `src/utils.py`

Holds the calculator functions:

| Function         | Description                           |
| ---------------- | ------------------------------------- |
| `add(a, b)`      | Returns the sum of `a` and `b`        |
| `subtract(a, b)` | Returns the difference of `a` and `b` |
| `multiply(a, b)` | Returns the product of `a` and `b`    |
| `divide(a, b)`   | Returns `a` divided by `b`            |

## How to Run

```bash
python3 src/main.py
```

## Git Workflow Used

```bash
git checkout -b feature/calculator   # create and switch to a feature branch
git add .                            # stage the changes
git commit -m "message"              # commit them
git checkout main                    # switch back to main
git merge feature/calculator         # merge the feature in
git branch -d feature/calculator     # delete the merged branch
```
