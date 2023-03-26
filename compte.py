"""

"""

import json
import random

class CompteBancaire :
    
    
    
    def __init__(self,numeroCompte, nom, solde ) :
        self.numCompte = numeroCompte
        self.nom = nom
        self.solde = solde
        self.montantAgios = 0 
        
        
    def versement(self, soldVersement ) :
        
        self.solde += soldVersement
        print(f"nouveau montant : {self.solde}\n\n")
        
    def retrait(self, montant) :
        
        if montant < self.solde  :
             self.solde -= montant
             print(f"solde restant : {self.solde}\n\n")
            
        else :
           print("Solde Insufisant\n\n")
            
        
    def agios(self) :
        self.montantAgios = (self.solde*5)/100
        self.solde += self.montantAgios 
        
        
        
        
    def afficher(self) :
        print(f"================================================\nnumero de compte : {self.numCompte}\nProprietaire : {self.nom}\nSolde : {self.solde} XAF\nDernier agios : {self.montantAgios}\n================================================")
        
        

class Client :
    
    def __init__(self, nom, prenom, telephone) :
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        
    def creer_compte(self) :
        self.numCompte = self.nom+self.prenom+str(random.randint(0, 999999))
        
        try :
            with open('db.json', 'r') as db : 
                data = json.load(db)
                #print(data)
        except FileNotFoundError :
            with open('db.json', 'w') as file :
                data = json.dump({'users' : {}, "key" : 0}, file, sort_keys=True, indent=4)
            #data = json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4)
        finally :
            data = None
            with open('db.json', 'r') as file :
                data = json.load(file)
                
            fill = False
            
            if len(data['users']) > 0 :
                for i in data['users'] :
                    if self.nom == data['users'][i]['nom'] and self.prenom == data['users'][i]['prenom'] and self.telephone == data['users'][i]['telephone'] :
                        print("Ce compte existe deja")
                        fill = False
                        break                        
                    else :
                        fill = True
                        continue
            else :
                fill = True

            if fill :
                data['users'][str(data["key"])] = {'nom' : self.nom, 'prenom' : self.prenom, 'telephone' : self.telephone, 'numCompte' : self.numCompte}
                print(data)
                data['key'] = data['key'] + 1
                print(data)
                
                print(data)  
                with open('db.json', 'w') as file :
                    json.dump(data, file, sort_keys=True, indent=4,)
                    
                    print("Client enreigistrer !")
                    
        return self.numCompte
                
                
    
    class BD :
        
        def __init__(self, user, password) :
            
            try :
                with open("db_user", "r") as file:
                     file.read()
            except FileNotFoundError :
                print("Configration de base.....")
                with open("db_user", "w") as file:
                    print("creation des fichiers base de donnees")
                    json.dump({"users" : {}, "key" : 0})
                    print("Terminee !")
            finally :
                self.user = user
                self.password = password 
            
            
        def login(self) :
            data = None
            with open("db_user", "r") as file :
                data = json.load(file)
                 
                
                
            
        
    
    def suprimer_compte(self) :
        pass
    
    def faire_retrait(self) :
        pass
    
    def faire_versement(self) :
        pass

    
cl = Client('paulin', 'ardi75', '068541193')
cl.creer_compte()


compte1 = CompteBancaire('AZ456', 'MANTSILA Clodlin', 20000)
compte1.afficher()



""" while True :
    rep = int(input("Menu : \n1-Versement\n2-Retraint\n3- Afficher\n4- Quitter \n\n~>"))

    if rep == 1 :
        montant = int(input("Entrer le montant du versement : "))
        compte1.versement(montant)
        
    elif rep == 2 :
        montant = int(input("Entrer le montant du retrait : "))
        compte1.retrait(montant)
        
    elif rep == 3 :
        compte1.afficher()
    
    elif rep == 4 :
        break
    
    elif rep == 50 :
        compte1.agios()
        compte1.afficher()
        
    else :
        print("erreur\n")

"""