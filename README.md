# KomTrack BF 🇧🇫

**Mobile Management Platform for Small Traders in Burkina Faso**  
CS27 — Advanced Programming | Burkina Institute of Technology  
Group Assignment 1 — May 2026

---

## What This Program Does

KomTrack BF is a command-line stock management system designed for small traders in Ouagadougou. It allows a merchant to add products to their inventory, record sales, track profit, and receive low-stock alerts — all through a simple text-based interface.

This project is the Python implementation of the KomTrack BF concept developed during the CS27 IT Project Management course, where the team designed a full project plan (charter, WBS, budget, risk register) for a real-world trading management platform in the Burkinabe context.

---

## Classes

### `Produit` (Parent class)

Represents a generic product in stock.

| Attribute | Type | Description |
|---|---|---|
| `nom` | `str` | Product name |
| `categorie` | `str` | Category (e.g. Alimentation, Hygiène) |
| `prix_achat` | `float` | Purchase price in FCFA |
| `prix_vente` | `float` | Sale price in FCFA |
| `quantite` | `int` | Current stock quantity |
| `seuil_alerte` | `int` | Minimum quantity before alert |
| `actif` | `bool` | Whether the product is available for sale |

**Methods:**
- `calculer_marge()` — returns the profit margin as a percentage
- `est_en_alerte()` — returns `True` if stock is at or below the alert threshold
- `enregistrer_vente(quantite_vendue)` — updates stock and returns the profit generated
- `afficher()` — prints a formatted summary of the product

---

### `ProduitAlimentaire(Produit)` (Child class)

Inherits from `Produit`. Adds one attribute specific to food products.

| Added Attribute | Type | Description |
|---|---|---|
| `unite` | `str` | Unit of measure (kg, litre, sachet, boîte…) |

Overrides `afficher()` to include the unit of measure in the display.

---

## How to Run

**Requirements:** Python 3.8 or higher. No external libraries needed.

```bash
# Clone the repository
git clone https://github.com/<kevin23phx>/<https://github.com/Kevin23phx/Advanced_Programming.git>.git
cd <https://github.com/Kevin23phx/Advanced_Programming.git>

# Run the program
python3 komtrack_bf.py
```

Once running, you will be prompted with a menu:

```
--- MENU PRINCIPAL ---
  1. Ajouter un produit
  2. Enregistrer une vente
  3. Voir le tableau de bord
  4. Quitter
```

Follow the prompts. All inputs are validated — the program will re-ask on invalid entries and never crash on bad input.

---

## Assignment Structure

This project covers all four parts of Group Assignment 1.

| Part | Topic | Status |
|---|---|---|
| Part 1 | Fix the Foundations — data types, booleans, input validation, f-strings, arithmetic | ✅ Done |
| Part 2 | Inheritance — `Produit` parent, `ProduitAlimentaire` child, `super().__init__()` | ✅ Done |
| Part 3 | Magic Methods — `__str__`, `__len__`, `__eq__` or similar | 🔄 In progress |
| Part 4 | Decorators — `@staticmethod`, `@classmethod`, or `@property` | 🔄 In progress |

---

## Part 1 Checklist

- **All four data types used correctly:**  `str` (name, category), `int` (quantity, threshold), `float` (prices in FCFA), `bool` (active status, food flag)
- **Correct boolean pattern:** `is_member = input("...").lower() == "oui"` — never `bool(input(...))`
- **10+ `input()` calls** with correct type casting throughout the program
- **3+ arithmetic expressions:** profit margin, transaction profit, total stock value, potential revenue, transaction receipt
- **Input validation:** `saisir_float()` and `saisir_int()` both use `while True` + `try/except` — re-prompts on bad input, never crashes
- **f-strings** used for all output
- **Summary screen** shown at exit and accessible from the menu

## Part 2 Checklist

- `class Produit:` — parent class with shared attributes and methods
- `class ProduitAlimentaire(Produit):` — child class, IS-A relationship is valid
- `super().__init__(...)` called in the child constructor
- Child adds `self.unite` — an attribute not present in the parent
- Child overrides `afficher()` to display the unit of measure

---

## Project Context

KomTrack BF was conceived during the IT Project Management module (CS27) at BIT. The full project plan includes:

- A project charter with problem statement and stakeholder analysis
- A SMART goal and OKRs
- A scope statement (in-scope / out-of-scope features)
- A Work Breakdown Structure across 5 phases
- A budget estimated in FCFA using open-source technologies
- A risk register with 8 identified risks scored by likelihood × impact

The Python implementation in this repository is the coding realisation of that plan, following the same domain: inventory and sales management for small traders in Ouagadougou.

---

## Team

| Name | Role |
|---|---|
| TRAORE Esmelle | Project Manager |
| Zongo Abdel Sadeck | CTO / Technical Lead |
| TOE L. Kevin | Quality & Risk Officer |
| KANTIONO Diane | Finance Lead |
| KAFANDO Wend Denda Arsene Bienvenu | Business Analyst |

**Lecturer:** Mme Kweyakie Afi Blebo  
**Course:** CS27 — Advanced Programming with Python (OOP)  
**Institution:** Burkina Institute of Technology  
**Deadline:** Sunday 25th May 2026, end of day
