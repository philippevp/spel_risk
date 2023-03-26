from dobbelsteen import Dobbelsteen
# import random

class Land:

    def __init__(self, naam, is_aanvaller, soldaten):
        self.naam = naam
        self.soldaten = soldaten
        self.is_aanvaller = is_aanvaller
        self.aantal_dobbelstenen = 0
        self.lijst_worpen = []
        self.lijst_values = []

    def input_verdediger(self):
        aantal_dobbelstenen = int(input("Verdediger, met hoeveel dobbels wil je werpen: "))
        while aantal_dobbelstenen > self.soldaten:
            print("Sorry, zoveel soldaten heb je niet meer.")
            aantal_dobbelstenen = int(input("Verdediger, met hoeveel dobbels wil je werpen: "))
        return aantal_dobbelstenen

    def aantal_dobbels(self):
        if self.is_aanvaller == True:
            if self.soldaten < 3:
                self.aantal_dobbelstenen = self.soldaten
            else:
                self.aantal_dobbelstenen = 3
        else:
            self.aantal_dobbelstenen = self.input_verdediger()

            # if self.soldaten < 2:
            #     self.aantal_dobbelstenen = self.soldaten
            # else:
            #     self.aantal_dobbelstenen = 2
    
      
    def rol_dobbelstenen(self):
        self.lijst_worpen = []
        for i in range(self.aantal_dobbelstenen):
            dobbelsteen = Dobbelsteen()
            dobbelsteen.worp()
            self.lijst_worpen.append(dobbelsteen)
        self.geef_values()

    def geef_values(self):
        self.lijst_values = []
        for dobbel in self.lijst_worpen:
            self.lijst_values.append(dobbel.value)
        # return self.lijst_values

    def ledig_lijst_worpen(self):
        self.lijst_worpen = []




def main():
    land = Land("BE",False,5)
    # land.aantal_dobbels_aanvaller()
    land.aantal_dobbels()
    # print(land.aantal_dobbelstenen)
    land.rol_dobbelstenen()
    print(land.lijst_worpen)
    for dobbel in land.lijst_worpen:
        print(dobbel.value)
    



if __name__ == "__main__":
   main()