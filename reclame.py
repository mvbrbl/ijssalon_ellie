#Huiswerkopdracht 12
from algemene_functies import mijn_functie_2

#Huiswerkopdracht 5

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs - (prijs * korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro."

print(aanbieding_1("aardbei", 4, 0.1))

#Huiswerkopdracht 6 en 7

def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal:.2f} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."


week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(inkomsten_totaal(week_inkomsten, 0.09))

#Huiswerkopdracht 8

def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return [hoogste, laagste]

week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(laag_en_hoog(week_inkomsten))

#Huiswerkopdracht 9 en 10

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    gemiddelde_waarde = totaal / aantal
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_waarde:.2f} euro."

week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(gemiddelde(week_inkomsten))

#Huiswerkopdracht 11

def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return [hoogste, laagste]

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

getallen = [10, 5, 3, 2, 1, 2, 9]
print(meervoudig(getallen))

#Huiswerkopdracht 12 vervolg

def combinatie(invoer_lijst_2):
    return laag_en_hoog(invoer_lijst_2)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0], korte_lijst[1])