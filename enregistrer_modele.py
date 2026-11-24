# ===== 1. Importer les bibliothèques =====
import mlflow
import mlflow.sklearn
import pandas as pd
from mlflow import MlflowClient
from sklearn.ensemble import RandomForestClassifier

# ===== 2. Se connecter au serveur MLflow lancé par Docker Compose =====
TRACKING_URI = "http://localhost:5000"
EXPERIMENT_NAME = "churn-docker"
MODEL_NAME = "churn-model"

mlflow.set_tracking_uri(TRACKING_URI)
mlflow.set_experiment(EXPERIMENT_NAME)

# ===== 3. Lire et préparer les données =====
df = pd.read_csv("churn_data.csv")

# Transformer la colonne catégorielle "abonnement" en variables indicatrices (0/1)
X = pd.get_dummies(df.drop(columns=["churn"]), columns=["abonnement"])
y = df["churn"]

# ===== 4. Entraîner le modèle =====
modele = RandomForestClassifier(n_estimators=100, random_state=42)
modele.fit(X, y)

# ===== 5. Enregistrer le modèle dans le Registry du serveur =====
with mlflow.start_run():
    model_info = mlflow.sklearn.log_model(
        sk_model=modele,
        artifact_path="model",
        registered_model_name=MODEL_NAME,
        serialization_format="cloudpickle",
    )

# ===== 6. Poser l'alias "champion" sur la version créée =====
client = MlflowClient()
versions = client.search_model_versions(f"name='{MODEL_NAME}'")
latest_version = max(int(v.version) for v in versions)

client.set_registered_model_alias(
    name=MODEL_NAME,
    alias="champion",
    version=str(latest_version),
)

print(f"Version {latest_version} de '{MODEL_NAME}' enregistrée avec l'alias 'champion'.")