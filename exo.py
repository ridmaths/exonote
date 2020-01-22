
from fonctions import *

date = "23/01/2020"

document = ""

for k in range(20):
	if (k%2==0):
		question1 = Question1Augm()
		question2 = Question1Dim()
		question3 = Question2FinalAug()
		question4 = Question2FinalDim()
		question5 = Exo2()
		enonce,reponse = sujetA(date,question1,question2,question3,question4,question5)
	else:
		question1 = Question1Dim()
		question2 = Question1Augm()
		question3 = Question2FinalDim()
		question4 = Question2FinalAug()
		question5 = Exo2()
		enonce,reponse = sujetB(date,question1,question2,question3,question4,question5)

	document += enonce+"\\newpage \n \n"+reponse+"\\newpage \n\n"


sujetComplet = docTEX(document)

fichier = open("enonceNote.tex","w",encoding="utf8")
fichier.write(sujetComplet)
fichier.close()

print(sujetComplet)