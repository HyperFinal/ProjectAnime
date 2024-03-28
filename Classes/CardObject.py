import random
from streamlit_card import card
from startfile import startfile

class CardObj():
  def __init__(self, title, ep, image):
    self.title = title
    self.ep = ep
    self.image = image

  def display(self):
    random_number = random.randint(0,10000000)
    card(self.title, self.ep, self.image, key=random_number)
    print("card displayed")

  
  
