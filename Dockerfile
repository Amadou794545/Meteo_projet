# Image de base
FROM python:3.11.14

# Dossier de travail dans le container
WORKDIR /app

# Copier les fichiers
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Commande à exécuter au lancement
CMD ["python", "__main__.py"]
