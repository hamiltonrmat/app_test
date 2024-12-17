import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import openpyxl
import hmac


def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password():
    st.stop()

st.set_page_config(layout="wide")

col1, col2, col3 = st.columns(3)

with col1:
  st.header('')
with col2:
  st.title('SkillQuest Maths')
  
  st.image("media.png", width=300)
  
  st.sidebar.header("Bienvenue !")
  
  st.sidebar.write("Explorez les compétences mathématiques de SkillQuest et votre situation dans l'aventure")
  
  
  st.sidebar.page_link("https://maths.unilasalle.fr", label="HubMaths UniLaSalle", icon="🌎")
  st.sidebar.page_link("https://moodle-beauvais.unilasalle.fr/course/view.php?id=1434", label="Moodle UniLaSalle SkillQuest", icon="🖥️")
  
  
  st.page_link("🏠_Homepage.py", label="Home", icon="🏠")
  st.page_link("pages/Détail par compétence.py", label="Détail par compétence", icon="1️⃣")
  st.page_link("pages/Informations personnelles.py", label="Informations personnelles", icon="2️⃣")
  st.page_link("pages/Situation Générale.py", label="Situation Générale", icon="3️⃣")
  st.page_link("pages/Top 20.py", label="Top 20", icon="4️⃣")
  st.page_link("pages/📄_Liste de Compétences.py", label="Liste de compétences", icon="📄")
  st.page_link("pages/Arbre de compétences.py", label="Arbre de compétences", icon="🌳")
  st.page_link("https://maths.unilasalle.fr", label="Hub Maths UniLaSalle", icon="🖥️")
  st.page_link("https://moodle-beauvais.unilasalle.fr/course/view.php?id=1434", label="Moodle SkillQuest", icon="📚")

with col3:
  st.header('')








