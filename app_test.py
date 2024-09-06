import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")


st.set_page_config(layout="wide")
st.title('SkillQuest Maths')

url = "https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=mathskillsq.drawio.html#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1JckKNze4ue0CTv6WzvzFtlcs34MNmWiI%26export%3Ddownload"
components.iframe(url, height=900)

