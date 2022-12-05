#Nathan Aguiar  Project 6
import random

import arcade


class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.score = 0
        self.player = None
        self.targets = arcade.SpriteList()
       # self.sound = None
        self.player_dx = 0
        self.player_dy = 0
        self.arrow = arcade.Sprite("ImagesForClass/ball-magenta.png")
        self.arrows = arcade.SpriteList()

    def setup(self):
       # self.sound = arcade.load_sound("elec_lightning.wav")
        self.player = arcade.Sprite("ImagesForClass\marksman.png")
        self.player.center_x = 500
        self.player.center_y = 100
        for ogre in range(20):
            self.target = arcade.Sprite("ImagesForClass\ogre.png")
            self.target.center_x = random.randint(200, 997)
            self.target.center_y = random.randint(925, 997)
            self.targets.append(self.target)
        for arrow in range(0):
            self.arrow = arcade.Sprite("ImagesForClass/ball-magenta.png")
            self.arrows.append(self.arrow)



    def on_update(self, time_since_update):
        #enemy_collision = arcade.check_for_collision_with_list(self.arrow, self.targets)
        #enemy_kill = arcade.check_for_collision_with_list(self.player, self.targets)
        self.player.center_x += self.player_dx
        if self.player.center_x > 1200:
            self.player.center_x = 0
           # arcade.play_sound(self.sound)
        if self.player.center_x < 0:
            self.player.center_x = 1200
           # arcade.play_sound(self.sound)

        self.player.center_y += self.player_dy
        if self.player.center_y > 1000:
            self.player.center_y = 0
            #arcade.play_sound(self.sound)
        if self.player.center_y < 0:
            self.player.center_y = 1000
            #arcade.play_sound(self.sound)
        for enemy in self.targets:
            enemy.center_y -= random.randint(0, 1)
            if enemy.center_y <= 0:
                enemy.center_y = 1000
            enemy.center_x += random.randint(0, 0)
        for arrow in self.arrows:
            enemy_collision = arcade.check_for_collision_with_list(self.target, self.arrows)
            #arrow.center_y = self.player.center_y
            #if arrow.center_y <= 0:
            arrow.center_y += 30
            if enemy_collision:
                    #arcade.play_sound(self.sound)
                    self.score += len(enemy_collision)
                    for enemy_down in enemy_collision:
                            self.arrows.remove(self.targets)
            #if enemy_kill:
                #arcade.play_sound(self.sound)
              #  arcade.draw_text(f"You Lose!!", 450, 470,
                       #          arcade.color.BLACK, 150)
               # exit()
           # if self.score == 20:
                # arcade.play_sound(self.sound)
              #  arcade.draw_text(f"You Win!!!", 450, 470,
                       #          arcade.color.BLACK, 150)


    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.targets.draw()
        self.arrows.draw()
        arcade.draw_text(f"Your score: {self.score}", 50, 970,
                         arcade.color.BLACK, 15)
        arcade.finish_render()

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player_dx = -6
        elif symbol == arcade.key.RIGHT:
            self.player_dx = 6
        elif symbol == arcade.key.UP:
            self.player_dy = 6
        elif symbol == arcade.key.DOWN:
            self.player_dy = -6
        elif symbol == arcade.key.X:
            arrow = arcade.Sprite("ImagesForClass/ball-magenta.png")
            arrow.center_y = self.player.center_y
            arrow.center_x = self.player.center_x
            self.arrows.append(arrow)

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT and self.player_dx < 0:
            self.player_dx = 0
        elif symbol == arcade.key.RIGHT and self.player_dx > 0:
            self.player_dx = 0
        elif symbol == arcade.key.UP and self.player_dy > 0:
            self.player_dy = 0
        elif symbol == arcade.key.DOWN and self.player_dy < 0:
            self.player_dy = 0
