import streamlit as st
from streamlit_card import card
import animeworld as aw
import os
from Classes.CardObject import CardObj
from Classes.ButtonObject import ButtonObj
from startfile import startfile
from pathlib import Path
from PIL import Image
import re as rgx




## FUNCTION USED BY DOWNLOAD API FUNCTIONS (ANIMEWORLD/SERVERS/SERVER.PY)
def getCounter():
    return st.session_state['counter']

## FUNCTION USED BY DOWNLOAD API FUNCTIONS (ANIMEWORLD/SERVERS/SERVER.PY)
def getArrayCards():
    cardCol1, cardCol2, cardCol3, cardCol4 = st._bottom.columns(4)
    cards = [cardCol1, cardCol2, cardCol3, cardCol4]
    return cards


## FUNCTION TO CREATE LAST SEEN ANIME FOR FAST SEARCH
EpDict = {}
def preferCreate():
    path = os.getcwd()
    path_anime = os.path.join(path, "AnimeDownloads")
    if not os.path.exists(path_anime):
        print("DOWNLOADS DIRECTORY NOT EXIST CANNOT GET LAST ANIME DOWNLOADS")
    else:
        print(path)
        files = os.listdir(path_anime)
        arrayTitle = []
        temp_ep = 0
        regex = r'(\d+|\D+)'
        for anime in files:
            if '.mp4' in anime:
                print(anime)
                info = rgx.split(regex, anime)
                info = [x for x in info if x] 
                print("NOME ANIME PREFER: " + info[0])
                if(info[0] in EpDict.keys()):
                    temp_ep = info[1]
                    if(EpDict[info[0]] < temp_ep):
                        EpDict[info[0]] = temp_ep
                else:
                    EpDict[info[0]] = info[1]
                title = info[0]
                if title not in arrayTitle:
                    arrayTitle.append(title)
                print(arrayTitle)
        print ("Files: " + str(files))
        return arrayTitle
    


