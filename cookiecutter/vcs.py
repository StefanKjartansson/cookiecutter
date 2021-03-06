#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
cookiecutter.vcs
----------------

Helper functions for working with version control systems.
"""

import logging
import os
import shutil
import subprocess
import sys

from .prompt import query_yes_no


def git_clone(repo, checkout=None):
    """
    Clone a git repo to the current directory.

    :param repo: Git repo URL ending with .git.
    :param checkout: The branch, tag or commit ID to checkout after clone
    """

    # Return repo dir
    tail = os.path.split(repo)[1]
    repo_dir = tail.rsplit('.git')[0]
    logging.debug('repo_dir is {0}'.format(repo_dir))

    if os.path.isdir(repo_dir):
        ok_to_delete = query_yes_no(
            "You've cloned {0} before. Is it okay to delete and re-clone it?".format(repo_dir),
            default="yes"
        )
        if ok_to_delete:
            shutil.rmtree(repo_dir)
        else:
            sys.exit()

    os.system('git clone {0}'.format(repo))

    if checkout is not None:
        subprocess.check_call(['git', 'checkout', checkout], cwd=repo_dir)

    return repo_dir
