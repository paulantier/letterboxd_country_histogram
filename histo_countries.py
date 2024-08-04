import matplotlib.pyplot as plt
import csv
from collections import Counter
import ast

# Remplace 'fichier.csv' par le nom de ton fichier CSV
filename = 'countries_of_origin.csv'
country_counter = Counter()

# Lire les données du fichier CSV et traiter chaque ligne
with open(filename, mode='r', newline='') as file:
    reader = csv.reader(file)
    for i,row in enumerate(reader):
        if i>0:
            # Convertir la ligne en une chaîne (le CSV semble contenir des listes comme des chaînes)
            line = row[0]

            # Supprimer les crochets et les guillemets pour extraire les pays
            line = line.replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
            countries = line.split(",")  # Séparer les pays par virgule

            # Ajouter chaque pays au compteur
            for country in countries:
                country_counter[country.strip()] += 1

# Trier les pays par ordre croissant d'occurrences
sorted_countries = sorted(country_counter.items(), key=lambda x: x[1])

# Extraire les labels (pays) et les valeurs (nombre d'occurrences)
labels, values = zip(*sorted_countries)

# Créer l'histogramme avec des barres horizontales
plt.barh(labels, values)
plt.xlabel('Nombre d\'occurrences')
plt.ylabel('Pays')
plt.title('Nombre d\'occurrences de chaque pays (trié par ordre croissant)')
#plt.xscale('log')
plt.show()