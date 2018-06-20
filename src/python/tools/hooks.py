# encoding: utf-8
from utils import gitFoldersPath

import argparse
import os
import subprocess


def removeFolder(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(path)


def gitInit(path):
    p = subprocess.Popen(['git', 'init'], cwd=path)
    p.wait()
    p = subprocess.Popen(['git', 'config', '--unset', 'core.hooksPath'], cwd=path)
    p.wait()


def removeGitHooksFolder(path):
    p = subprocess.Popen(['git', 'config', 'core.hooksPath', '/dev/null'], cwd=path)
    p.wait()
    path = os.path.join(path, '.git', 'hooks')
    if os.path.exists(path):
        print 'Remove Hooks repository in %s' % path
        removeFolder(path)


def reload_hooks():
    parser = argparse.ArgumentParser(description='Reload Hooks.')
    parser.add_argument('path', type=str,
                        help='Path. Example: /Users/Francois/buildout/')
    args = parser.parse_args()
    for dirpath in gitFoldersPath(args.path):
        removeGitHooksFolder(dirpath)
        gitInit(dirpath)


def remove_hooks():
    parser = argparse.ArgumentParser(description='Remove Hooks.')
    parser.add_argument('path', type=str,
                        help='Path. Example: /Users/Francois/buildout/')
    args = parser.parse_args()
    for dirpath in gitFoldersPath(args.path):
        removeGitHooksFolder(dirpath)
