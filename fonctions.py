from random import randint

def debutTEX():
	document = "\\documentclass[12pt,a4paper]{article} \n  \n"

	document += "\\usepackage[utf8]{inputenc} \n"
	document += "\\usepackage[french]{babel} \n"
	document += "\\usepackage[T1]{fontenc} \n"
	document += "\\usepackage{fourier} \n"
	document += "\\usepackage{amsmath,amsfonts,amssymb} \n"
	document += "\\usepackage[left=2cm,right=2cm,top=1cm,bottom=0.5cm]{geometry} \n"
	document += "\\usepackage{xcolor} \n \n"

	document += "\\newcounter{nexo} \n"
	document += "\\setcounter{nexo}{0} \n"
	document += "\\newcommand{\\exo}{% \n"
	document += "\\stepcounter{nexo} \n"
	document += "{\\textbf{\\underline{\\textsc{Exercice \\arabic{nexo}}}} \\medskip}} \n \n"

	document += "\\setlength\\parindent{0mm} \n \n"

	return document


def docTEX(contenu):
	doc = debutTEX()
	doc += "\\begin{document} \n \n"
	doc += contenu
	doc += "\n \n\\end{document}"
	return doc

def sujet(date):
	document = "\\setcounter{nexo}{0}"
	document += "\\pagestyle{empty} \n\n"
	document += "{\\large \\textbf{Exercices notés - 2GT4}} \\hfill "+date+" \n \n"
	document += "\\bigskip \n \n"
	document += "Nom : \\dotfill Prénom : \\dotfill Note : \\dotfill \n \n"
	document += "\\bigskip \n \n"
	document += "\\textit{Toutes les réponses devront être justifiées. } \n \n"
	document += "\\bigskip \n \n"
	return document

def corrige(date):
	document = "\\setcounter{nexo}{0}"
	document = "\\pagestyle{empty} \n\n"
	document += "{\\large \\textbf{Exercices notés - 2GT4}} - {\\color{blue} Corrigé}\\hfill "+date+"\n \n"
	document += "\\bigskip \n \n"
	return document


class Question1Augm():

	def __init__(self):
		self.valeur = randint(11,89)
		self.coeff = (100+self.valeur)/100

	def enonce(self):
		texte = f"Quel est le coefficient multiplicateur associé à une augmentation de ${self.valeur}\\%$ ?"
		return texte

	def reponse(self):
		texte1 = f"$CM = 1 + \\dfrac{{{self.valeur}}}{{100}} = 1 + {self.valeur/100} = {(100+self.valeur)/100}$"
		texte1 = texte1.replace(".",",")
		texte2 = f"Augmenter une valeur de ${self.valeur}\\%$ revient à multiplier par $CM = {self.coeff}$"
		texte2 = texte2.replace(".",",")
		return texte1+". \\par \n"+texte2+". \n"


class Question1Dim():

	def __init__(self):
		self.valeur = randint(11,89)
		self.coeff = (100-self.valeur)/100

	def enonce(self):
		texte = f"Quel est le coefficient multiplicateur associé à une diminution de ${self.valeur}\\%$ ?"
		return texte

	def reponse(self):
		texte1 = f"$CM = 1 - \\dfrac{{{self.valeur}}}{{100}} = 1 - {self.valeur/100} = {(100-self.valeur)/100}$"
		texte1 = texte1.replace(".",",")
		texte2 = f"Diminuer une valeur de ${self.valeur}\\%$ revient à multiplier par $CM = {self.coeff}$"
		texte2 = texte2.replace(".",",")
		return texte1+". \\par \n"+texte2+". \n"


class Question2FinalAug():

	def __init__(self):
		self.prixDep = randint(101,499)
		self.valeur = randint(11,89)
		self.prixFin = self.prixDep + self.prixDep*self.valeur/100
		self.coeff = (100+self.valeur)/100
		self.coeffStr = str(self.coeff).replace(".",",")

	def enonce1(self):
		texte = f"Le prix d'un article est de ${self.prixDep}$ euros. On augmente le prix de cet article de ${self.valeur}\\%$. \\par \n"
		texte += "Quel est le prix final ? Justifier."
		return texte

	def reponse1(self):
		texte = f"Augmenter une valeur de {self.valeur}\\% revient à multiplier par $CM = {self.coeffStr}$. \\par \n"
		texte += f"${self.prixDep} \\times {self.coeffStr} = {self.prixFin}$. \\quad Le prix final est de ${self.prixDep}$ euros."
		return texte 

	def enonce2(self):
		texte = f"On a augmenté le prix d'un article de ${self.valeur}\\%$. Le prix final est de ${self.prixFin}$ euros. \\par \n"
		texte += "Quel était le prix de départ ? Justifier."
		return texte

	def reponse2(self):
		texte = f"Augmenter une valeur de {self.valeur}\\% revient à multiplier par $CM = {self.coeffStr}$. \\par \n"
		texte += f"On note $V_d$ le prix de départ. On a : $V_d \\times {self.coeff} = {self.prixFin}$. \\par \n"
		texte += f"D'où $V_d = \\dfrac{{{self.prixFin}}}{{{self.coeff}}} = {self.prixDep}$. \\quad Le prix initial était de ${self.prixDep}$ euros."
		return texte

