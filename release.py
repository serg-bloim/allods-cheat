import sys

from github.GitRelease import GitRelease
from github.Repository import Repository
from setuptools import sandbox
import zipfile
from github import Github
from version import __version__
import git

def createStaticZip():
    zipF = zipfile.ZipFile('static.zip', mode='w')
    zipF.write('static')
    zipF.write('start.bat')
    zipF.write('upgrade.bat')
    zipF.close()
    return zipF.filename

def createUpgradeBat(v):
    with open('upgrade.bat.tpl', 'r') as ftpl:
        tpl = ftpl.read()
        with open('upgrade.bat', 'w') as f:
            f.write(tpl.format(v))


def release():
    new_release_version = __version__
    sandbox.run_setup('setup.py', ['bdist_wheel'])
    wheel_file = 'dist/aoe2stats-{}-py3-none-any.whl'.format(new_release_version)
    print(wheel_file)
    createUpgradeBat(new_release_version)
    createStaticZip()
    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha
    print(sha)

    gh = Github('b27c41bba330d579fbcfa650475835b324faa97e')
    repo: Repository = gh.get_repo('serg-bloim/aoe2-cheat')
    print(repo)
    rel: GitRelease = repo.create_git_release(tag=new_release_version, name=new_release_version, message='new release',target_commitish=sha)
    rel.upload_asset(wheel_file)

    # print(rel)
    # repo.get_releases()

release()