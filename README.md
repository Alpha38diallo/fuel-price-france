# ⛽ Fuel Price France Dashboard

## 📖 Description

Projet Data Engineering et Data Analytics permettant d'analyser les prix des carburants en France à l'aide d'un pipeline Python, d'une base de données PostgreSQL et d'un tableau de bord interactif Streamlit.

## 🚀 Technologies utilisées

- Python
- Pandas
- PostgreSQL
- Streamlit
- Git
- GitHub

## 📊 Fonctionnalités

- Collecte et traitement des données carburant
- Chargement automatique des données dans PostgreSQL
- Tableau de bord interactif Streamlit
- Filtre par région
- Filtre par carburant
- KPI dynamiques
- Prix moyen par carburant
- Top 10 villes les plus chères
- Top 10 villes les moins chères
- Ville la plus chère
- Ville la moins chère
- Aperçu des données

## 📈 Résultats

- 9 814 enregistrements analysés
- 13 régions couvertes
- Analyse interactive des prix des carburants en France

## 📷 Captures d'écran

### Vue générale du dashboard

Screenshots/dashboard-overview.png

### KPI et filtres

Screenshots/dashboard-kpi.png

### Analyse des villes

Screenshots/dashboard-analysis.png

## 🛠️ Installation

### Cloner le dépôt

```bash
git clone https://github.com/Alpha38diallo/fuel-price-france.git
cd fuel-price-france
```

### Créer l'environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

### Configurer les variables d'environnement

Créer un fichier `.env` :

```env
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=fuel_db
```

### Exécuter le pipeline

```bash
python3 fuel_pipeline.py
```

### Lancer le dashboard

```bash
streamlit run dashboard/app.py
```

## 📂 Structure du projet

```text
fuel-price-france/
├── dashboard/
│   └── app.py
├── data/
├── scripts/
├── Screenshots/
│   ├── dashboard-overview.png
│   ├── dashboard-kpi.png
│   └── dashboard-analysis.png
├── requirements.txt
├── fuel_pipeline.py
└── README.md
```

## 👨‍💻 Auteur

**Alpha Diallo**

- GitHub : https://github.com/Alpha38diallo