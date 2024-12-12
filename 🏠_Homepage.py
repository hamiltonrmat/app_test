import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import openpyxl


st.set_page_config(layout="wide")
st.title('SkillQuest Maths')

st.sidebar.header("Bienvenue !")

st.sidebar.write("Explorez l'arbre de compétences mathématiques UniLaSalle")


st.sidebar.page_link("https://maths.unilasalle.fr", label="HubMaths UniLaSalle", icon="🌎")
st.sidebar.page_link("https://moodle-beauvais.unilasalle.fr/course/view.php?id=1434", label="Moodle UniLaSalle SkillQuest", icon="🖥️")


st.page_link("Home.py", label="Home", icon="🏠")
st.page_link("pages/Informations personnelles.py", label="Informations personnelles", icon="1️⃣")
st.page_link("pages/Détail par compétence.py", label="Détail par compétence", icon="2️⃣")
st.page_link("pages/Situation Générale.py", label="Situation Générale", icon="3️⃣")
st.page_link("https://maths.unilasalle.fr", label="Hub Maths UniLaSalle", icon="🖥️")
st.page_link("https://moodle-beauvais.unilasalle.fr/course/view.php?id=1434", label="Moodle SkillQuest", icon="📚")




