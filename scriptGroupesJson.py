import math
import random
import logging
import json
#voir l autre bibliotreque jsonyfile

logging.basicConfig(filename='./logs.log',level=logging.DEBUG,\
      format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')

try:
    logging.info("Ouverture du fichier des donnes")
    fichier = open("noms.txt", "r")    
except: 
    logging.error("un erreur c est produit" )
finally:
    logging.info("Fin de l'ouverture de fichier!!")


try:
    logging.info("debut de la lecture du fichier!!")
    noms = fichier.read()
    fichier.close()
    if noms=="" or len(noms)==0:
        print("Erreur de lecture")
        logging.error("Erreur de lecture" )
        #TODO j essaie de creer un Error personnalisé mais il y a un erreur
        #raise LectureErreur("Erreur de lecture")
    print(noms)
# except LectureErreur as ve: 
#     print(ve.args)
#     logging.error("Erreur de Lecture "+ve.args)
except:
    print("Un erreur se produit dans la lecture du fichier")
    logging.error("Un erreur se produit dans la lecture du fichier ")
finally:
    logging.info("Fin de la lecture du fichier!!")

logging.info("conversion du string en list")
listeNoms = noms.split(',')#conversion de le string en liste

#print(listeNoms)
nbParGroups = 3 # TODO : on pourra ajouter comme input de l'utilisateur

print("Tapez la quantite des personnes qu'integreront un groups ")
nbParGroups = int(input())


logging.info("calcule de la quantites de groupes")
groupes = math.ceil(len(listeNoms) / nbParGroups) #ceil pour arrondir en superieur
#print (groupes)

#verifier le cas que le fichiers soit vide ou on le trouve pas
logging.info("Creation et ouverture du fichier des groupes")
fichierEcriture = open("fichierGroupes.txt", "w")

#declaration du dictionaire à utiliser pour cree un json
dictJson = {}
listeNomsCopie = listeNoms[:] #copier une liste qui sera indépendante

logging.info("Creation des groupes")
for x in range(1,groupes+1):
    #generation des groupe
    if len(listeNomsCopie) >= nbParGroups:
        #j'ai choisi al hazar 2 personnes du groupe
        selected = random.sample(listeNomsCopie, k= nbParGroups)    

        #je parcours les noms selection et les efface de la liste des noms  
        for sel in selected:   
            listeNomsCopie.remove(sel)
    else:
        selected=listeNomsCopie #pour les dernieres elements de la liste

    logging.info("Ecriture dans le fichier Resultat groupe : "+ str(x))
    fichierEcriture.write("# GROUP #"+ str(x)+" : " + str(selected)+"\n")
    
    dictJson["groupe"+str(x)] = str(selected)


logging.info("fermeture du fichier txt")
fichierEcriture.close() # fermeture du fichier txt

#JSON
print(dictJson) #variable String cree en forme de json
logging.info("Gestion des variables json")

logging.info("convertir le dictionnaire en une chaîne en utilisant json.dumps")
#jsonNoms = json.loads(dictNoms) # la methode loads return un dictionnaire, décoder le JSON en dictionay
jsonNoms = json.dumps(dictJson) #convertir le dictionnaire en une chaîne en utilisant json.dumps:, POUR CONVERTIR DES DONNÉES EN UNE CHAÎNE D'UN OBJET JSON

print(jsonNoms)
logging.info("La chaîne json est "+jsonNoms)

logging.info("creation du fichier Json")
with open("resultatJson.json","w") as fileJson:    
    fileJson.write(jsonNoms)

fileJson.close()
logging.info("Fermeture du fichier Json")
logging.info("Fin de l script") 


#TODO creer des functions et les tests unitaires
#TODO creation du module ça n a pas functionné a refaire


