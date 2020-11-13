from datetime import datetime
import json, subprocess
from os.path import join, getsize
from os import walk
from argparse import ArgumentParser


#Les arguments qu'on va utiliser :
parser = ArgumentParser(description="Traquer les changements dans un dossier. Ajouts et suppressions,\n \
                                     modifications de fichiers et sous-dossiers, le tout sera traqué dans un fichier log.\n \
                                     Si une limite définie est dépassée on envoie une alerte.\n")
parser.add_argument("-d","--dir", dest="dir", required=True, help="Le dossier choisi (requis)")
parser.add_argument("-s","--sizeabs", dest="size_abs", default=30, type=float, help="Nombre de mb a partir duquel on genere une alerte (defaut=30)")
parser.add_argument("-r","--sizerel", dest="size_rel", default=0.05, type=float, help="Changements minis pour alerte (defaut=0.05)")
parser.add_argument("-n","--numabs", dest="num_abs", default=50, type=int, help="Nombre de fichiers+dossiers a ajouter ou supprimer pour une alerte (defaut=50)")
parser.add_argument("-q","--numrel", dest="num_rel", default=0.05, type=float, help="Fraction de fichier et dossiers mini pr alerte (defaut=0.05)")
parser.add_argument("-l","--logdir", dest="log_dir", default="logs/", help="Emplacement du fichier de logs (defaut logs/)")
parser.add_argument("--schedule", dest="daySchedule", default="",  help="Definit les moments ou le script se lance. De la forme:  HH:MM,HH:MM,..")
parser.add_argument("--persistentAlert", action='store_true',  help="Notification en fenetre avec un bouton OK si activé")

args = parser.parse_args()

#Definir snapshot

#Definir alertes
