import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import json


def send_email(receveur, object, msg,nomfichiers, adressepiecesjointes): 
 
 with open("config.json", "r") as f_read: #partie dico du json
   
      dico = json.load(f_read)
     
    
 envoyeur = dico["sender"]
 mdp = dico["password"]
 port = dico["port"]
 serveur = dico["serveur"]
 

 message = MIMEMultipart()    ## Création de l'objet "message"
 message['From'] = envoyeur    ## Spécification de l'expéditeur
 message['To'] = receveur    ## Attache du destinataire à l'objet "message"



 message['Subject'] = object    ## Spécification de l'objet de votre mail
      ## Message à envoyer
 message.attach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'))    ## Attache du message à l'objet "message", et encodage en UTF-8
 #while nombrepiecejointe!=0:
 j=0
 for i in nomfichiers : # Passe la partie fichier si on ne rentre rien
    if i != '':
      nom_fichier = i   ## Spécification du nom de la pièce jointe
                    
      piece = open(adressepiecesjointes[j], "rb")    ## Ouverture du fichier
      part = MIMEBase('application', 'octet-stream')    ## Encodage de la pièce jointe en Base64
      part.set_payload((piece).read())
      encoders.encode_base64(part)
      part.add_header('Content-Disposition', "piece; filename= %s" % nom_fichier)
      message.attach(part)    ## Attache de la pièce jointe à l'objet "message" 
      j+=1
 serveur = smtplib.SMTP(serveur, port)    ## Connexion au serveur sortant (en précisant son nom et son port)
 serveur.starttls()    ## Spécification de la sécurisation
 serveur.login(envoyeur, mdp)    ## Authentification
 msg = message.as_string().encode('utf-8')    ## Conversion de l'objet "message" en chaine de caractère et encodage en UTF-8
 serveur.sendmail(envoyeur, receveur, msg)    ## Envoi du mail
 serveur.quit()    ## Déconnexion du serveur

while True:
 print('Pour modifier vos identifiants, allez dans le fichier config')   
 print('Envoyez votre mail ici :') 
 receveur = input("adresse du destinataire : ")
 
 sujet = input("object : ")
 message = input("message : ")
 strpiece = input("nombre de pièce jointe :")
 if strpiece =='':
      strpiece ='0'
 nouvadressepiecejointe = []
 nouvnomfichier= []
 nbpj = int(strpiece)
 if nbpj != 0:
      i=0
      
      while i<nbpj:
           print("Rentrez votre pièce jointe") 
           fichier = input("nom du fichier : ")
           nouvnomfichier.append(fichier)
           adresse = input("adresse pièce jointe : ")
           nouvadressepiecejointe.append(adresse)
           i+=1
 
 print('Envoi en cours')
 print('Veuillez patienter') 
 send_email(receveur, sujet, message, nouvnomfichier, nouvadressepiecejointe)
 print('Votre message a bien été envoyé')
 print("Merci d'avoir utilisé le script WFJL")
 print("\n")
 print("\n")