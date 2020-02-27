# Update your repo!

## One-time setup

Run the following commands on the first setup:

1. Create an empty repository on github.
    * Name: `credit-risk-lecture`
    * Description: `[team-name]`
1. Create the repo and add `rhdzmota` as a collaborator.
    * Follow [these instructions](https://help.github.com/en/github/setting-up-and-managing-your-github-user-account/inviting-collaborators-to-a-personal-repository) to add collaborators. 
1. Clone the repository on your local machine:
    * Go to your base path. Ex: `cd ~/Documents`
    * Clone the repo: `git clone [url]`
    * Enter the repo: `cd credit-risk-lecture`
1. Create a `solutions` branch and push to remote.
    * Create branch: `git checkout -b solutions`
    * Push to remote: `git push origin solutions`
    * Return to master: `git checkout master`
1. Add an `upstream` repository:
    * `git remote add upstream [url]`
    * Use url: `https://github.com/RHDZMOTA/credit-risk-lecture.git`
    * Show remotes: `git remote -v`

## Verify before updating!

Please check your current workspace and identify if there's something to add/commit. 

Ask yourself the following: 

1. On which branch are you at? 
    * `git branch`
1. Is there anything I should add or commit?
    * `git status`
1. Before using `git add` or `git commit` verify if the current branch is the one you should be uploading those changes.
    * Change with: `git checkout [branch]`
    * Create with: `git checkout -b [branch]`
1. If needed, add/commit/push to the branch!
    * Add: `git add [file-path]`
    * Commit: `git commit -m "message"`
    * Push: `git push origin [branch]` in this case masterg
    
## Update procedure

**Update** your repo with the latest changes: 

1. Change to the master branch: 
    * `git checkout master`
1. Fetch latest updates from the upstream:
    * `git fetch upstream`
1. Merge into your master branch: 
    * `git merge upstream/master master`
    * `git push origin master`
    
**Create** a new working branch for a classwork or homework: 

1. Pull possible changes on your `solutions` branch:
    * Checkout: `git checkout solutions`

    * Pull: `git pull origin solutions`
1. Create the new branch from master: 
    * `git checkout master`
    * `git checkout -b [branch]`
1. Merge your `solutions` branch to ensure compatibility:
    * Merge: `git merge solutions` origin/solutions es posible
    * Solve conflicts if needed.

**Sync** current branch to Github:

1. Add and commit the relevant changes: 
    * Add: `git add [file-path]`
    * Commit: `git commit -m "message"`
1. Push to the remote:
    * Push: `git push [branch]`
1. Create a PR on github from `[branch]` to `solutions`!
    * 
