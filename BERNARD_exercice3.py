from abc import ABCMeta, abstractmethod

class Vehicule(metaclass=ABCMeta):
    pass

class UnmannedVehicule(Vehicule):
    @abstractmethod
    def mission(self):
        pass

class AerialVehicule(Vehicule):
    @abstractmethod
    def vol(self):
        pass

class UnderseaVehicule(Vehicule):
    @abstractmethod
    def plongee(self):
        pass

class GroundVehicule(Vehicule):
    @abstractmethod
    def conduite(self):
        pass

class UAV(UnmannedVehicule, AerialVehicule):
    def mission(self):
        print("UAV: Execution de la mission en vol:")
    
    def vol(self):
        print("UAV: Decollage et vol en cours...")

class UUV(UnmannedVehicule, UnderseaVehicule):
    def mission(self):
        print("UUV: Execution de la mission sous-marine:")
    
    def plongee(self):
        print("UUV: Plongee en cours...")

class UGV(UnmannedVehicule, GroundVehicule):
    def mission(self):
        print("UGV: Execution de la mission terrestre:")
    
    def conduite(self):
        print("UGV: Conduite en cours...")

def main():
    vehicules = [UAV(), UUV(), UGV()]
    for vehicule in vehicules:
        vehicule.mission()
        if isinstance(vehicule, AerialVehicule):
            vehicule.vol()
        elif isinstance(vehicule, UnderseaVehicule):
            vehicule.plongee()
        elif isinstance(vehicule, GroundVehicule):
            vehicule.conduite()

if __name__ == "__main__":
    main()
