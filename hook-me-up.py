#!/usr/bin/env python

from os import system

system("python ./scripts/init.py")
system("python ./scripts/php.py")
system("python ./scripts/apps.py")
system("python ./scripts/ssh.py")
system("python ./scripts/github.py")

print "Calibration complete. Have a nice day."

# TODO:
# apache (hosts + vhosts)
