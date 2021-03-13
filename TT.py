import wrap_py, wrap_py.ru
from wrap_py import world, sprite

world.create_world(600, 600)
sprite.add_sprite("rocket_man", 300, 300, costume="rocket")
world.set_world_background_color_rgb(180, 45, 255)
num = sprite.add_sprite("X_X_pushka", 80, 600)
sprite.set_bottom_to(num, 600)
sprite.set_left_to(num, 0)
ball=sprite.add_sprite("spring",100,400)

@wrap_py.on_key_down(wrap_py.K_RIGHT, wrap_py.K_LEFT)
def dvijenie_pushki(key):
    if key == wrap_py.K_RIGHT:
        sprite.move_sprite_by(num, 10, 0)
    if key == wrap_py.K_LEFT:
        sprite.move_sprite_by(num, -10, 0)
