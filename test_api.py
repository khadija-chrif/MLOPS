import requests

URL = "http://localhost:8000"

print("=== Début des tests de l'API ==-\n")

# 1. L'API est-elle en vie ?
try:
    response = requests.get(f"{URL}/health")
    print(f"GET /health -> {response.status_code} {response.json()}")
except requests.exceptions.ConnectionError:
    print("Erreur : Impossible de joindre le serveur. Vérifiez qu'il est bien démarré sur http://localhost:8000")
    exit(1)

# 2. Un client à faible consommation et faible ancienneté
client_1 = {
    "age": 35,
    "salaire": 2500,
    "abonnement": "Standard",
    "anciennete": 1,
    "consommation": 10
}
r1 = requests.post(f"{URL}/predict", json=client_1)
print(f"POST /predict (Client 1) -> {r1.status_code} {r1.json()}")

# 3. Un client fidèle : forte consommation, forte ancienneté
client_2 = {
    "age": 50,
    "salaire": 4000,
    "abonnement": "Premium",
    "anciennete": 10,
    "consommation": 80
}
r2 = requests.post(f"{URL}/predict", json=client_2)
print(f"POST /predict (Client 2) -> {r2.status_code} {r2.json()}")

# 4. Une erreur volontaire : l'âge est du texte
client_mauvais = {**client_1, "age": "abc"}
r3 = requests.post(f"{URL}/predict", json=client_mauvais)
print(f"POST /predict (age='abc') -> Statut {r3.status_code}")

try:
    error_message = r3.json()["detail"][0]["msg"]
    print(f"Message de validation : {error_message}")
except (KeyError, IndexError, TypeError):
    print(f"Réponse brute : {r3.text}")
