import kivy
kivy.require('1.10.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.properties import ListProperty, ObjectProperty
from kivy.graphics.vertex_instructions import(Rectangle, Ellipse, Line)
from kivy.graphics.context_instructions import Color

import random

class Mainy(GridLayout):

	def __init__(self, **kwargs):
		super(Mainy, self).__init__(**kwargs)
		self.cols = 1
		



class MyApp(App):

    def build(self):
        return Mainy()


if __name__ == '__main__':
    MyApp().run()