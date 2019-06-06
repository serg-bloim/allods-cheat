import os
from urllib import request
import zipfile

base = ''


def install(version, force=False):
    url = f'https://github.com/serg-bloim/aoe2-cheat/releases/download/v{version}/static.zip'
    localfile = f'static{version}.zip'
    if not os.path.isdir('static') or force:
        print("Instlling static files " + version)
        request.urlretrieve(url, localfile)
        zipref = zipfile.ZipFile(localfile)
        zipref.extractall()
        zipref.close()
