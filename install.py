#!/usr/bin/env python
############################################################################################################
##BFAC: Backup File Artifacts Checker
###Homepage:
#https://github.com/mazen160/bfac
##install.py: BFAC Installer
###
##Author:
#Mazin Ahmed <Mazin AT MazinAhmed DOT net>
############################################################################################################
import os
import sys

if ( os.name != 'posix' ):
	exit('[!] Error: BFAC can not be installed on non *NIX machines.')

if ( os.getuid() != 0 ):
	exit('[!] Error: The installation process requires root access on the machine.')

def message_and_exit():
	print('#Run:')
	print('python '+sys.argv[0]+' confirm')
	exit()
	
if ( len(sys.argv) == 1 ):
	message_and_exit()
if ( sys.argv[1] != 'confirm'):
	message_and_exit()

os.system('pip install -r requirements.txt')
os.system('pip3 install -r requirements.txt')

os.system('cp bfac.py /usr/bin/bfac -v')
os.system('chmod 555 /usr/bin/bfac -v')

print('Installation is finished.')
os.system('bfac')
