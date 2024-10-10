

- Go to - https://github.com/ 


- register and login

  Go to https://git-scm.com/downloads

  download and install github

- open cmd / git bash/ terminal-

- check git version-

  $ git --version


After successful installation , configure git in terminal/cmd/git bash- 

```
$ git config --global user.name "write your username"
$ git config --global user.email email@example.com
```

```
-view all of your settings
$ git config --list --show-origin / $ git config --list
```

Login github account in browser  

go to -> Your repositories -> create a Create a new repository

follow the instructions - 

### or create a new repository on the command line

```
echo "# repo name - fluffy-sniffle" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/mousumiahmed/fluffy-sniffle.git
git push -u origin main
```

### …or push an existing repository from the command line

```
git remote add origin https://github.com/mousumiahmed/fluffy-sniffle.git
git branch -M main
git push -u origin main
```

or 

- Clone the repo directly in cmd/ git bash/ terminal using -

  $ git clone <repository url>

  eg : git clone https://github.com/mousumiahmed/fluffy-sniffle.git

- create file inside your local repo folder

  $ touch <fileName >

- add all files -

  $ git add .

- add specific file -

  $ git add <filename 1><filename 2> .....................etc

- check added file in staging -

  $ git status 

- commit file -

  $ git commit -m "commit message"

- check in the codes -

  $ git push -u origin master

- View commit history-

  $ git log

  ​

  ​

-GIT Branching

    -Create Branch
    $ git branch <branch Name/Feature Branch>
    
    - Navigate to new Branch from current Branch
    $ git checkout <branch Name>
    
    - creating the branch and navigating to the branch at one time
    $ git checkout -b <new branch Name>
    
    - Check Your Current Branch
    $ git branch
    
    -Delete a Branch(make sure you are not in the branch you want to delete)
    $ git branch -d <branch-name>

- Common Git Branching Strategies

  - Master – Used for product release
  - Develop – Used for ongoing development
  - Feature Branching – To develop new features/task.
  - Release – Assist in preparing a new production release and bug fixing, typically branched from the develop branch, and necessitating merges back into both develop and master branches.
  - Hotfix – hotfix branches are created from master branch specifically for critical bug resolution in the production release.


![img.png](img.png)



- **Pull Request (PR):** A request made by a developer to merge their changes into another branch, often used for code review

- **Merge: **The process of combining changes from one branch into another.

  ```
  $ git merge [branch]
  ```

- **Git Fetch**: It's only retrieves changes from the remote repository but does not automatically merge them into the current branch. Instead, it updates the remote-tracking branches.

  ```
  - fetch the remote repository
  $ git fetch< repository Url>
  - synchronize the local repository
  $ git fetch origin
  - fetch all the branches simultaneously
  $ git fetch -all
  -fetch a specific branch from a repository
  $ git fetch <branch URL><branch name>
  ```

