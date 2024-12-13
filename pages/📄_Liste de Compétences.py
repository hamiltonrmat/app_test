import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import openpyxl

lien = "https://filesender.renater.fr/download.php?token=009f30f6-dc95-4b89-9638-ca4bbbd994af&files_ids=43453410"
data = pd.read_excel("liste compétences pour manuel des joueurs.xlsx", sheet_name="données")

domaines = data.nomDomaine.unique()

st.header("Liste de compétences")
option = st.selectbox(
    "Sélectioner un domaine:",domaines, index=1)
comp_domaine = data[data['nomDomaine'] == option]
compet = list(comp_domaine.nomCompetence)

option = st.selectbox(
    "Sélectioner un domaine:",compet,  index=3)
st.write("Détails de la compétence:")
df = data[data['nomCompetence'] == option][['Responsable', 'nbXP', 'disponible', 'obligatoire']]
df
ds = data[data['nomCompetence'] == option]
st.write("Description de la compétence:")
list(ds.DescriptionCompetence)[0]
