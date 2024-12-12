import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import openpyxl


st.set_page_config(layout="wide")
st.title('SkillQuest Maths')

st.image("media.png", width=300)

st.sidebar.header("Bienvenue !")

st.sidebar.write("Explorez les compétences mathématiques de SkillQuest et votre situation dans l'aventure")


st.sidebar.page_link("https://maths.unilasalle.fr", label="HubMaths UniLaSalle", icon="🌎")
st.sidebar.page_link("https://moodle-beauvais.unilasalle.fr/course/view.php?id=1434", label="Moodle UniLaSalle SkillQuest", icon="🖥️")


st.page_link("🏠_Homepage.py", label="Home", icon="🏠")
st.page_link("pages/Informations personnelles.py", label="Informations personnelles", icon="2️⃣")
st.page_link("pages/1️⃣_Détail par compétence.py", label="Détail par compétence", icon="1️⃣")
st.page_link("pages/Situation Générale.py", label="Situation Générale", icon="3️⃣")
st.page_link("pages/📄_Liste de Compétences.py", label="Situation Générale", icon="📄")
st.page_link("https://maths.unilasalle.fr", label="Hub Maths UniLaSalle", icon="🖥️")
st.page_link("https://moodle-beauvais.unilasalle.fr/course/view.php?id=1434", label="Moodle SkillQuest", icon="📚")




