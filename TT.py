import wrap_py, wrap_py.ru
from wrap_py import world, sprite

world.create_world(600, 600)
sprite.add_sprite("rocket_man", 300, 300, costume="rocket")
world.set_world_background_color_rgb(180, 45, 255)
num = sprite.add_sprite("X_X_pushka", 80, 600)
sprite.set_bottom_to(num, 600)
sprite.set_left_to(num, 0)
ball = sprite.add_sprite("spring", 100, 100)
scorost = 0


@wrap_py.on_key_down(wrap_py.K_RIGHT, wrap_py.K_LEFT)
def dvijenie_pushki(key):
    if key == wrap_py.K_RIGHT:
        sprite.move_sprite_by(num, 10, 0)
    if key == wrap_py.K_LEFT:
        sprite.move_sprite_by(num, -10, 0)


@wrap_py.always(50)
def beskonechnoe_dvijenie_karika():
    global scorost
    sprite.move_sprite_by(ball, 0, scorost)
    scorost += 1
    niz = sprite.get_bottom(ball)
    if niz >= 600:
        sprite.set_bottom_to(ball, 600)
        scorost = - scorost * 0.8
