#!/usr/bin/env python3
# coding=utf-8
# *******************************************************************
# *** BFAC: Backup File Artifacts Checker ***
# * Homepage:
#   https://github.com/mazen160/bfac
# * setup.py:
#   BFAC setup script
# * Author:
#   Mazin Ahmed <Mazin AT MazinAhmed DOT net>
# *******************************************************************

from setuptools import setup, find_packages

setup(
    name='bfac',
    packages=find_packages(),
    version='1.4',
    scripts=['bfac'],
    description="Advanced Backup-File Artifacts Testing for Web-Applications",
    long_description="An automated tool that checks for backup artifacts " +
                     "that may disclose the web-application's" +
                     " source code.",
    author='Mazin Ahmed',
    author_email='mazin@mazinahmed.net',
    url='https://github.com/mazen160/bfac',
    keywords=['backup', 'artifacts', 'checker', 'web scanner',
              'web vulnerability scanner', 'bfac'],
    install_requires=['colorama', 'requests', 'requests[socks]'],
    license='GPL-3.0'
)
