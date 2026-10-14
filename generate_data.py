import pandas as pd  # Pandas : pour construire et manipuler notre tableau de données
import numpy as np   # NumPy : pour générer des valeurs numériques aléatoires

# On fixe une graine aléatoire pour garantir la reproductibilité
np.random.seed(42)

n = 500  # Nombre de clients fictifs à générer

# Création du tableau de données (features)
data = pd.DataFrame({
    "age": np.random.randint(18, 70, n),  # Âge entre 18 et 69 ans
    "salaire": np.random.randint(1200, 8000, n),  # Salaire mensuel simulé
    "abonnement": np.random.choice(
        ["Basique", "Standard", "Premium"], n
    ),  # Type d'offre
    "anciennete": np.random.randint(0, 15, n),  # Ancienneté en années
    "consommation": np.random.randint(0, 100, n),  # Score d'utilisation du service sur 100
})

# Création de la target (colonne à prédire) : churn
# Un client est considéré à risque si :
# - sa consommation est inférieure à 30
# - son ancienneté est inférieure à 2 ans

data["churn"] = (
    (data["consommation"] < 30)
    & (data["anciennete"] < 2)
).astype(int)  # Conversion de True/False en 1/0

# Sauvegarde des données dans un fichier CSV
data.to_csv("churn_data.csv", index=False)

# Affichage des premières lignes pour vérifier les données
print(data.head())

# Affichage du taux de churn
print(f"Taux de churn : {data['churn'].mean():.1%}")