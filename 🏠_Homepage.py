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



url = "https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=mathskillsq.drawio.html#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1JckKNze4ue0CTv6WzvzFtlcs34MNmWiI%26export%3Ddownload"
components.iframe(url, height=900)




