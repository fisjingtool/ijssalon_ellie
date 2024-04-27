
def presenteer(dictionary, totaal):
    for k, v in dictionary.items():
        print(f"{k} : {v} euro")
    print("=====================")
    totaal = sum(dictionary.values())
    print(f"Totaal : {totaal} euro.")

   

