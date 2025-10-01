# -------------------------------------------
# Exercise 3: Git Branch & Pull Request
# -------------------------------------------
# In this exercise you will learn:
# - What a Git branch is
# - Why branches are useful
# - How to create your own branch
# - How to make changes safely on a branch
# - How to submit a Pull Request to merge back into main
#
# All students will work in the same repository but on separate branches.
# -------------------------------------------

# Step 1: Python Task
# -------------------
# First, let’s add some simple Python code.
# This will give us something to commit to Git.

# TODO:
# 1. Ask the user for their name
# 2. Ask the user for their favourite hobby
# 3. Print a greeting using both inputs
#
# IMPORTANT:
# Don’t just copy an example – create your own version.
#
# Example:
# Imagine we wanted to ask about a person’s favourite colour:
# colour = input("What is your favourite colour? ")
# print(f"Wow! {colour} is a nice colour!")
#
# 👉 Notice how we:
# - Store the input in a variable (colour)
# - Use that variable inside an f-string with {}
#
# For YOUR task, you must:
# - Use different variable names (e.g. username, activity)
# - Follow the same pattern with input + f-string
# - But this time ask about *name* and *hobby*

# Step 2: Understanding Git Branches
# ----------------------------------
# A branch is like a “copy” of your project where you can make changes
# without affecting the main version (main branch).
#
# This is useful because:
# - You can try out new features safely
# - Other people can work on their own branches at the same time
# - Once tested, branches can be merged back into main
#
# Think of it like a “parallel timeline” for your code.

# Step 3: Creating and Using a Branch
# -----------------------------------
# 1. Check what branch you are on:
#    git branch
#
# (You’ll probably see *main)
#
# 2. Create a new branch with your name or initials:
#    git branch yourname
#
# 3. Switch to your branch:
#    git checkout yourname
#
# Now you’re working on your own copy of the code.
# Any changes you make are saved here, not in main.

# Step 4: Make Your Changes
# -------------------------
# - Add your Python code (name + hobby)
# - Save the file
#
# Then commit your work on your branch:
#    git add Ex3_git_branch.py
#    git commit -m "Added greeting with hobby"
#
# Push your branch to GitHub:
#    git push origin yourname

# Step 5: Pull Request (PR)
# -------------------------
# A Pull Request is how you ask to merge your branch into main.
# It lets others review your changes before they become part of the main project.
#
# 1. Go to your GitHub repository in the browser
# 2. You’ll see a button: "Compare & pull request"
# 3. Click it and describe what you changed
# 4. Submit the Pull Request
# 5. Your tutor or classmates can review and merge it

# Step 6: Done!
# -------------
# Once your pull request has been merged, update your local main branch:
#    git checkout main
#    git pull origin main
#
# 🎉 Congratulations! You’ve learned how to use branches and pull requests.
