import time

class Robot:

    '''
    Constructeur de la classe Robot
    '''

    def __init__(self, nom):
        self.__nom = nom
        self.__power = False
        self.__vitesse_actuelle = 0
        self.__niveau_batterie = 0
        self.__etats = ['éteint', 'allumé']

    '''
    Getters et setters de la classe
    '''

    def setNom(self, x):
        self.__nom = x

    def getNom(self):
        return self.__nom
    
    def setPower(self, x):
        self.__Power = x

    def getPower(self):
        return self.__Power
    
    def setNiveauBatterie(self, x):
        self.__niveau_batterie = x

    def getNiveauBatterie(self):
        return self.__niveau_batterie
    
    def setVitesseDeplacement(self, x):
        if (self.__power == True):
            self.__vitesse_actuelle = x

    def getVitesseDeplacement(self):
        return self.__vitesse_actuelle
    
    '''
    Méthodes de la classe
    '''

    def allumageRobot(self):
        if (self.__power == False):
            self.__power = True
            print("Le robot", self.__nom, "est", self.__etats[1])
        else:
            print("Le robot", self.__nom, "est deja", self.__etats[1])

    def eteindreRobot(self):
        if (self.__power == True):
            self.__power = False
            print("Le robot", self.__nom, "est", self.__etats[0])
        else:
            print("Le robot", self.__nom, "est deja", self.__etats[0])

    def chargementRobot(self):
        if self.__niveau_batterie < 100:
            print("Chargement du Robot ...")
            time1 = time.perf_counter()
            while (self.__niveau_batterie != 100):
                time.sleep(1)
                self.__niveau_batterie += 10
                print("Niveau de batterie =", self.__niveau_batterie, "%")
            print("Robot chargé à 100 %")
            time2 = time.perf_counter()
            temps_de_charge = time2 - time1
            print("Le chargement a pris {:.2f} secondes".format(temps_de_charge))
        else:
            print("Le robot est deja chargé")

    def afficherVitesse(self):
        print("La vitesse du robot est de", self.__vitesse_actuelle, "km/h.")

    def stopDeplacement(self):
        if (self.__power == True):
            self.__vitesse_actuelle = 0
            print("Le robot s'arrête.")

    def etatGlobalRobot(self):
        if (self.__power == True):
            etat = self.__etats[1]
        else:
            etat = self.__etats[0]
        print("Le robot", self.__nom, "est", etat,", est chargé à", self.__niveau_batterie, "%, et se déplace à une vitesse de", self.__vitesse_actuelle, "km/h.")

if __name__ == "__main__":
    robot1 = Robot("R2D2")
    robot1.allumageRobot()
    robot1.eteindreRobot()
    robot1.chargementRobot()
    robot1.allumageRobot()
    robot1.setVitesseDeplacement(60)
    robot1.afficherVitesse()
    robot1.etatGlobalRobot()
    robot1.stopDeplacement()
    robot1.etatGlobalRobot()
    robot1.eteindreRobot()