if __name__ == "__main__":

    ## CREATION OF SESSION VARIABLES
    if 'name' not in st.session_state:
        st.session_state['name'] = 'value'
    if 'last_view' not in st.session_state:
        st.session_state['last_view'] = 'value'
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
    if "sliderA2" not in st.session_state:
        st.session_state.sliderA2 = 0
    if "sliderDA2" not in st.session_state:
        st.session_state.sliderDA2 = 0  
    else: ## ELSE FOR SET THE SLIDER 'TO' WITH THE VALUE OF SLIDER 'FROM' ON EACH CHANGE
        if(st.session_state.sliderDA != 0):
            if(st.session_state.sliderA < st.session_state.sliderDA):
                if(st.session_state.sliderDA < st.session_state.maxEp):
                    st.session_state.sliderA = st.session_state.sliderDA + 3
                else:
                    st.session_state.sliderA = st.session_state.sliderDA
        if(st.session_state.sliderDA == 0):
            st.session_state.sliderA = 0
    if "counter" not in st.session_state:
        st.session_state['counter'] = 0
    if "name_input" not in st.session_state:
        st.session_state.name_input = ""
    if "disable" not in st.session_state:
        st.session_state.disable = False

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
    if 'checkSelect' not in st.session_state:
        st.session_state.checkSelect = False
    ## FUCNTION MAIN
    def main():
        ArrayButtons = st.session_state['arrayB']
        ##  COLOR CURSOR SLIDER FROM - TO
        st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{
        background-color: rgb(0,0,0); box-shadow: rgb(14 38 74 / 20%) 0px 0px 0px 0.2rem;} </style>''', unsafe_allow_html = True)
        
        ##  COLOR VALUE SLIDER DISPLAYER (THE NUMBER ON TOP OF THE CURSOR)
        st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div > div
        { color: rgb(14, 38, 74); font-size: 15px; } </style>''', unsafe_allow_html = True)


        print(ArrayButtons)

        ## HEADER
        
        with st.container():
            st.title("ProjectAnime")
            st.write("Benvenuto, Inserisci il titolo di un anime e gli episodi che vuoi scaricare")
        header = st.columns((0.4,1,0.4,1))
        
        with header[0]:
            st.session_state['last_view'] = CreateSelect()
            if(st.session_state['last_view'] == []):
                st.session_state.checkSelect = False
        with header[1]:
            st.text("")
            st.text("")
            st.session_state.startFirst = st.checkbox('Avviare la prima puntata al termine del download')
        SendCol = st.columns((0.1,1,0.1,1))
        with SendCol[0]:
            st.button("Invia")
        ## FORM FOR GET ANIME NAME AND WHICH EPISODES DOWNLOAD
        st.markdown("<style> button[kind = 'secondary']{display: block; margin-left: auto; margin-right: auto}</style>", unsafe_allow_html=True)
        ##st.markdown('<p style ="color: black; font-size: 30px; font-weight: bold; font-family: sans serif;"> Title: </p>', unsafe_allow_html=True)
        col1 = st.container()
        st.session_state.col = col1
        with col1:
                st.session_state.name_input = st.text_input(
                    'Title:',
                    placeholder="Inserisci titolo se non hai selezionato un'anime tra gli ultimi visti...",
                )
                if(st.session_state.name_input != st.session_state['name'] and st.session_state['name'] != 'value' and st.session_state.name_input != ''):
                    print('NAME UGUALE A ' + str(st.session_state.name_input))
                    st.session_state.checkSelect = False
                if(st.session_state.checkSelect == False):
                    st.session_state['name'] = st.session_state.name_input
                    st.session_state.disable = True
                    print("CCCCCCCCCCCCCCCCCCCCCCCCC " + st.session_state.name_input)
                    EpSlider1(col1)
                else:
                    st.session_state.disable = False
                    if(st.session_state['name'] != 'value'):
                        last_ep = EpDict[st.session_state['name']]
                        EpSlider2(col1, last_ep)
        button = st.button("Download", type='primary')
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
                    print("entrato primo button clicked")
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
        print("Start" + str(start))
        print("END" + str(end))
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
                        print("ENTRATO IF1 NOT BUTTON")
                        print(path)
                        print("VALORE CHECKBOX FIRST DOWNLOAD: " + str(st.session_state.startFirst))
                        if(st.session_state.startFirst == True):
                            startFunc(st.session_state['B0'].getPath(), st.session_state['B0'].getName())
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
        print('test')
        anime_info = aw.find(st.session_state['name'])
        if(anime_info == []):
            st.write("Anime con quel nome non esistente")
            return
        print(anime_info)
        Anime = aw.Anime(anime_info[0]['link'])
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        current_path = os.getcwd()
        path_dir = os.path.join(current_path, "AnimeDownloads")
        if not os.path.exists(path_dir):
            os.makedirs(path_dir)
            print("Directory created successfully!")
        else:
            print("Directory already exists!")   
        getEp(int(st.session_state['start']), int(st.session_state['end']), Anime, anime_info[0]['image'],cardCol1, cardCol2, cardCol3, cardcol4, arrayB)



    ## FUNCTION FOR CREATE SLIDERS FOR EPISODE SELECTION
    def EpSlider1(col1):
        print('ENTRATO EP SLIDER 1')
        if(st.session_state['name'] != 'value' and st.session_state['name'] != ''):
            print('Valore di name e ' + str(st.session_state['name']))   
            anime_info = aw.find(st.session_state['name'])
            print('FUNZIONE ANIMEWORLD RITORNO: ' + str(anime_info))
            if(anime_info == []):
                st.write("Anime con quel nome non esistente")
                return
            print("EPISODI MASSIMI ANIME: " + str(anime_info[0]['episodes']))
            max_episodes = anime_info[0]['episodes']
            max_episodes = int(max_episodes)
            if "maxEp" not in st.session_state:
                st.session_state.maxEp = max_episodes
            print("EPISODI MASSIMI APP.PY " + str(anime_info[0]['episodes']))
            with col1.container():
                st.slider('DA', 0, max_episodes, None, 1, None, 'sliderDA', None, on_change= setStart())
            with col1.container():
                st.slider('A', 0, max_episodes, step=1, key='sliderA', on_change=setEnd())
        else:
            print('ELSE valore di name e value')
        return
    
    def EpSlider2(col1, last_ep):
        print('ENTRATO EP SLIDER 2')
        if(st.session_state['name'] != 'value' and st.session_state['name'] != ''):
            print('Valore di name e ' + str(st.session_state['name']))   
            anime_info = aw.find(st.session_state['name'])
            print('FUNZIONE ANIMEWORLD RITORNO: ' + str(anime_info))
            if(anime_info == []):
                st.write("Anime con quel nome non esistente")
                return
            print("EPISODI MASSIMI ANIME: " + str(anime_info[0]['episodes']))
            max_episodes = anime_info[0]['episodes']
            max_episodes = int(max_episodes)
            if "maxEp" not in st.session_state:
                st.session_state.maxEp = max_episodes
            print("EPISODI MASSIMI APP.PY " + str(anime_info[0]['episodes']))
            with col1.container():
                print("LAST EP UGUALE A " + str(last_ep))
                ep = int(last_ep)
                st.slider(label='DA', min_value=0, value= ep, max_value=max_episodes, step=1,format=None, key = 'sliderDA2', on_change=setStart2())
                ##print("VALORE SLIDER DA " + str(sliderDA))
            with col1.container():
                print('CREATION SLIDER A EPSL2')
                st.slider(label='A', min_value=0, value= ep+3, max_value=max_episodes, step=1,format=None, key = 'sliderA2', on_change=setEnd2())
        else:
            print('ELSE valore di name e value')
        return
        

    ## FUNCTION THAT BUTTONS CALLS TO START ANIME MP4 
    def startFunc(path, name):
        print("PATH BUTTON INSIDE START METHOD:" + path)
        path = Path.joinpath(Path.cwd(), path)
        startfile(path)
        print("AVVIATO FILE " + str(path))
        return fr'Avviato file {name}'
   

    ## FUNCTION THAT SET THE EPISODE FROM WHERE START TO DOWNLOAD (RETRIVE FROM THE SLIDER)
    def setStart():
        st.session_state['start'] = st.session_state.sliderDA
        print("START: " + str(st.session_state['start']))
        return

    ## FUNCTION THAT SET THE EPISODE FROM WHERE END TO DOWNLOAD (RETRIVE FROM THE SLIDER)
    def setEnd():
        st.session_state['end'] = st.session_state.sliderA
        print("END: " + str(st.session_state['end']))
        return
    
    def setStart2():
        st.session_state['start'] = st.session_state.sliderDA2
        print("START: " + str(st.session_state['start']))
        return

    ## FUNCTION THAT SET THE EPISODE FROM WHERE END TO DOWNLOAD (RETRIVE FROM THE SLIDER)
    def setEnd2():
        st.session_state['end'] = st.session_state.sliderA2
        print("END: " + str(st.session_state['end']))
        return
    
    def getCol():
        return st.session_state.col


    def setName():
        st.session_state.checkSelect = True
        st.session_state['name'] = st.session_state['last_view']
        print(st.session_state['name'])
        return

    def CreateSelect():
        print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL " + str(st.session_state.disable))
        return st.selectbox("Ultimi anime visti: ", preferCreate(), on_change=setName(), disabled=st.session_state.disable)
 
    main()