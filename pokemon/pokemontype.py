class Pokemon_type():
    def __init__(self, nom, pv, attaque, defense):
        self.__nom = nom
        self.__pv = pv
        self.__attaque = attaque
        self.__defense = defense

    # getter
    def get_nom(self):
        return self.__nom
    
    def get_pv(self):
        return self.__pv
    
    def get_attaque(self):
        return self.__attaque
    
    def get_defense(self):
        return self.__defense
    # setter
    def set_nom(self):
        return self.__nom
    
    def set_pv(self):
        return self.__pv
    
    def set_attaque(self):
        return self.__attaque
    
    def set_defense(self):
        return self.__defense

# Créaction des types de pokemon
class Normal(Pokemon_type):
    def __init__(self, nom,):
        super().__init__(nom, 100, 50, 60)

class Feu(Pokemon_type):
    def __init__(self, nom):
        super().__init__(nom, 100, 55, 63)

class Eau(Pokemon_type):
    def __init__(self, nom):
        super().__init__(nom, 100, 60, 70)

class Terre(Pokemon_type):
    def __init__(self, nom):
        super().__init__(nom, 100, 59, 69)

if __name__ == "__main__":
    print("Menu:")

# Créaction d'un pokemon
class Pokemon_nom(Normal):
    def __init__(self, nom):
        super().__init__(nom)
        
    def affich():
        info = int(input("Veuillz appuyer sur 1 pour les pokemons:"))
        print("r",info)
af = Normal()
print(af.affich())

    

    





    

    


    



