# Usefull git commands in Linux:

## What is git?
- Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

## First Steps: Git version and Setting config values
- Make sure you have git installed by: ```git version```
- Configure name, username and emial for git: 
  - ```git config --global user.name "Your Name"```
  - ```git config --global user.email "Your Email"```
  - ```git config --list``` view all the configs
  - Note that none of the above is used to log you in your github account. This info is only for people who work on a repo to be able to find out who made any changes.
- For addding github login account information you should add the credentials in the git config file later in home directory.

## Repositories
Are the containers for the git. You need to initialize a new repository anytime you want to start working on a new project.
- To initialize a new git repository, use the git init command inside a directory that you want to be tracked by git: ```git init```
- To clone a git repo from github: ```git clone "link to the repo in github that you copied from browser"```
- How to check in on the status of your repo: ```git status``` provides information of all the new untracked or modified or to be commited files.
- How to commit a change: 
  - ```git add file.js``` this will first add the file/files to the commiting stage
  - ```git commit -m "message for this file"``` this will commit the changes and submits.
- Get a history of all the commits that are made in the repo: ```git log```
- ```git add .``` will add all the changes within the current dir
- ```git add -A``` will add all the chanegs within the repo..
  
## How to back to an old commit using git checkout
- Using the ```git log``` command we can first extract the hash number of any of the old commits and using the following code, switch back to that commit: ```git checkout #####```

## Branching in git
- A branch could be interpreted as an individual timeline of our project commits. The "Official" stable version of our branch is call the master or the main branch. When we initialize a repository and start making commits, they are saved to the master branch by default.
- Creating a new branch: ```git branch "new branch name"``` the new branch that gets created will be the reference to the current state of your repository.
- List all the existing branches in your repo: ```git branch```
- a development branch is usually helpful to always do your tests and improving in it and then merging it finally to your main/master branch.

## How to merge your changes from a branch to the master/main
- After you fully implemented and tested a new feature in your code, you would want to merge those changes to the stable branch of your project (master branch).
- To merge the changes from a different branch into your current branch (this could be either the master branch to be updated by your latest changes or another dev branch just to receive updates from another), you can use this command: ```git merge "branch-name-that-has-changes"```
## How to delete a branch
- to delete a branch you can run: ```git branch -d "branch-name"```


## .gitignore file
- you can add any file names in this file to be ignored when adding and commiting any changes into your repo.

## The staging area and how to remove files from it:
- The git add command will add the files that are provided to it to the staging area. For example: ```git add -A``` will add all the files that are created or modified to the staging area.
- to remove a file from the staging area you can use ```git reset file_name``` or ```git reset``` to remove everything from the staging area.

## Tracking an existing remote project with git:
- ```git clone "url" "where you want to clone it"``` this will clone the remote repo to the dir you want.
- Viewing information about a remote repository that we just cloned: 
  - ```git remote -v```: it lists the location of your local machin or where the repository is
  - ```git branch -a```: it will list all of the local and remote branches that are creted for this repository (both locally and remotely)


## Pushing changes to a branch
- First you would need to commit the changes locally:
  - ```git diff``` is gonna show you the changes that were made to the code.
  - ```git status``` will show info of untracked and modified files
  - ```git add -A``` will add to the staging area
  - ```git commit -m "message"``` will commit the changes
  - ```git pull origin master``` it will pull any changes that have been made to the repository since the last time we pulled from that repo.
  - ```git push origin master``` will push your changes to the master branch of your remote repository "origin"

## Common workflow with git
- Is to first create a branch of your desired feature and then begin off of that branch.
  - ```git branch calc-divid```
  - ```git checkout clac-divid```
  -  Make the changes that you want within the new branch you created.
  -  ```git status``` 
  -  View and see the files that have been modified or created.
  -  ```git add -A``` / ```git add file/files``` add the updated file/files/all to the staging area.
  -  ```git commit -m "message for my commit"``` commit the changes to our local calc-divid branch. This had no effect on our local master branch yet. And no effect on our remote repo.
  -  Now to push this branch to our remote repository: ```git push -u origin calc-divide``` you will only do this with -u option at the first time you push. The -u option just tells git that we wanna associate our local calc-divid branch with the remote calc-divid branch. And next time pushing you will only use ```git push``` and ```git pull``` bc it will know that those two branches are associated to each other.
  -  now with ```git branch -a``` you can see the info about the remote repositories and the new calc-divid remote branch that's been associated.

## Merge a branch with master when all the tests are done and you are 100 percent sure your code works!
- First checkout to your local master branch: ```git checkout master```
- Pull all the latest changes from the origin master remote branch: ```git pull origin master```
- ```git branch --merged``` this will only show the branches that we have merged in so far.
- Merge your local branch with all your changes with master local branch: ```git merge calc-divid```
- Now push the changes that are now in your local master branch to the reomte "origin" master branch: ```git push origin master```

## Deleting a branch from a remote repository
- First you may delete a branch that's been merged from your local: 
  - ```git branch --merged``` check if the branch you want to delete has already been merged.
  - ```git branch -d calc-divid``` this will delete the local branch
  - ```git branch -a``` this will show you all the existing branches within your local and remote repositories.
  - Since you also pushed that local branch to a "calc-divid" branch into your remote repository, you may want to delete that as well.
  - ```git push origin --delete calc-divid``` will delete the cal-divid branch from your remote "origin" repository. Origing is the name of our remote repo.


# Some Faster Examples: Push a final change to the remote repo
1. ```git branch feature_name```
2. ```git checkout feature_name```
3. make the changes that you need and save them in your editor
4. ```git add -A``` or ```git add file_name```
5. ```git commit -m "my latest changes"```
6. ```git push -u origin feature_name```
7. At this point you have already pushed your changes to a feature branch (not the main or master) of your remote (origin) repository.
8. Now to also merge chanegs in your local and remote master branches follow next steps.
9. ```git checkout master```
10. ```git pull origin master```
11. ```git merge feature_name```
12. ```git push origin master```
13. You can also go thru the process of deleting the feature branches in both local and remote if you want like explained above.
