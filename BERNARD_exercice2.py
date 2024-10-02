# exercice2.py
from exercice1 import Robot

class Humain:
    def __init__(self, nom, sexe):
        self.__nom = nom
        self.__sexe = sexe
        self.__aliments = []

    def setNom(self, x):
        self.__nom = x

    def getNom(self):
        return self.__nom
    
    def setSexe(self, x):
        self.__sexe = x

    def getSexe(self):
        return self.__sexe
    
    def mangerAliment(self, aliment):
        self.__aliments.append(aliment)
        print(self.__nom, "vient d'ingérer l'aliment :", aliment)
        print("L'estomac de", self.__nom, "contient", self.__aliments)

    def digererAliment(self):
        if len(self.__aliments) != 0:
            self.__aliments.clear()
            print("L'estomac de", self.__nom, "est vide")
        else:
            print("L'estomac de", self.__nom, "est déjà vide")

class Cyborg(Robot, Humain):
    def __init__(self, nom, sexe):
        Robot.__init__(self, nom)
        Humain.__init__(self, nom, sexe)

    def cyborgSurpuissant(self):
        print(self.getNom(), "marque 35 buts en 20 matchs. Quel  TRRRRIIIIIIPPPLLLLEE   MOOOOONNSTTRREEEEEEE !!!!!!!!!!!!!!!!!!!!!!!!")
    

if __name__ == "__main__":
    cyborg1 = Cyborg("Haaland", "Homme")
    cyborg1.allumageRobot()
    cyborg1.eteindreRobot()
    cyborg1.chargementRobot()
    cyborg1.allumageRobot()
    cyborg1.mangerAliment("pomme")
    cyborg1.mangerAliment("banane")
    cyborg1.mangerAliment("fraise")
    cyborg1.mangerAliment("nutella")
    cyborg1.digererAliment()
    cyborg1.digererAliment()
    cyborg1.setVitesseDeplacement(60)
    cyborg1.afficherVitesse()
    cyborg1.etatGlobalRobot()
    cyborg1.stopDeplacement()
    cyborg1.etatGlobalRobot()
    cyborg1.cyborgSurpuissant()
    cyborg1.eteindreRobot()
