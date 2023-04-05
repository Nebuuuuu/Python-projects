géantemaquereau=0
géantemaquereauautre=0
benef=0
autre=12000


géante = int(input("Prix géante/u ? "))
maquereau=int(input("Prix maquereau/u ? "))
divine=int(input("prix divine/u ? "))

géante=géante*30
maquereau=maquereau*3
divine=divine*10
géantemaquereau=(géante+maquereau)

#print (géantemaquereau)
géantemaquereauautre=(géantemaquereau+autre)
#print (géantemaquereauautre)
benef=(divine-géantemaquereauautre)

phrase1 = "Tu fais un benef de " + str(benef)
phrase2 = "Tu fais un déficit de " +str(benef*-1)
if benef>=0:
    print(phrase1)
else:
    benef=benef*-1
    print(phrase2)

input("Appuier sur entrer pour quitter ! \n ")