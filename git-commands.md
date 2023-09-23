# Useful Git Commands

- To clone this repo, you can use the following command

  The <ssh_link_to_repo> can be found be clicking the <>code button above the top of the repo and selecting ssh.

```
git clone <ssh_link_to_repo>
```

- To make sure your current branch is up to date, use git pull

```
git pull
```

- To look at all your branches locally use:
- NOTE: The branch that is currently your head will have a \* in front of the name.

```
git branch
```

- To look at all your local branches and all the remote branches, use the -a flag.

```
git branch -a
```

- To create a new branch locally, use git checkout -b  
  You only need the <remote_branch> if you wanted to base the new branch off of a different branch than the default (Main)

```
git checkout -b <branch_name> <remote_branch>
```

Example:

- This creates a new local branch named prototype-casey that is based off the main branch from remote.

```
git checkout -b prototype-casey
```

- This creates a new local branch named mike, that is based off of the prototype-mike branch

```
git checkout -b mike remotes/origin/prototype-mike
```

- To switch to a different branch you can use the checkout command without the -b flag.
- This works for checking out remote branches without making a local copy as well.

```
git checkout <branch_name>
```

Example:

- This allows me to checkout the remote prototype-john branch and see his code without making a local copy.

```
git checkout remotes/origin/prototype-john
```

- If you're checking out a remote branch and are detached from HEAD, you can use this command to go back to your head.

```
git switch -
```

1. After you've completed work in your branch, use the following to push a commit to remote

```
git add -u (to add all the files you've updated)
```

or

```
git add <file-name> (to add a specific file)
```

or

```
git add . (to all everything in the current directory)
```

2. After adding your changes, you have to commit before pushing.
   - the -m flag is required to add a comment, without a comment you will be forced into a text editor to add one. The comment is required in order to commit.

```
git commit -m " I did this work on these files."
```

3. After the commit and the meaningful comment is added, you can push your commit to remote.
   - if this is your first push to remote you need some extra commands to add it to the remote tree.

```
git push -u origin <branch_name> # If this is your first push of the branch to remote
```

Example:

```
git push -u origin prototype-casey
```

- If your branch is already on the remote tree, you can simply use:

```
git push
```

1. If you want to delete a local branch that you no longer need
   - Take note that the casing matters, d & D are different.
   - These commands DO NOT delete the branch from the remote git, meaning you can still pull them down later if you need to.

```
git branch -d <branch_name> # -d allows errors to stop the deletion
git branch -D prototype-casey # -D forces the deletion of the branch
```
