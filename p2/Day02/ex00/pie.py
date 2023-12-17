import psycopg2
import matplotlib.pyplot as plt

# Connexion à la base de données (remplacer avec vos propres identifiants)
conn = psycopg2.connect(
    host='localhost',
    dbname='piscineds',
    user='your_login',  # Remplacez par votre identifiant réel
    password='mysecretpassword',
    port=5432
)

try:
    # Création d'un curseur et exécution de la requête
    with conn.cursor() as cur:
        cur.execute("SELECT event_type, COUNT(*) FROM customers GROUP BY event_type")
        data = cur.fetchall()

    for i in range(len(data)):
        print(data[i][0], data[i][1])
    # Préparation des données pour le camembert
    labels = [row[0] for row in data]
    sizes = [row[1] for row in data]
    print(labels)
    print(sizes)
    # Création du camembert
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')  # Assure que le camembert est bien rond.

    # Affichage du camembert
    plt.show()

finally:
    # Fermeture de la connexion à la base de données
    conn.close()
