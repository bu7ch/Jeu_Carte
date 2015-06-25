class Carte:
	def __init__(self, val, coul):
		if val < 2 or val > 14:
			print("Erreur :	La valeur d'une carte est comprise entre 2 et 14")
		exit(1)
		if coul < 0 or coul > 3:
			print("Erreur: Le code couleur d'une carte est comprise entre 0 et 3")
		exit(1)
		self.valeur = val
		self.couleur = coul

	def affiche(self):
		affiche_valeur = None
		affiche_couleur = None

		if self.valeur <= 10:
			affiche_valeur = self.valeur
		elif self.valeur == 11:
			affiche_valeur = "Valet"
		elif self.valeur == 12:
			affiche_valeur = "Dame"
		elif self.valeur == 13:
			affiche_valeur = "Roi"
		else:
			affiche_valeur = "As"

		if self.couleur == 0:
			affiche_couleur = "Coeur"
		elif self.couleur == 1:
			affiche_couleur = "Carreaux"
		elif self.couleur == 2:
			affiche_couleur = "Trefle"
		else:
			affiche_couleur = "Pique"

		print(affiche_valeur, "de", affiche_couleur)