class Question2FinalDim():

	def __init__(self):
		self.prixDep = randint(101,499)
		self.valeur = randint(11,89)
		self.prixFin = self.prixDep - self.prixDep*self.valeur/100
		self.coeff = (100-self.valeur)/100
		self.coeffStr = str(self.coeff).replace(".",",")

	def enonce1(self):
		texte = f"Le prix d'un article est de ${self.prixDep}$ euros. On diminue le prix de cet article de ${self.valeur}\\%$. \\par \n"
		texte += "Quel est le prix final ? Justifier."
		return texte

	def reponse1(self):
		texte = f"Diminuer une valeur de {self.valeur}\\% revient à multiplier par $CM = {self.coeffStr}$. \\par \n"
		texte += f"${self.prixDep} \\times {self.coeffStr} = {self.prixFin}$. \\quad Le prix final est de ${self.prixDep}$ euros."
		return texte

	def enonce2(self):
		texte = f"On a diminué le prix d'un article de ${self.valeur}\\%$. Le prix final est de ${self.prixFin}$ euros. \\par \n"
		texte += "Quel était le prix de départ ? Justifier."
		return texte

	def reponse2(self):
		texte = f"Diminuer une valeur de {self.valeur}\\% revient à multiplier par $CM = {self.coeffStr}$. \\par \n"
		texte += f"On note $V_d$ le prix de départ. On a : $V_d \\times {self.coeff} = {self.prixFin}$. \\par \n"
		texte += f"D'où $V_d = \\dfrac{{{self.prixFin}}}{{{self.coeff}}} = {self.prixDep}$. \\quad Le prix initial était de ${self.prixDep}$ euros."
		return texte

class Exo2:

	def __init__(self):
		self.valeur1 = randint(11,89)
		self.valeur2 = randint(11,89)
		self.CMchoix1 = (100+self.valeur1)*(100-self.valeur2)/10000
		self.CMchoix2 = (100-self.valeur1)*(100+self.valeur2)/10000

	def choix1(self):
		return f"Un article subit une augmentation de ${self.valeur1}\\%$ puis une diminution de ${self.valeur2}\\%$."

	def choix2(self):
		return f"Un article subit une diminution de ${self.valeur1}\\%$ puis une augmentation de ${self.valeur2}\\%$."

	def choix1rep1(self):
		texte = f"On a : $CM_1 = {(100+self.valeur1)/100}$ et $CM_2 = {(100-self.valeur2)/100}$. \\par \n"
		texte += f"$CM_g = CM_1 \\times CM_2 = {(100+self.valeur1)/100} \\times {(100-self.valeur2)/100} = {(100+self.valeur1)*(100-self.valeur2)/10000}$ \\par \n"
		texte += f"Le coefficient multiplicateur global est $CM_g = {(100+self.valeur1)*(100-self.valeur2)/10000}$."
		return texte 

	def choix1rep2(self):
		texte = f"$t_g = CM_g-1 = {self.CMchoix1} - 1 = {self.CMchoix1 - 1}$. \\quad Le taux d'évolution global est $t_g = {self.CMchoix1 - 1}$. \\par \n"
		texte += f"une augmentation de ${self.valeur1}\\%$ puis une diminution de ${self.valeur2}\\%$ correspondent à une évolution globale de {(self.CMchoix1-1)*100}\\%."
		return texte 

	def choix2rep1(self):
		texte = f"On a : $CM_1 = {(100-self.valeur1)/100}$ et $CM_2 = {(100+self.valeur2)/100}$. \\par \n"
		texte += f"$CM_g = CM_1 \\times CM_2 = {(100-self.valeur1)/100} \\times {(100+self.valeur2)/100} = {(100-self.valeur1)*(100+self.valeur2)/10000}$ \\par \n"
		texte += f"Le coefficient multiplicateur global est $CM_g = {(100-self.valeur1)*(100+self.valeur2)/10000}$."
		return texte 

	def choix2rep2(self):
		texte = f"$t_g = CM_g-1 = {self.CMchoix2} - 1 = {self.CMchoix2 - 1}$. \\quad Le taux d'évolution global est $t_g = {self.CMchoix2 - 1}$. \\par \n"
		texte += f"une diminution de ${self.valeur1}\\%$ puis une augmentation de ${self.valeur2}\\%$ correspondent à une évolution globale de {(self.CMchoix2-1)*100}\\%."
		return texte 

	def q1(self):
		return "Calculer le coefficient multiplicateur $CM_g$ associé à cette évolution."

	def q2(self):
		return "En déduire le taux d'évolution $t_g$ associé."

