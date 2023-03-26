from land import Land

class Gevecht:
    def __init__(self, gevecht_id, land1, land2):
        self.gevecht_id = gevecht_id
        self.land1 = land1
        self.land2 = land2
        self._aanv_verd_vaststellen()


    def _aanv_verd_vaststellen(self):
        if self.land1.is_aanvaller == True:
            self.aanvaller = self.land1
            self.verdediger = self.land2
        else:
            self.aanvaller = self.land2
            self.verdediger = self.land1

    def vergelijk(self, aanvaller, verdediger):
        self.verlies_aanvaller = 0
        self.verlies_verdediger = 0

        lijstaanvaller = aanvaller.lijst_values
        lijstverdediger = verdediger.lijst_values

        while len(lijstaanvaller) >= 1 and len(lijstverdediger) >= 1:
            if max(lijstaanvaller) > max(lijstverdediger):
                self.verlies_verdediger += 1
            else:
                self.verlies_aanvaller += 1

            lijstaanvaller.remove(max(lijstaanvaller))
            lijstverdediger.remove(max(lijstverdediger))


        print(f"verlies aanvaller: {self.verlies_aanvaller}")
        print(f"verlies verdediger: {self.verlies_verdediger}")

        aanvaller.soldaten = aanvaller.soldaten - self.verlies_aanvaller
        verdediger.soldaten = verdediger.soldaten - self.verlies_verdediger

        self.verlies_aanvaller = 0
        self.verlies_verdediger = 0

        print(f"Totaal aantal soldaten aanvaller na gevecht: {aanvaller.soldaten}")
        print(f"Totaal aantal soldaten verdediger na gevecht: {verdediger.soldaten}")
    

    def winnaar_naam(self):
        if self.land1.soldaten == 0:
            winnaar = self.land2.naam
        else:
            winnaar = self.land1.naam
        return winnaar

    def spel_ronde(self):
        self.aanvaller.aantal_dobbels()
        self.aanvaller.rol_dobbelstenen()
        self.aanvaller.geef_values()
        print("Aanvaller gooit:")
        print(self.aanvaller.lijst_values)


        self.verdediger.aantal_dobbels()
        self.verdediger.rol_dobbelstenen()
        self.verdediger.geef_values()
        print("Verdediger gooit:")
        print(self.verdediger.lijst_values)


    def speel(self):
            print(f"Aanvaller is: {self.aanvaller.naam}")
            print(f"Verdediger is: {self.verdediger.naam}")

            while self.aanvaller.soldaten > 0 and self.verdediger.soldaten > 0:
                self.spel_ronde()

                print(f"Totaal aantal soldaten aanvaller: {self.aanvaller.soldaten}")
                print(f"Totaal aantal soldaten verdediger: {self.verdediger.soldaten}")
                self.vergelijk(self.aanvaller, self.verdediger)

                if self.aanvaller.soldaten > 0 and self.verdediger.soldaten > 0:
                    aanvaller_doorvechten = input("Aanvaller, wil je verder doen [y] of stoppen [q]?")
                    if aanvaller_doorvechten == 'q':
                        break
                    print("Volgende worp.")
                    print("")
            
            print("")
            print(f"Spel is gedaan, winnaar is: {self.winnaar_naam()}")



def main():
    landA = Land("Jeff",True,5)
    landB = Land("Papa",False,5)
    
    gevecht1=Gevecht(1,landA, landB)
    # print(gevecht1.aanvaller.naam)
    # print(gevecht1.verdediger.naam)    
    gevecht1.speel()
    

if __name__ == "__main__":
   main()