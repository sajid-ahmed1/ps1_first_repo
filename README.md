# ps1_first_repo
This repository is for exercise 1 of the problem set 1.

sajidahmed@MacBookAir ps1_first_repo % ls
first_repo      README.md
# This command shows what is inside the first_repo file.

sajidahmed@MacBookAir ps1_first_repo % git status
# Shows the state of the working directory (so your local folder) and the staging area (the folder that is ready for the next commit)
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        first_repo/

nothing added to commit but untracked files present (use "git add" to track)

sajidahmed@MacBookAir ps1_first_repo % git add .
# This command puts all files into staging

sajidahmed@MacBookAir ps1_first_repo % git commit -m "included my_function.py and added to README.md"
# This command is the record of updates in your local folder

[main 33ba0fd] included my_function.py and added to README.md
 Committer: Sajid Ahmed <sajidahmed@MacBookAir.powerhub>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 2 files changed, 15 insertions(+)
 create mode 100644 first_repo/my_function.py


sajidahmed@MacBookAir ps1_first_repo % git push origin main
# This command updates the server folder

Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 679 bytes | 679.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/sajid-ahmed1/ps1_first_repo.git
   e6d53b1..33ba0fd  main -> main
sajidahmed@MacBookAir ps1_first_repo % 

