import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Remplacez ces informations par vos paramètres de connexion réels
hostname = 'localhost'
database = 'piscineds'
username = 'your_login'
password = 'mysecretpassword'
port_id = 5432

# Établir la connexion
conn = psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=password,
    port=port_id
)

# Exécuter la requête pour récupérer les données d'achat
query = """
SELECT event_time, price
FROM customers
WHERE event_type = 'purchase'
AND event_time BETWEEN '2022-10-01' AND '2023-02-28';
"""

# Récupérer les données dans un DataFrame pandas
df = pd.read_sql_query(query, conn)

# Fermer la connexion
conn.close()

# Grouper les données par mois et calculer le total des ventes pour chaque mois
df['month'] = df['event_time'].dt.to_period('M')
df_bar = df.groupby('month')['price'].sum()

# Créer le graphique en barres
plt.figure(figsize=(10, 6))
plt.bar(range(len(df_bar)), df_bar.values)
plt.title('Total des Ventes par Mois en Altairian Dollars')
plt.xlabel('Mois')
plt.ylabel('Total des Ventes ($)')
months = ['Oct', 'Nov', 'Jan']  # Liste des mois comme étiquettes
plt.xticks(ticks=range(len(months)), labels=months)  # Utiliser les mois comme étiquettes
plt.show()


# Créer le graphique en barres
plt.figure(figsize=(10, 6))
plt.bar(range(len(df_bar)), df_bar.values)
plt.title('Total des Ventes par Mois en Altairian Dollars')
plt.xlabel('Mois')
plt.ylabel('Total des Ventes ($)')
months = ['Oct', 'Nov', 'Jan']  # Liste des mois comme étiquettes
plt.xticks(ticks=range(len(months)), labels=months)  # Utiliser les mois comme étiquettes
plt.show()


# Exemple de graphique en aires (area chart)
plt.figure(figsize=(10, 6))
df_area = df.groupby(df['event_time'].dt.date)['price'].mean()
plt.fill_between(df_area.index, df_area.values, alpha=0.5)
plt.plot(df_area.index, df_area.values)
plt.title('Dépense Moyenne Journalière en Altairian Dollars')
plt.xlabel('Date')
plt.ylabel('Dépense Moyenne ($)')
plt.show()
