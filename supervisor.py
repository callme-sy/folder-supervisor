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

def __init__(self, root, log_dir=''):
        
        self.root = root # the directory that we will monitor and track changes
        self.log_dir = log_dir # the directory where the logs and json files will be kept

        self.previous_state = self.readPrevState()  # a structure to hold all dir and file info of our previous snapshot
        self.current_state = {}  # a structure to hold all dir and file info of the current state
        
        self.added_dirs = []    # a list of directories added along with file and subdir info
        self.deleted_dirs = []  # a list of directories deleted along with the total size and number of files in them
        self.added_files = {}   # a dictionary of files added. filename is the key, size is the value
        self.deleted_files = {} # a dictionary of files deleted. filename is the key, size is the value
        self.changed_files = {} # a dictionary of files changed. filename is the key, a tuple (old_size, new_size) is the value 

        self.added_total_size = 0   # The total size in bytes of all files added
        self.deleted_total_size = 0 # The total size in bytes of all files deleted
        self.changed_total_size = 0 # The total size in bytes of all files changes
        self.added_total_num = 0   # The total number of all files added
        self.deleted_total_num = 0 # The total number of all files deleted
        self.changed_total_num = 0 # The total number of all files changed

        self.current_total_size = 0 # The total size of all files inside the tracked dir
        self.current_total_file_num = 0 # The total number of all files inside the tracked dir
        self.current_total_dir_num = 0 # The total number of all subdirs inside the tracked dir
    
        self.summary = ''  # A string to contain a summary of the additions/deletions/changes

 '''
    Read the previous state of the root directory from a special file. 
    If the file does not exist or is corrupted, return an empty dict
    '''
def readPrevState(self):

        prev_state_filename = 'track{}.json'.format(self.root.replace('/','_'))
        try:
            with open(join(self.log_dir, prev_state_filename)) as state_file:
                return json.load(state_file) # note: strings are returned as unicode strings

        except (IOError, ValueError):
            return {}

    '''
      
      
#Definir alertes
