import streamlit as st
from streamlit_card import card
import animeworld as aw
import os
from Classes.CardObject import CardObj
from Classes.ButtonObject import ButtonObj
from startfile import startfile
from pathlib import Path
st.set_page_config(page_title="ProjectAnime", layout="wide")


if 'name' not in st.session_state:
    st.session_state['name'] = 'value'
if 'start' not in st.session_state:
    st.session_state['start'] = 'value'
if 'end' not in st.session_state:
    st.session_state['end'] = 'value'
if 'i' not in st.session_state:
    st.session_state['i'] = 0
if 'arrayB' not in st.session_state:
    st.session_state['arrayB'] = []



def main():
    ArrayButtons = st.session_state['arrayB']
    print(ArrayButtons)
    ##HEADER
    with st.container():
        st.title("ProjectAnime")
        st.write("Benvenuto, Inserisci il titolo di un anime e gli episodi che vuoi scaricare")

    ##FORM
    st.markdown("<style> button[kind = 'secondary']{display: block; margin-left: auto; margin-right: auto}</style>", unsafe_allow_html=True)
    cardCol1, cardCol2, cardCol3, cardCol4 = st._bottom.columns(4)
    col1, col2, col3 = st.columns((1,0.1,0.1))
    with col1:
            name = st.text_input(
                "Title",
            )
            st.session_state['name'] = name
    with col2:
            start = st.text_input(
                "Da",
            )
            st.session_state['start'] = start
    with col3:
            end= st.text_input(
                "A",
            )
            st.session_state['end'] = end
    button = st.button("Invia", type="primary")
    if button: 
        getAnimeInfo(cardCol1, cardCol2, cardCol3, cardCol4, ArrayButtons)

    print()
    cardCol1.empty()
    cardCol2.empty()
    cardCol3.empty()
    cardCol4.empty()
    with cardCol1:
        if '0' in  st.session_state:
            st.session_state['0'].display()
        if 'B0' in st.session_state:
            text = st.session_state['B0'].getText()
            print(text)
            if st.button(fr'{text}'):
                st.write(startFunc(st.session_state['B0'].getPath(), st.session_state['B0'].getName()))
    with cardCol2:
        if '1' in  st.session_state:
            st.session_state['1'].display()
        if 'B1' in st.session_state:
            text = st.session_state['B1'].getText()
            print(text)
            if st.button(fr'{text}'):
                st.write(startFunc(st.session_state['B1'].getPath(), st.session_state['B1'].getName()))
    with cardCol3:
        if '2' in  st.session_state:
            st.session_state['2'].display()
        if 'B2' in st.session_state:
            text = st.session_state['B2'].getText()
            print(text)
            if st.button(fr'{text}'):
                st.write(startFunc(st.session_state['B2'].getPath(), st.session_state['B2'].getName()))
    with cardCol4:
        if '3' in  st.session_state:
            st.session_state['3'].display()
        if 'B3' in st.session_state:
            text = st.session_state['B3'].getText()
            print(text)
            if st.button(fr'{text}'):
                st.write(startFunc(st.session_state['B3'].getPath(), st.session_state['B3'].getName()))
    if st.button("Refresh"):
            st.write(st.rerun())
    
    

