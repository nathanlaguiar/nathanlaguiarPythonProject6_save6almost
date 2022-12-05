#Nathan Aguiar Project 6
import arcade

import Window

#Left and right to move
#X to shoot
# If enemies are close enough you might hit two with the same shot.


def main():
    our_window = Window.Window(
          1200, 1000, "Legendary Epic Mega Super Adventure Hero: The Re-Awakening")
    arcade.set_background_color(arcade.color.ARMY_GREEN),
    our_window.setup()
    arcade.run()

main()


