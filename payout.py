def payout(nb_j, montant_est, repa):
    taxe = 0.895
    montant_rendu = (montant_est * taxe - repa)/nb_j
    return round(montant_rendu,0)

nb_j = int(input('Combien de joueurs ? '))
montant_est = int(input("De combien est le montant estimé de l'inventaire ? (800k = 800) " ))
repa = int(input('Combien ont couté les réparations ? (200k = 200) '))

input('Chaque joueur doit recevoir ' + str(payout(nb_j,montant_est,repa)) +"K ! ")