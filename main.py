class Processus:
    def __init__(self, pid, duree):
        self.pid = pid
        self.duree = duree
        # Le nombre de cycles qui restent à faire :
        self.reste_a_faire = duree
        self.etat = "Prêt" # les états possibles : ["Prêt", "En cours d'exécution", "Suspendu", "Terminé"]
    def __str__(self):
        return "PID : "+str(self.pid) 
    
    def execute_un_cycle(self):
        """Met à jour le reste à faire après l'exécution d'un cycle."""
        if self.reste_a_faire>0:
            self.reste_a_faire-=1
    def change_etat(self, nouvel_etat):
        """Change l'état du processus avec la valeur passée en paramètre."""
        self.etat = nouvel_etat
    def est_termine(self):
        """Renvoie True si le processus est terminé, False sinon, en se basant sur le reste à faire."""
        if self.reste_a_faire ==0:
            return True
        return False
    
liste_attente = [Processus(11,4), Processus(20,2), Processus(32,3)]

def tourniquet(liste_attente, quantum):
    ordre_execution = []
    while liste_attente != []:
        # On extrait le premier processus
        processus = liste_attente.pop(0)
        processus.change_etat("En cours d'exécution")
        compteur_tourniquet = 0
        while not processus.est_termine() and compteur_tourniquet<quantum:
            ordre_execution.append(processus)
            processus.execute_un_cycle()
            compteur_tourniquet = compteur_tourniquet + 1
        if processus.reste_a_faire>0 :
            processus.change_etat("Suspendu")
            liste_attente.append(processus)
        else:
            processus.change_etat("Terminé")
    return ordre_execution


liste_attente1 = [Processus(11,4), Processus(20,2), Processus(32,3)]
E1 = tourniquet(liste_attente1,2)
print ("Execution avec quantum à 1")
for v in E1 :
    print(v)

    
liste_attente2 = [Processus(11,4), Processus(20,2), Processus(32,3)]
E2 = tourniquet(liste_attente2,2)
print ("Execution avec quantum à 2")
for v in E2 :
    print(v)