- **Git Pull**: The "git pull" command is a combination of two other Git commands: "git fetch" and "git merge." It fetches changes from the remote repository and automatically merges them into the current branch

  ```
  $ git pull origin master/git pull
  ```

  -**Git **Difference: See Difference between two Commit or branch or files or difference with current branch etc

  ```
  $ git diff
  $ git diff branch1_name branch2_name
  $ git diff commit-id-1 commit-id-2
  $ git diff name_of_branch
  etc
  ```

  Git Stash :

  Suppose a developer is working on a feature in a branch and he needs to pull changes from some other developer’s branch or if he has to work urgently on some other feature, but the feature he is currently working on is incomplete. In this case, you cannot commit the partial code of the currently working feature. To add this new feature, you have to remove your current changes and store them somewhere else. For this type of situation, Git offers a very useful command known as ‘**git stash**‘.

  ```
  - stash the changes
  $ git stash 
  - stash your untracked files
  $ git stash -u
  -provide more context to the stash
  $ git stash save "message"
  - to view stashes e.g. stash@{1}
  $ git stash list
  - To reapply the previously stashed changes with the ‘git stash pop’ or ‘git stash apply’ commands.“pop” removes the state from the stash list while “apply” does not remove the state from the stash list.eg: git stash pop stash@{2}
  $ git stash pop
  $ git stash apply
  - used to display the summary of operations performed on the stash
  $ git stash show
  - Creating A Branch From Your Stash.eg: git stash branch newbranch stash@{0}
  $ git stash branch branch_name stash_name
  -Cleaning Up Your Stash
  $ Git Stash Clear
  - To delete any particular stash (For ex:– stash@{1}), use ‘git stash drop stash@{1}’.
  $ git stash drop
  - Stashing Untracked Or Ignored Files
  $ git stash save --include-untracked

  ```

  Git Reset Vs Git Revert : git reset is used when to unstage a file and bring our changes back to the working directory. It can also be used to remove commits from the local repository.

  ```
   HEAD~1 here means that we are going to remove the topmost commit or the latest commit that we have done-
  $ git reset HEAD~1
  -Different ways in which git reset can actually keep your changes-
  1. This command will remove the commit but would not unstage a file. Changes still would be in the staging area -
  $ git reset –soft HEAD~1
  2. Used to removes the commit as well as unstages the file and our changes are stored in the working directory
  git reset –mixed HEAD~1 or git reset HEAD~1 
  3.removes the commit as well as the changes from your working directory
  git reset –hard HEAD~1

  git revert:It is used to remove the commits from the remote repository
  - Reverting a Single Commit
  $ git revert <commit>
  - To revert the last commit
  $ git revert HEAD
  - Reverting Multiple Commits
  $ git revert <commit1> <commit2> ... <commitN>
  - To revert the last three commits
  $ git revert HEAD~2..HEAD

  git revert commit1^..commit3
  git revert --skip
  git revert --abort
  etc
  ```


  ```

  Git Rebase :Process of integrating a series of commits on top of another base tip. It takes all the commits of a branch and appends them to the commits of a new branch

  ![git rebase.](https://media.geeksforgeeks.org/wp-content/uploads/20200415234509/Rebasing-in-git.png)



1. **git rebase master: **The command **“git rebase master”** can be used to make all modifications found in your master branch part of current branch.
2. **git rebase –continue: **When we are rebasing the branches we will face some conflicts and issues then we need to resolve the issue. After resolving the issue we again continue the rebasing processes for that we use “**git rebase –continue”.**
3. **git rebase –abort: “Git rebase –abort” **command cancels a rebase that is currently underway and restores the branch to its initial state.
4. **git rebase –skip: **When rebasing the branches we might face some unresolved conflicts to skip the particular encounters we will use ** “git rebase –skip”. **Skipping the commit is not good practice it will damage your codebase.
5. **git rebase -I HEAD~3: **With this command, we can interactively rebase the most recent three commits onto the active branch. You can choose which commits to rebase, alter commit messages, and squash or divide commits in the interactive editor that is opened.



git **cherry-pick** in git means choosing a commit from one branch and applying it to another branch



![After Cherry Pick](https://media.geeksforgeeks.org/wp-content/uploads/20220302150549/AfterCherryPick.jpg)

  ```
$ git cherry-pick<commit-hash>
- check your commit by git log command
  eg: git cherry-pick a1b2c3d4
- Cherry-Picking Multiple Commits
  $ git cherry-pick <commit1> <commit2> ... <commitN>
- Cherry-Picking a Range of Commits
  $ git cherry-pick <start_commit>^..<end_commit>
- Cherry-Picking with Conflict Resolution- If conflicts arise during cherry-picking, Git will pause  and allow you to resolve them. After resolving the conflicts, you can continue the cherry-pick with
  $ git cherry-pick --continue
- To abort the cherry-pick and return to the state before you starte
  $ git cherry-pick --abort
- Cherry-Picking Without Committing
  $ git cherry-pick <commit> --no-commit
- Cherry-Picking and Editing the Commit Message
  $ git cherry-pick <commit> --edit
- Find the commit hash
  $ git log --oneline




```

```