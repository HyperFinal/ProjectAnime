import streamlit as st
from streamlit_card import card
import animeworld as aw
import os
from Classes.CardObject import CardObj
from Classes.ButtonObject import ButtonObj
from startfile import startfile
from pathlib import Path
from PIL import Image



## FUNCTION USED BY DOWNLOAD API FUNCTIONS (ANIMEWORLD/SERVERS/SERVER.PY)
def getCounter():
    return st.session_state['counter']

## FUNCTION USED BY DOWNLOAD API FUNCTIONS (ANIMEWORLD/SERVERS/SERVER.PY)
def getArrayCards():
    cardCol1, cardCol2, cardCol3, cardCol4 = st._bottom.columns(4)
    cards = [cardCol1, cardCol2, cardCol3, cardCol4]
    return cards


if __name__ == "__main__":

    ## CREATION OF SESSION VARIABLES
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
    if "sliderA" not in st.session_state:
        st.session_state.sliderA = 0
    if "sliderDA" not in st.session_state:
        st.session_state.sliderDA = 0
    else: ## ELSE FOR SET THE SLIDER 'TO' WITH THE VALUE OF SLIDER 'FROM' ON EACH CHANGE
        if(st.session_state.sliderDA != 0):
            st.session_state.sliderA = st.session_state.sliderDA + 1
        if(st.session_state.sliderDA == 0):
            st.session_state.sliderA = 0
    if "counter" not in st.session_state:
        st.session_state['counter'] = 0

    im = Image.open("img/ShanksRoger.ico")
    st.set_page_config(layout="wide", page_icon=im, page_title='ProjectAnime') 


    
    ## SET BACKGROUND IMAGE
    background_image = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: url("https://images5.alphacoders.com/790/790571.jpg");
        background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
        background-repeat: no-repeat;
    }
    </style>
    """
    st.markdown(background_image, unsafe_allow_html=True)

    ## CREATION OF WIDGETS WHERE THE CARDS WILL BE DISPLAYED
    cardCol1, cardCol2, cardCol3, cardCol4 = st._bottom.columns(4)
    cards = [cardCol1, cardCol2, cardCol3, cardCol4]

    ## FUCNTION MAIN
    def main():
        
        ArrayButtons = st.session_state['arrayB']
        ##  COLOR CURSOR SLIDER FROM - TO
        st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{
        background-color: rgb(0,0,0); box-shadow: rgb(14 38 74 / 20%) 0px 0px 0px 0.2rem;} </style>''', unsafe_allow_html = True)
        
        ##  COLOR VALUE SLIDER DISPLAYER (THE NUMBER ON TOP OF THE CURSOR)
        st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div > div
        { color: rgb(14, 38, 74); font-size: 15px; } </style>''', unsafe_allow_html = True)

        ##  COLOR SLIDER BAR
        
        
        print(ArrayButtons)

        ## HEADER
        with st.container():
            st.title("ProjectAnime")
            st.write("Benvenuto, Inserisci il titolo di un anime e gli episodi che vuoi scaricare")

        ## FORM FOR GET ANIME NAME AND WHICH EPISODES DOWNLOAD
        st.markdown("<style> button[kind = 'secondary']{display: block; margin-left: auto; margin-right: auto}</style>", unsafe_allow_html=True)
        ##st.markdown('<p style ="color: black; font-size: 30px; font-weight: bold; font-family: sans serif;"> Title: </p>', unsafe_allow_html=True)
        col1 = st.container()
        with col1:
                name = st.text_input(
                    'Title:',
                    placeholder="Inserisci titolo...",
                )
                st.session_state['name'] = name
                EpSlider(col1)
        button = st.button("Invia", type="primary")
        if button: 
            getAnimeInfo(cardCol1, cardCol2, cardCol3, cardCol4, ArrayButtons)

        ## CARDS DISPLAYING
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


    ## FUNCTION EPISODES DOWNLOAD
    
    def getEp(start: int,end: int,_anime,image,_cardCol1, _cardCol2, _cardCol3, _cardcol4, _arrayB: list):
        if(start > end):
            print('finish')
            st.rerun()
        episodes = _anime.getEpisodes([start]) 
        for ep in episodes:
            i = st.session_state['i']
            if(i < 4):
                print(fr"entrato if i: {i}")
            else:
                st.session_state['i'] = 0
                st.session_state['counter'] = 0
                st.session_state[f'{i}'] = CardObj(_anime.getName(), "Ep." + str(start), image)
                print(fr"entrato else i: {i}")
            print(i)
            print(f"Downloading episode {ep.number}.")
            name_file = fr"{_anime.getName()}{start}"
            ep.download(name_file, "AnimeDownloads")
            print(f"Download completed.")
            st.session_state['counter'] += 1
            print("GET EP COUNTER " + str(st.session_state['counter']))
            path = fr"AnimeDownloads/{_anime.getName()}{start}.mp4"
            text = fr"Play {_anime.getName()} Ep.{start}"
            nameF = fr"{_anime.getName()}{start}"
            Button = ButtonObj(text, path, nameF)
            _arrayB.insert(i, Button)
            st.session_state['arrayB'] = _arrayB
            print("INSERITO IN ARRAY B")
            if f'{i}' not in st.session_state:
                st.session_state[f'{i}'] = CardObj(_anime.getName(), "Ep." + str(start), image)
                print("ENTRATO IF NOT")
                print(f'{i}')
                print(st.session_state[f'{i}'])
            else:
                st.session_state[f'{i}'] = CardObj(_anime.getName(), "Ep." + str(start), image)
                print("ENTRATO ELSE NOT")
                print(f'{i}')
                print(st.session_state[f'{i}']) 
            if(i == 0):
                _cardCol1.empty()
                with _cardCol1.container():
                    st.session_state[f'{i}'].display()
                    if f'B{i}' not in st.session_state:
                        st.session_state[f'B{i}'] = _arrayB[i]
                        textB = st.session_state[f'B{i}'].getText()
                        print(textB)
                        if st.button(fr'{textB}'):
                            st.write(startFunc(st.session_state[f'B{i}'].getPath(), st.session_state[f'B{i}'].getName()))
                        else:
                            st.write(startFunc(st.session_state[f'B{i}'].getPath(), st.session_state[f'B{i}'].getName()))
                        
                        print("ENTRATO IF1 NOT BUTTON")
                        print(path)
                    else:
                        st.session_state[f'B{i}'] = _arrayB[i]
                        textB = st.session_state[f'B{i}'].getText()
                        print(textB)
                        if st.button(fr'{textB}'):
                            st.write(startFunc(st.session_state[f'B{i}'].getPath(), st.session_state[f'B{i}'].getName()))
                        print("ENTRATO ELSE1 BUTTON")
                        print(path)
            if(i == 1):
                _cardCol2.empty()
                with _cardCol2.container():
                    st.session_state[f'{i}'].display()
                    if f'B{i}' not in st.session_state:
                        st.session_state[f'B{i}'] = _arrayB[i]
                        textB = st.session_state[f'B{i}'].getText()
                        print(textB)
                        if st.button(fr'{textB}'):
                            st.write(startFunc(st.session_state[f'B{i}'].getPath(), st.session_state[f'B{i}'].getName()))
                        print("ENTRATO IF2 NOT BUTTON")
                        print(path)
                    else:
                        st.session_state[f'B{i}'] = _arrayB[i]
                        textB = st.session_state[f'B{i}'].getText()
                        print(textB)
                        if st.button(fr'{textB}'):
                            st.write(startFunc(st.session_state[f'B{i}'].getPath(), st.session_state[f'B{i}'].getName()))
                        print("ENTRATO ELSE2 BUTTON")
                        print(path)
            if(i == 2):
                _cardCol3.empty()
                with _cardCol3.container():
                    st.session_state[f'{i}'].display()
                    if f'B{i}' not in st.session_state:
                        print(_arrayB)
                        st.session_state[f'B{i}'] = _arrayB[i]
                        textB = st.session_state[f'B{i}'].getText()
                        print(textB)
                        if st.button(fr'{textB}'):
                            st.write(startFunc(st.session_state[f'B{i}'].getPath(), st.session_state[f'B{i}'].getName()))
                        print("ENTRATO IF3 NOT BUTTON")
                        print(path)
                    else:
                        st.session_state[f'B{i}'] = _arrayB[i]
                        textB = st.session_state[f'B{i}'].getText()
                        print(textB)
                        if st.button(fr'{textB}'):
                            st.write(startFunc(st.session_state[f'B{i}'].getPath(), st.session_state[f'B{i}'].getName()))
                        print(path)
            if(i == 3):
                _cardcol4.empty()
                with _cardcol4.container():
                    st.session_state[f'{i}'].display()
                    if f'B{i}' not in st.session_state:
                        st.session_state[f'B{i}'] = _arrayB[i]
                        textB = st.session_state[f'B{i}'].getText()
                        print(textB)
                        if st.button(fr'{textB}'):
                            st.write(startFunc(st.session_state[f'B{i}'].getPath(), st.session_state[f'B{i}'].getName()))
                        print(path)
                    else:
                        st.session_state[f'B{i}'] = _arrayB[i]
                        textB = st.session_state[f'B{i}'].getText()
                        print(textB)
                        if st.button(fr'{textB}'):
                            st.write(startFunc(st.session_state[f'B{i}'].getPath(), st.session_state[f'B{i}'].getName()))
                        print(path)
            st.session_state['i'] = st.session_state['i'] + 1
            start = start + 1
            return (getEp(start,end,_anime,image, _cardCol1, _cardCol2, _cardCol3, _cardcol4, _arrayB))
        
    ## FUNCTION TO GET INFO ABOUT THE ANIME LIKE LINK, IMAGE ETC
    def getAnimeInfo(cardCol1, cardCol2, cardCol3, cardcol4, arrayB):
        anime_info = aw.find(st.session_state['name'])
        if(anime_info == []):
            st.write("Anime con quel nome non esistente")
            return
        print(anime_info)
        Anime = aw.Anime(anime_info[0]['link'])
        directory = "C:/ProjectAnimeDownloads"
        if not os.path.exists(directory):
            os.makedirs(directory)
            print("Directory created successfully!")
        else:
            print("Directory already exists!")   
        getEp(int(st.session_state['start']), int(st.session_state['end']), Anime, anime_info[0]['image'],cardCol1, cardCol2, cardCol3, cardcol4, arrayB)



    ## FUNCTION FOR CREATE SLIDERS FOR EPISODE SELECTION
    def EpSlider(col1):
        if(st.session_state['name'] != 'value' and st.session_state['name'] != ''):
            print('Valore di name e' + st.session_state['name'])   
            anime_info = aw.find(st.session_state['name'])
            if(anime_info == []):
                st.write("Anime con quel nome non esistente")
                return
            max_episodes = anime_info[0]['episodes']
            
            with col1.container():
                st.slider('DA',0,max_episodes, step=1, key='sliderDA', on_change=setStart())
            with col1.container():
                st.slider('A', 0,max_episodes, step=1,key='sliderA', on_change=setEnd())
                
        else:
            print('ELSE valore di name e value')
        return

    ## FUNCTION THAT BUTTONS CALLS TO START ANIME MP4
    def startFunc(path, name):
        print("PATH BUTTON INSIDE START METHOD:" + path)
        startfile(Path.joinpath(Path.cwd(), path))
        ##print("AVVIATO FILE " + path)
        return fr'Avviato file {name}'

    ## FUNCTION THAT SET THE EPISODE FROM WHERE START TO DOWNLOAD (RETRIVE FROM THE SLIDER)
    def setStart():
        
        st.session_state['start'] = st.session_state.sliderDA
        print("START: " + str(st.session_state['start']))
        return

    ## FUNCTION THAT SET THE EPISODE FROM WHERE END TO DOWNLOAD (RETRIVE FROM THE SLIDER)
    def setEnd():
        st.session_state['end'] = st.session_state.sliderA
        ##print("END: " + str(st.session_state['end']))
        return
    
    

    


        
    main()