def sujetA(date,q1,q2,q3,q4,q5):

	## Construction du sujet 

	enonce = sujet(date)

	enonce += "\\exo \n \n"
	enonce += "\\begin{enumerate} \n"
	enonce += "\\item "+q1.enonce()+"\n\n\\vspace{1,5cm}\n\n"
	enonce += "\\item "+q2.enonce()+"\n\n\\vspace{1,5cm}\n\n"
	enonce += "\\item "+q3.enonce1()+"\n\n\\vspace{4cm}\n\n"
	enonce += "\\item "+q4.enonce2()+"\n\n\\vspace{4cm}\n\n"
	enonce += "\\end{enumerate} \n\n"

	enonce += "\\exo \n \n"
	enonce += q5.choix1()
	enonce += "\n\n"
	enonce += "\\begin{enumerate} \n"
	enonce += "\\item "+q5.q1()+"\n\n\\vspace{4cm}\n\n"
	enonce += "\\item "+q5.q2()+"\n\n"
	enonce += "\\end{enumerate} \n\n"

	## Construction du corrigé

	reponse = corrige(date)

	reponse += "\\exo \n \n"
	reponse += "\\begin{enumerate} \n"
	reponse += "\\item "+q1.enonce()+"\n\n"
	reponse += "{\\color{blue} "+q1.reponse()+"} \n\n"
	reponse += "\\medskip \n\n"
	reponse += "\\item "+q2.enonce()+"\n\n"
	reponse += "{\\color{blue} "+q2.reponse()+"} \n\n"
	reponse += "\\medskip \n\n"
	reponse += "\\item "+q3.enonce1()+"\n\n"
	reponse += "{\\color{blue} "+q3.reponse1()+"} \n\n"
	reponse += "\\medskip \n\n"
	reponse += "\\item "+q4.enonce2()+"\n\n"
	reponse += "{\\color{blue} "+q4.reponse2()+"} \n\n"
	reponse += "\\medskip \n\n"
	reponse += "\\end{enumerate} \n\n"

	reponse += "\\exo \n \n"
	reponse += q5.choix1()
	reponse += "\n\n"
	reponse += "\\begin{enumerate} \n"
	reponse += "\\item "+q5.q1()+"\n\n"
	reponse += "{\\color{blue} "+q5.choix1rep1()+"} \n\n"
	reponse += "\\medskip \n\n"
	reponse += "\\item "+q5.q2()+"\n\n"
	reponse += "{\\color{blue} "+q5.choix1rep2()+"} \n\n"
	reponse += "\\end{enumerate} \n\n"

	return enonce,reponse

def sujetB(date,q1,q2,q3,q4,q5):

	## Construction du sujet 

	enonce = sujet(date)

	enonce += "\\exo \n \n"
	enonce += "\\begin{enumerate} \n"
	enonce += "\\item "+q1.enonce()+"\n\n\\vspace{1,5cm}\n\n"
	enonce += "\\item "+q2.enonce()+"\n\n\\vspace{1,5cm}\n\n"
	enonce += "\\item "+q3.enonce1()+"\n\n\\vspace{4cm}\n\n"
	enonce += "\\item "+q4.enonce2()+"\n\n\\vspace{4cm}\n\n"
	enonce += "\\end{enumerate} \n\n"

	enonce += "\\exo \n \n"
	enonce += q5.choix2()
	enonce += "\n\n"
	enonce += "\\begin{enumerate} \n"
	enonce += "\\item "+q5.q1()+"\n\n\\vspace{4cm}\n\n"
	enonce += "\\item "+q5.q2()+"\n\n"
	enonce += "\\end{enumerate} \n\n"

	## Construction du corrigé

	reponse = corrige(date)

	reponse += "\\exo \n \n"
	reponse += "\\begin{enumerate} \n"
	reponse += "\\item "+q1.enonce()+"\n\n"
	reponse += "{\\color{blue} "+q1.reponse()+"} \n\n"
	reponse += "\\medskip \n\n"
	reponse += "\\item "+q2.enonce()+"\n\n"
	reponse += "{\\color{blue} "+q2.reponse()+"} \n\n"
	reponse += "\\medskip \n\n"
	reponse += "\\item "+q3.enonce1()+"\n\n"
	reponse += "{\\color{blue} "+q3.reponse1()+"} \n\n"
	reponse += "\\medskip \n\n"
	reponse += "\\item "+q4.enonce2()+"\n\n"
	reponse += "{\\color{blue} "+q4.reponse2()+"} \n\n"
	reponse += "\\medskip \n\n"
	reponse += "\\end{enumerate} \n\n"

	reponse += "\\exo \n \n"
	reponse += q5.choix2()
	reponse += "\n\n"
	reponse += "\\begin{enumerate} \n"
	reponse += "\\item "+q5.q1()+"\n\n"
	reponse += "{\\color{blue} "+q5.choix2rep1()+"} \n\n"
	reponse += "\\medskip \n\n"
	reponse += "\\item "+q5.q2()+"\n\n"
	reponse += "{\\color{blue} "+q5.choix2rep2()+"} \n\n"
	reponse += "\\end{enumerate} \n\n"

	return enonce,reponse