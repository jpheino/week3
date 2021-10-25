from statistics import mode

syote = input("Anna numeroita pilkulla eroteltuna: ")

lista = list((syote.split(",")))
numerot = list(map(int, lista))



suurin = max(numerot)
pienin = min(numerot)
mediaani = len(numerot)//2
moodi = mode(numerot)
pituus = len(numerot)
summa = sum(numerot)
keskiarvo = summa/pituus

print(f"suurin luku = {suurin}, pienin luku = {pienin}, lukujen keskiarvo = {keskiarvo}, mediaani = {syote[mediaani]}, moodi = {moodi}")
