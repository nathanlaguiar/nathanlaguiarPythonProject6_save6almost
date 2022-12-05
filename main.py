import arcade

import Window
#from Comp151Window import Comp151Window

def main():
    our_window = Window.Window(
          1200, 1000, "Legendary Epic Mega Super Adventure Hero: The Re-Awakening")
    arcade.set_background_color(arcade.color.ARMY_GREEN),
    our_window.setup()
    arcade.run()

main()
