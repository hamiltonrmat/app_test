import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import openpyxl


st.set_page_config(layout="wide")
st.title('SkillQuest Maths')

st.sidebar.page_link("https://maths.unilasalle.fr", label="HubMaths UniLaSalle", icon="🌎")
st.sidebar.write("Explorez l'arbre de compétences mathématiques UniLaSalle")

url = "https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=mathskillsq.drawio.html#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1JckKNze4ue0CTv6WzvzFtlcs34MNmWiI%26export%3Ddownload"
components.iframe(url, height=900)

lien = "https://filesender.renater.fr/download.php?token=009f30f6-dc95-4b89-9638-ca4bbbd994af&files_ids=43453410"
data = pd.read_excel("liste compétences pour manuel des joueurs.xlsx", sheet_name="données")

domaines = data.nomDomaine.unique()

st.header("Liste de compétences")
option = st.selectbox(
    "Sélectioner un domaine:",domaines)
comp_domaine = data[data['nomDomaine'] == option]
compet = list(comp_domaine.nomCompetence)

option = st.selectbox(
    "Sélectioner un domaine:",compet)
st.write("Détails de la compétence:")
df = data[data['nomCompetence'] == option][['Responsable', 'nbXP', 'disponible', 'obligatoire']]
df
ds = data[data['nomCompetence'] == option]
st.write("Description de la compétence:")
list(ds.DescriptionCompetence)[0]




