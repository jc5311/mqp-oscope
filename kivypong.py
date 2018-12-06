import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

class PongBall(Widget):
	#velocity of the ball on the x and y axis
	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)

	#reference list? I guess it can be used so we can
	#short hand directional veloecity as ball.velocity(x,y)
	velocity = ReferenceListProperty(velocity_x, velocity_y)

	def move(self):
		#used to the move the ball on each frame
		self.pos = vector(*self.velocity) + self.pos

class PongGame(Widget):
	pass

class PongApp(App):
	def build(self):
		App.title = "KivyPong!"
		return PongGame()

if __name__ == '__main__':
	PongApp().run()