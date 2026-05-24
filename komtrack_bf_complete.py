
class Produit:

    def __init__(self, nom: str, categorie: str, prix_achat: float,
                 prix_vente: float, quantite: int, seuil_alerte: int,
                 actif: bool):

        self.nom = nom
        self.categorie = categorie
        self.prix_achat = prix_achat
        self.prix_vente = prix_vente
        self.quantite = quantite
        self.seuil_alerte = seuil_alerte
        self.actif = actif

# PART 3 — Magic Methods (__str__, __eq__, __len__)
    def __str__(self):
        statut = "Actif" if self.actif else "Inactif"
        alerte = " ⚠ STOCK BAS" if self.est_en_alerte() else ""

        return (
            f"[{statut}] {self.nom} | "
            f"Catégorie: {self.categorie} | "
            f"Achat: {self.prix_achat:.0f} FCFA | "
            f"Vente: {self.prix_vente:.0f} FCFA | "
            f"Quantité: {self.quantite}{alerte}"
        )

    @property
# PART 4 — Decorators (@property)
    def valeur_stock(self) -> float:
        return self.prix_achat * self.quantite

    def calculer_marge(self) -> float:
        return ((self.prix_vente - self.prix_achat) / self.prix_achat) * 100

    def est_en_alerte(self) -> bool:
        return self.quantite <= self.seuil_alerte

    def enregistrer_vente(self, quantite_vendue: int) -> float:
        if quantite_vendue > self.quantite:
            print(f"⚠ Stock insuffisant — disponible : {self.quantite}")
            return 0.0

        self.quantite -= quantite_vendue
        return (self.prix_vente - self.prix_achat) * quantite_vendue


class ProduitAlimentaire(Produit):
    def __init__(self, nom, categorie, prix_achat, prix_vente,
                 quantite, seuil_alerte, actif, unite):
        super().__init__(nom, categorie, prix_achat, prix_vente,
                         quantite, seuil_alerte, actif)
        self.unite = unite

    def afficher(self):
        print(self)



def saisir_float(message):
    while True:
        try:
            v = float(input(message))
            if v <= 0:
                print("Valeur > 0 requise")
                continue
            return v
        except:
            print("Entrée invalide")


def saisir_int(message, min_val=0):
    while True:
        try:
            v = int(input(message))
            if v < min_val:
                print(f"Min {min_val}")
                continue
            return v
        except:
            print("Entrée invalide")


def ajouter_produit():
    print("\n--- AJOUT PRODUIT ---")

    nom = input("Nom: ")
    categorie = input("Catégorie: ")
    est_alim = input("Alimentaire ? (oui/non): ").lower() == "oui"
    prix_achat = saisir_float("Prix achat: ")
    prix_vente = saisir_float("Prix vente: ")
    quantite = saisir_int("Quantité: ", 1)
    seuil = saisir_int("Seuil alerte: ", 1)
    actif = input("Actif ? (oui/non): ").lower() == "oui"

    if est_alim:
        unite = input("Unité: ")
        return ProduitAlimentaire(nom, categorie, prix_achat,
                                   prix_vente, quantite, seuil,
                                   actif, unite)

    return Produit(nom, categorie, prix_achat,
                   prix_vente, quantite, seuil, actif)


def enregistrer_vente(stock):
    if not stock:
        print("Stock vide")
        return 0

    for i, p in enumerate(stock):
        print(i + 1, p.nom, p.quantite)

    try:
        choix = int(input("Choix: ")) - 1
        qte = saisir_int("Quantité: ", 1)
        return stock[choix].enregistrer_vente(qte)
    except:
        print("Erreur")
        return 0


def afficher_tableau_de_bord(stock, benefice):
    print("\n===== TABLEAU DE BORD =====")

    valeur_stock = sum(p.valeur_stock for p in stock)

    print(f"Valeur stock: {valeur_stock}")
    print(f"Bénéfice total: {benefice}")

    for p in stock:
        print(p)


def main():
    stock = []
    benefice_total = 0

    while True:
        print("\n1. Ajouter produit")
        print("2. Vente")
        print("3. Tableau de bord")
        print("4. Quitter")

        choix = input("> ")

        if choix == "1":
            stock.append(ajouter_produit())

        elif choix == "2":
            benefice_total += enregistrer_vente(stock)

        elif choix == "3":
            afficher_tableau_de_bord(stock, benefice_total)

        elif choix == "4":
            break


if __name__ == "__main__":
    main()
