import cocos
from cocos.layer import Layer, ColorLayer
from cocos import layer
from cocos.sprite import Sprite
from cocos.actions import *
from cocos.director import director
from time import sleep


# Here I make a class that extends cocos' ColorLayer class
# This type of layer is different because it has a background color! (awesome right?)
class Actions(ColorLayer):
    # When I initialize it I need to pass in an RGBA colour value so it can set the ColorLayer's background
    # I grabbed the Peter River colour (#3498db) from http://flatuicolors.com for this sample
    def __init__(self):
        super(Actions, self).__init__(52, 152, 219, 1000)

        # I initialize a sprite using the cocos sprite.Sprite class
        # Change the path below to whatever your sprite image is
        self.sprite = Sprite('assets/img/grossini.png')

        # I set the sprite's position to the center of the screen
        self.sprite.position = 320, 240

        # Here are all the actions I make my sprite perform
        # Check those class functions for info on how to code them!
        self.fade_in()
        self.move_left()

        # It's important to note that placing actions one after another can often lead to issues
        # For example, if you told the sprite to move left one and then move right twice, it would only move right once
        # This is because python executes the code so quickly that it doesn't have time to complete the first animations
        # Using the typical time.sleep from the time builtin doesn't work either, because it stops the entire game
        # However, actions can be added together in the do() function of the sprite using the + operator
        # This works very well and allows you to string actions like moving left and right together

    def fade_in(self):
        # First I make a FadeIn animation object
        fade_action = FadeIn(2)

        # I set the sprite opacity to 0 so that it doesn't flash on the screen.
        # You should try removing this to see what happens
        self.sprite.opacity = 0

        # I add the sprite to the screen (remember it can't be seen yet)
        self.add(self.sprite, z=1)

        # I then start the fading in (which takes 2 seconds)
        # I don't need to reset the opacity because the FadeIn action does that for me!
        self.sprite.do(fade_action)

    def move_left(self):
        # First I make a MoveBy animation object
        # I set this to move -150 on the X axis, 0 on the Y axis, and to take 2 seconds
        left = MoveBy((-150, 0), 2)

        # Finally I make my sprite move left
        self.sprite.do(left)


# I initialize the director and run the layer (this is typical for cocos programs)
director.init()
director.run(cocos.scene.Scene(Actions()))
