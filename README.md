# STAT 214

This is the github repository for STAT 214, Spring 2025.

Thanks to Chengzhong Ye, Theo Saarinen, Omer Ronen, James Duncan, Tiffany Tang, Zoe Vernon, Rebecca Barter, and other past GSI's for sharing their material with us. This document was originally written by Rebecca for STAT 215A in the Fall of 2017, has been slightly modified in subsequent years, and has been significantly modified for STAT 214.

Questions and discussions between students can be posted on Ed Discussions (signup link on bCourses). That way everyone else can see your questions and the answers, and we don't have to answer the same questions a million billion times. Preferably you will answer each other's questions. It is our intention to only jump in when the question is one that only we can answer.

Please think carefully before asking questions specifically about the projects. For example, questions concerning how to do something specific in Python (e.g. "how do I format the data for linear regression in sklearn?") are fine, but questions asking what other people did for their analysis are not (e.g. "what are some findings that people have come across in the TBI project"). Questions asking about clarifications are fine.

# The lab assignments

There will be 3 lab reports throughout the semester (2 labs and 1 final project). These reports are a *big deal*. It is in completing these reports that the real learning happens. You will get to apply what you've learned in the lectures and labs to real datasets (with real issues). You will also learn to develop a narrative that reports your scientific findings as accurately and accessibly as possible: you will learn to tell a story with your analysis.

While you are allowed to discuss the projects with one another, each student must work on and hand in their own report. If you do consult with other students, please acknowledge these students in your lab reports.

## Setting up GitHub for this class

Your report and code will be submitted via GitHub. The following instructions will show you how to set up your GitHub account and configure a repository so that you can submit your assignments. This workflow is shamelessly copied (with slight modifications) from Chris Paciorek and Jarod Millman's setup from STAT243 in 2014.

1. Install Git on your system (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

1. Sign up for GitHub (https://github.com/).

1. Go to https://education.github.com/ and sign up for the student pack to get unlimited private repositories and access to Copilot. You are a "student" and you want an "individual account".

Once you have completed these first steps, you are then ready to create your private GitHub repository for this class.

1. Locally on your machine, clone our stat214 repository: `git clone https://github.com/anthonyozerov/stat214-gsi`. This will create a copy of the repository on your own computer.

1. On the GitHub website, log in and create a **private** remote repository called *stat214*. Add your GSI's as collaborators for this repository (check out settings on the repo website).

1. Back in the terminal, change directories to the stat214 folder and set the origin of your local repository to be the remote repository that you just made: `git remote set-url origin https://github.com/USERNAME/stat214.git` (Change USERNAME below to your username). This tells git which remote repository to push your changes to when you `git push`.

1. Edit *info.txt* to reflect your own information.

```
name = "Jane Smith"
SID = "0123456789"
email = "jsmith@berkeley.edu"
github_name = "janesmith"
```

Now you're ready to push to your remote repository for the first time:

1. Check git status `git status`. You should see a bunch of text including `modified:   info.txt`.

1. Add (`git add info.txt`) and commit (`git commit -m “Updated info.txt with my own information”`) your edited *info.txt* file

1. Push your changes to your copy of the remote repository (`git push` or sometimes `git push remote origin`)

1. Check that info.txt has been updated in your remote github repository by navigating to https://github.com/USERNAME/stat214 (change USERNAME to your username)

## Submitting your projects

To submit your projects, you will need to create a subfolder in your local `stat214` folder called `lab1` (if you are submitting lab 1). Inside this folder you should have the following (exact) structure:

```
lab1/
  data/
  documents/
  lab1.ipynb
  lab1.pdf
  lab1_blind.ipynb
  lab1_blind.pdf
  src/
  other/
```

- The source of your report (with code) will be contained in the `lab1.ipynb` file.

- The compiled version of your report will be contained in `lab1.pdf`.

- You will also submit a "blind" version of each of these documents that does not include your name (`lab1_blind.ipynb` and `lab1_blind.pdf`).

- The `src/` folder will contain any extra Python scripts needed to compile your report.

- The `data/` folder will contain any data you use for the lab.

- The `documents/` folder will contain any relevant papers or documents for the project.

- The `other/` directory can contain additional files needed to reproduce your lab (e.g. .bib files), but try to avoid depending too heavily on this directory.

Note that GitHub cannot host files more than 100 MB. If you try to push a file larger than this, GitHub will cry.

When you are ready, you need to add, commit, and push the `lab1/` folder.

At the time when the lab is due, I will run a script that automatically pulls all of your assignments into my local versions of your `stat214` repositories. Please make sure to submit your labs on time. We will spend some time in the first lab having everyone submit a pretend assignment so that you are all clear on what to do.
