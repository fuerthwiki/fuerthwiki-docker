# This is my first attempt to write a build-script for fuerthwiki.de

REL = "REL1_39"
progfile = "./progress.json"  # that file is used for saving state to be able to restart this!
clone=False

import os, sys
import git, json

pj=[]
if not os.path.isfile(progfile):
    print('Creating {progfile}')
    with open(progfile, 'w') as pf:
        pf.write(json.dumps(pj))

print('Opening {progfile} to continue installation')
with open(progfile, 'r') as pf:
    pj=json.loads(pf.read())

repository_url = 'git@github.com:wikimedia/mediawiki.git'  # 'git@github.com:fuerthwiki/mediawiki.git'
local_path = f'./wiki_{REL}'
git_ssh_identity_file = r'"C:\Users\Red Rooster\.ssh\DellNotebook-RedRooster"'
git_ssh_cmd = f'ssh -i {git_ssh_identity_file}'

with git.Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd):
    print('Set ssh cmd to', git_ssh_cmd)

if clone:
    print(f'Cloning repo "{repository_url}"')
    repo = git.Repo.clone_from(repository_url, local_path, env=dict(GIT_SSH_COMMAND=git_ssh_cmd))
    print(f'Cloned repo {repo}')

repo = git.Repo(local_path)

print(f'Checking out {REL}')
repo.git.branch(f'{REL}')
repo.git.checkout(f'origin/{REL}')
print(f'Ready checking out.')
