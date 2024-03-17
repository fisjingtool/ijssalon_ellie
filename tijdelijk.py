prijzen = {
"aardbei" : 3,
"vanille" : 4,
"chocolade" : 5
}

#3
aanbieding = (prijzen["aardbei"]) * 0.8

#4
reclame_tekst = (f"Vandaag in de aanbieding: aardbei-ijs, 1 liter – slechts € {aanbieding}")
#5
reclame_tekst2 = reclame_tekst[:63]
#6
reclame_tekst = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter – slechts € {aanbieding}")
reclame_tekst3 = reclame_tekst2.upper()
#7
reclame_tekst4 = (reclame_tekst3).split()
#8# en 9

#for el in reclame_tekst4:
#    print(el.lower())

for el in reclame_tekst4:
    if len(el) >= 5:
        print(el.lower())
    if len(el) < 5:
        print(el.upper())

