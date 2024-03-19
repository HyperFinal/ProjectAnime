import random
from streamlit_card import card
from startfile import startfile

class CardObj():
  def __init__(self, title, ep, image, path):
    self.title = title
    self.ep = ep
    self.image = image
    self.path = path

  def start(self):
    startfile(self.path)
    print("AVVIO FILE " + self.path)

  def display(self):
    random_number = random.randint(0,10000000)
    card(self.title, self.ep, self.image, key=random_number)
    print("test")
    return True
  
  
