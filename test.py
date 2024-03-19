import streamlit as st
import os
from Classes.CardObject import CardObj
from os import startfile
from streamlit_card import card
from pathlib import Path



st.write("hello")
i=0
k = 1

def start_capture():
    import os
    
    print(Path.cwd())
    print(Path.joinpath(Path.cwd(),'AnimeDownloads/Sampei (ITA)1.MP4'))
    startfile(Path.joinpath(Path.cwd(),'AnimeDownloads/Sampei (ITA)1.MP4'))
    print("START1")

    return "Avviato"
                  



hasClicked = card(
  title="CARD1",
  text="Some description",
  image="http://placekitten.com/200/300",
)

if st.button("Start Capturing", key=2):
    st.write(start_capture())

hasClicked2 = card(
  title="CARD2!",
  text="Some description",
  image="http://placekitten.com/200/300",
)

st.markdown("<style> button[kind = 'secondary']{display: block; margin-left: auto; margin-right: auto}</style>", unsafe_allow_html=True)

if st.button("Start Capturing2"):
    st.write(start_capture())