def getEp(start: int,end: int,anime:aw.Anime,image,cardCol1, cardCol2, cardCol3, cardcol4, arrayB: list):
    if(start > end):
        print('finish')
        st.rerun()
    episodes = anime.getEpisodes([start])
    i = st.session_state['i']
    for ep in episodes:
        if(i < 4):
            print(fr"entrato if i: {i}")
        else:
            i = 0
            st.session_state[f'{i}'] = CardObj(anime.getName(), "Ep." + str(start), image, path)
            print(fr"entrato else i: {i}")
        print(i)
        print(f"Downloading episode {ep.number}.")
        name_file = fr"{anime.getName()}{start}"
        ep.download(name_file, "AnimeDownloads") 
        print(f"Download completed.")
        path = fr"AnimeDownloads/{anime.getName()}{start}.mp4"
        text = fr"Play {anime.getName()} Ep.{start}"
        nameF = fr"{anime.getName()}{start}"
        Button = ButtonObj(text, path, nameF)
        arrayB.insert(i, Button)
        st.session_state['arrayB'] = arrayB
        print("INSERITO IN ARRAY B")
        if f'{i}' not in st.session_state:
            st.session_state[f'{i}'] = CardObj(anime.getName(), "Ep." + str(start), image, path)
            print("ENTRATO IF NOT")
            print(f'{i}')
            print(st.session_state[f'{i}'])
        else:
            st.session_state[f'{i}'] = CardObj(anime.getName(), "Ep." + str(start), image, path)
            print("ENTRATO ELSE NOT")
            print(f'{i}')
            print(st.session_state[f'{i}']) 
        if(i == 0):
            cardCol1.empty()
            with cardCol1.container():
                st.session_state[f'{i}'].display()
                if f'B{i}' not in st.session_state:
                    st.session_state[f'B{i}'] = arrayB[i]
                    textB = st.session_state[f'B{i}'].getText()
                    print(textB)
                    if st.button(fr'{textB}'):
                        st.write(startFunc(st.session_state[f'B{i}'].getPath(), st.session_state[f'B{i}'].getName()))
                    print("ENTRATO IF1 NOT BUTTON")
                    print(path)
                else:
                    st.session_state[f'B{i}'] = arrayB[i]
                    textB = st.session_state[f'B{i}'].getText()
                    print(textB)
                    if st.button(fr'{textB}'):
                        st.write(startFunc(st.session_state[f'B{i}'].getPath(), st.session_state[f'B{i}'].getName()))
                    print("ENTRATO ELSE1 BUTTON")
                    print(path)
        if(i == 1):
            cardCol2.empty()
            with cardCol2.container():
                st.session_state[f'{i}'].display()
                if f'B{i}' not in st.session_state:
                    st.session_state[f'B{i}'] = arrayB[i]
                    textB = st.session_state[f'B{i}'].getText()
                    print(textB)
                    if st.button(fr'{textB}'):
                        st.write(startFunc(st.session_state[f'B{i}'].getPath(), st.session_state[f'B{i}'].getName()))
                    print("ENTRATO IF2 NOT BUTTON")
                    print(path)
                else:
                    st.session_state[f'B{i}'] = arrayB[i]
                    textB = st.session_state[f'B{i}'].getText()
                    print(textB)
                    if st.button(fr'{textB}'):
                        st.write(startFunc(st.session_state[f'B{i}'].getPath(), st.session_state[f'B{i}'].getName()))
                    print("ENTRATO ELSE2 BUTTON")
                    print(path)
        if(i == 2):
            cardCol3.empty()
            with cardCol3.container():
                st.session_state[f'{i}'].display()
                if f'B{i}' not in st.session_state:
                    print(arrayB)
                    st.session_state[f'B{i}'] = arrayB[i]
                    textB = st.session_state[f'B{i}'].getText()
                    print(textB)
                    if st.button(fr'{textB}'):
                        st.write(startFunc(st.session_state[f'B{i}'].getPath(), st.session_state[f'B{i}'].getName()))
                    print("ENTRATO IF3 NOT BUTTON")
                    print(path)
                else:
                    st.session_state[f'B{i}'] = arrayB[i]
                    textB = st.session_state[f'B{i}'].getText()
                    print(textB)
                    if st.button(fr'{textB}'):
                        st.write(startFunc(st.session_state[f'B{i}'].getPath(), st.session_state[f'B{i}'].getName()))
                    print(path)
        if(i == 3):
            cardcol4.empty()
            with cardcol4.container():
                st.session_state[f'{i}'].display()
                if f'B{i}' not in st.session_state:
                    st.session_state[f'B{i}'] = arrayB[i]
                    textB = st.session_state[f'B{i}'].getText()
                    print(textB)
                    if st.button(fr'{textB}'):
                        st.write(startFunc(st.session_state[f'B{i}'].getPath(), st.session_state[f'B{i}'].getName()))
                    print(path)
                else:
                    st.session_state[f'B{i}'] = arrayB[i]
                    textB = st.session_state[f'B{i}'].getText()
                    print(textB)
                    if st.button(fr'{textB}'):
                        st.write(startFunc(st.session_state[f'B{i}'].getPath(), st.session_state[f'B{i}'].getName()))
                    print(path)
        st.session_state['i'] = st.session_state['i'] + 1
        start = start + 1
        return (getEp(start,end,anime,image, cardCol1, cardCol2, cardCol3, cardcol4, arrayB))
    
def getAnimeInfo(cardCol1, cardCol2, cardCol3, cardcol4, arrayB):
    anime_info = aw.find(st.session_state['name'])
    if(anime_info == []):
        st.write("Anime con quel nome non esistente")
        return
    Anime = aw.Anime(anime_info[0]['link'])
    directory = "C:/ProjectAnimeDownloads"
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Directory created successfully!")
    else:
        print("Directory already exists!")   
    getEp(int(st.session_state['start']), int(st.session_state['end']), Anime, anime_info[0]['image'],cardCol1, cardCol2, cardCol3, cardcol4, arrayB)



def startFunc(path, name):
    print("PATH BUTTON INSIDE START METHOD:" + path)
    startfile(Path.joinpath(Path.cwd(), path))
    print("AVVIATO FILE " + path)
    return fr'Avviato file {name}'

main()