import os

from github.GitRelease import GitRelease
from github.Repository import Repository
from setuptools import sandbox
import zipfile
from github import Github
import tokens
from version import __version__
import git

def get_upgrade_filename(v):
    return 'upgrade-{}.bat'.format(v)

def createStaticZip(version):
    def addToZip(zf, path, zippath):
        if os.path.isfile(path):
            zf.write(path, zippath, zipfile.ZIP_DEFLATED)
        elif os.path.isdir(path):
            if zippath:
                zf.write(path, zippath)
            for nm in sorted(os.listdir(path)):
                addToZip(zf, os.path.join(path, nm), os.path.join(zippath, nm))
    zipF = zipfile.ZipFile('static.zip', mode='w')
    addToZip(zipF, 'static', 'static')
    zipF.write('start.bat')
    zipF.write(get_upgrade_filename(version))
    zipF.writestr('static/version.txt', version)
    zipF.close()
    return zipF.filename

def createUpgradeBat(v):
    with open('upgrade.bat.tpl', 'r') as ftpl:
        tpl = ftpl.read()
        with open(get_upgrade_filename(v), 'w') as f:
            f.write(tpl.format(v))


def release():
    new_release_version = __version__
    sandbox.run_setup('setup.py', ['bdist_wheel'])
    wheel_file = 'dist/aoe2stats-{}-py3-none-any.whl'.format(new_release_version)
    print(wheel_file)
    createUpgradeBat(new_release_version)
    createStaticZip(new_release_version)
    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha
    print(sha)
    gh = Github(tokens.github)
    repo: Repository = gh.get_repo('serg-bloim/aoe2-cheat')
    print(repo)
    rel: GitRelease = repo.create_git_release(tag=new_release_version, name=new_release_version, message='new release',target_commitish=sha)
    rel.upload_asset(wheel_file)
    rel.upload_asset('upgrade.bat')
    rel.upload_asset('static.zip')

release()