import streamlit as st
import pandas as pd
import psycopg2

st.set_page_config(
    page_title="Fuel Price France Dashboard",
    layout="wide"
)

conn = psycopg2.connect(
    host="localhost",
    database="fuel_db",
    user="alphadiallo",
    password=""
)

query = """
SELECT *
FROM fuel_prices
"""

df = pd.read_sql(query, conn)
prix_cols = [
    "gazole_prix",
    "sp95_prix",
    "sp98_prix",
    "e10_prix",
    "e85_prix",
    "gplc_prix"
]

for col in prix_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Filtre Région
st.sidebar.header("Filtres")

liste_regions = sorted(df["region"].dropna().unique())

region_selectionnee = st.sidebar.selectbox(
    "Choisir une région",
    ["Toutes les régions"] + list(liste_regions)
)

if region_selectionnee != "Toutes les régions":
    df = df[df["region"] == region_selectionnee]

# Filtre Carburant
carburant_selectionne = st.sidebar.selectbox(
    "Choisir un carburant",
    [
        "gazole_prix",
        "sp95_prix",
        "sp98_prix",
        "e10_prix",
        "e85_prix",
        "gplc_prix"
    ]
)        

st.title("⛽ Fuel Price France Dashboard")

ville_moins_chere = (
    df.groupby("ville")[carburant_selectionne]
    .mean()
    .idxmin()
)

ville_plus_chere = (
    df.groupby("ville")[carburant_selectionne]
    .mean()
    .idxmax()
)

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.metric("Stations", len(df))

with col2:
    st.metric(
        "Prix moyen",
        f"{df[carburant_selectionne].mean():.2f} €"
    )

with col3:
    st.metric(
        "Prix minimum",
        f"{df[carburant_selectionne].min():.2f} €"
    )

with col4:
    st.metric(
        "Régions",
        df["region"].nunique()
    )

with col5:
    st.metric(
        "Ville la moins chère",
        ville_moins_chere
    )

with col6:
    st.metric(
        "Ville la plus chère",
        ville_plus_chere
    )

st.divider()

st.subheader("Prix moyens par carburant")

fuel_data = pd.DataFrame({
    "Carburant": [
        "Gazole",
        "SP95",
        "SP98",
        "E10",
        "E85",
        "GPLc"
    ],
    "Prix moyen": [
        df["gazole_prix"].mean(),
        df["sp95_prix"].mean(),
        df["sp98_prix"].mean(),
        df["e10_prix"].mean(),
        df["e85_prix"].mean(),
        df["gplc_prix"].mean()
    ]
})

st.bar_chart(
    fuel_data.set_index("Carburant")
)

st.divider()
st.divider()

st.subheader("🏆 Top 10 villes les plus chères")
villes = (
    df.groupby("ville")[carburant_selectionne]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(villes)

st.subheader("💰 Top 10 villes les moins chères")

villes_moins_cheres = (
    df.groupby("ville")[carburant_selectionne]
    .mean()
    .sort_values(ascending=True)
    .head(10)
)

st.bar_chart(villes_moins_cheres)

st.subheader("Aperçu des données")

st.dataframe(
    df[
        [
            "ville",
            "gazole_prix",
            "sp95_prix",
            "e10_prix"
        ]
    ]
    .fillna("Non disponible")
    .head(20)
)