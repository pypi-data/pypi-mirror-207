import git

# replace the URL with your Git repository URL
url = 'https://github.com/benstocker07/PhD.git'

# replace the branch name with the branch you want to clone
branch = 'task'

# replace the folder path with the folder you want to clone
folder = 'Task'

# replace the local path with the directory you want to download the folder to
local_path = 'C:/Users/Ben/Downloads/'

# clone the Git repository
repo = git.Repo.clone_from(url, local_path, branch=branch, depth=1)

# checkout the branch
repo.git.checkout(branch)

# get the folder path
folder_path = repo.working_dir + '/' + folder

print(f'The folder has been cloned to {folder_path}.')
