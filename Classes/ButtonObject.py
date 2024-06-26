import streamlit as st
from streamlit_card import card
from startfile import startfile
import random

class ButtonObj():
  def __init__(self, text, path, nameF):
    self.path = path
    self.text = text
    self.name = nameF
    print("PATH BUTTON INSIDE BUTTON OBJ: " + self.path)
    
  def getText(self):
      return self.text
  def getName(self):
      return self.name
  def getPath(self):
      return self.path
  def getKey(self):
     random_number = random.randint(0,10000000)
     return random_number
  
  def display(self):
    st.button(self.text, key=self.getKey())
    print("PATH B: " + self.getPath())


