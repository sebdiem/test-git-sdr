# GIT dojo

## Introduction

Welcome to this GIT dojo.
In this dojo you will learn the fundamentals of our GIT workflow, which relies
heavily on `git rebase`.
First of all if you don't know what `rebase` is, please head over to [this
article](https://www.atlassian.com/git/tutorials/merging-vs-rebasing) which
explains the concept in great details, and how it differs from merging.

Don't worry and take the time needed to read the above article. I'm waiting for
you :p.

Ok now that you are more familiar with the concept, let's put this into practice!

## Rebasing "for real"

In this toy exercise, you will be working on a very simple codebase and we will
simulate multiple engineers working in parallel on the same files (that's funnier).

1. Choose a trigram (e.g. sdr for Sébastien Diemer). Replace `xxx` in the rest of this document by this trigram.
2. Create a branch named `dev-xxx`:

        git checkout master  # move to the master branch
        git pull --rebase origin master  # update the local copy with the remote one
        git checkout -b master-xxx  # create a fake master branch
        git checkout -b dev-xxx  # create a fake dev branch

3. Make some changes to `src/main.py`: change the code to print the strings in
   `hello_world` and `goodbye_all` on 2 lines. Commit the change.

4. Fake activity on master by running `python fake_git.py master_activity xxx`

5. Now update your local copy

        git fetch  # fetch modifications on the server without touching local copies
        git pull --rebase origin/master-xxx  # rebase your dev branch on master

This will cause a conflict and this is completely normal. Conflicts are
"normal" when collaborating on a codebase with multiple people. It just means
that two people tried to update the same portion of the code simultaneously,
and that git does not know how to reconcile both versions so you have work to
do. If you do not expect any conflict and want to check things before editing
anything you can always run `git rebase --abort` to cancel an ongoing rebase.

Try it! And then re-run the pull --rebase command `git pull --rebase origin/master-xxx`.

Now let's fix the conflict. Edit `src/main.py` to have both `===` separators
and multilines prints. Save and commit your change. Good job! If you look at
your commit history with `log --graph --decorate --pretty=oneline
--abbrev-commit`, you can see that your new commit now sits on top of
`master-xxx` (this is what rebase did)

6. Add another commit that creates a function that prints "See you tomorrow".

7. Squash your two commits into one by using interactive rebase `git rebase -i master-xxx` (see [here](https://git-scm.com/book/fr/v2/Utilitaires-Git-R%C3%A9%C3%A9crire-l%E2%80%99historique#s_squashing). Interactive rebase also allows you to reorder the commits, rewrite commit messages, split a commit, remove a commit (see documentation in thee link)).

8. Push your changes and open a PR.

        git push origin dev-xxx

9. Go to github.com and open a PR.

10. Push your changes to master-xxx. Normally you can do that from the github
   pull request interface but let's do this in the terminal.

        git checkout master-xxx  # move to the master-xxx branch
        git pull --rebase  # update the local copy with the remote one (just in case something new happened on the remote, but if it did, you'll have to update your dev branch too)
        git rebase dev-xxx  # rebase master-xxx on dev-xxx to incorporate your change (this is how you "merge" your work into the master in a rebase workflow)
        git push origin master-xxx


11. Clean the remote: `python fake_git.py clean xxx`. The PR should be automatically closed on github. If it's not the case close **without merging**.

12. You're done congratulations! Make sure you have understood all the commands
   you run in this dojo before proceeding to the next task.


## Code review process

Next you can read more about our code review process [here](https://mytraffic.atlassian.net/wiki/spaces/TECH/pages/882376709/The+code+review+process)
