#!/usr/bin/python

from datetime import datetime
import json, subprocess
from os.path import join, getsize
import os
from argparse import ArgumentParser
import time
from shutil import move




for root, dirs, files in os.walk("surveiller", topdown=False):
    for name in files:
        print(os.path.join(root, name), file=open("nomsfichiers", "a"))
    for name in dirs:
        print(os.path.join(root, name), file=open("nomsdossiers", "a"))
    for fn in files:
        path = os.path.join(root, fn)
        print(os.stat(path).st_size, file=open("poidsfichiers", "a"))



with open("nomsfichiers",'r') as f:
    d=set(f.readlines())
with open("nomsfichiersold",'r') as f:
    e=set(f.readlines())
with open('differencesnomsfichiers','w') as f:
    for line in list(d-e):
        f.write(line)

#envoyer differencesnomsfichiers par mail ici
move('nomsfichiers', 'nomsfichiersold')


with open("nomsdossiers",'r') as f:
    d=set(f.readlines())
with open("nomsdossiersold",'r') as f:
    e=set(f.readlines())
with open('differencesnomsdossiers','w') as f:
    for line in list(d-e):
        f.write(line)

#envoyer differencesnomsdossiers par mail ici
move('nomsdossiers', 'nomsdossiersold')


with open("poidsfichiers",'r') as f:
    d=set(f.readlines())
with open("poidsfichiersold",'r') as f:
    e=set(f.readlines())
with open('differencespoidsfichiers','w') as f:
    for line in list(d-e):
        f.write(line)

#envoyer differencespoidsfichiers par mail ici
move('poidsfichiers', 'poidsfichiersold')


time.sleep(60)
#on attend 1 minute

#return line 14


