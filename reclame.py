from algemene_functies import mijn_functie2
#5
def aanbieding_1(smaak,prijs,korting):
    korting1 = prijs * korting
    korting = prijs - korting1 
    uitvoer =f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro."
    print(uitvoer)
#aanbieding_1("aardbei",4,0.1)


#6
inkomsten = [220, 430, 125, 160, 205, 90, 345]
def inkomsten_totaal(inkomsten):
   print(sum(inkomsten))
#inkomsten_totaal(inkomsten)
 
#7

inkomsten = [220, 430, 125, 160, 205, 90, 345]
def inkomsten_totaal(inkomsten,btw):
    totaal =(sum(inkomsten))
    bedrag = btw * totaal    
    uitvoer =f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
    print(uitvoer)
#inkomsten_totaal(inkomsten, 0.09)




#8

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]

def laag_en_hoog(mijn_lijst):
  laag = min(mijn_lijst)
  hoog = max(mijn_lijst)
  print(laag ,hoog)
#laag_en_hoog(mijn_lijst)

#9

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    gemiddelde = totaal / 7 
    uitvoer =f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."
    print(uitvoer)


#11
invoerlijst = [10,5,3,2,1,2,9]
def meervoudig(invoerlijst):
  laag_en_hoog(invoerlijst)
#meervoudig(invoerlijst)

#12
invoer_lijst_2 = [10, 20, 60, 70]
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie2(korte_lijst[0], korte_lijst[1])
    return uitvoer
#    print(korte_lijst)
combinatie(invoer_lijst_2)



