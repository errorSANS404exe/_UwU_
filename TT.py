import wrap_py, wrap_py.ru
from wrap_py import world, sprite

world.create_world(600, 600)
sprite.add_sprite("rocket_man", 300, 300, costume="rocket")
world.set_world_background_color_rgb(180, 45, 255)
pushka_UwU = sprite.add_sprite("X_X_pushka", 80, 600)
sprite.set_bottom_to(pushka_UwU, 600)
sprite.set_left_to(pushka_UwU, 0)
ball = sprite.add_sprite("spring", 100, 100)
scorost = 0
bullet=None
bullets=[]

@wrap_py.always(50)
def beskonechnoe_dvijenie_karika():
    global scorost
    sprite.move_sprite_by(ball, 0, scorost)
    scorost += 1
    niz = sprite.get_bottom(ball)
    if niz >= 600:
        sprite.set_bottom_to(ball, 600)
        scorost = - scorost * 0.8


@wrap_py.on_mouse_move
def mouse_move(pos):
    y = sprite.get_sprite_y(pushka_UwU)
    sprite.move_sprite_to(pushka_UwU, pos[0], y)
    left = sprite.get_left(pushka_UwU)
    right = sprite.get_right(pushka_UwU)
    if left <= 0:
        sprite.set_left_to(pushka_UwU, 0)
    if right >= 600:
        sprite.set_right_to(pushka_UwU,600)


@wrap_py.on_mouse_down()
def shooting():
    global bullet
    y=sprite.get_top(pushka_UwU)
    x=sprite.get_sprite_x(pushka_UwU)
    bullet=sprite.add_sprite("bullet",x,y)
    bullets.append(bullet)
    sprite.set_bottom_to(bullet,y)


@wrap_py.always
def flight():
    # if bullet is not None:
    #     x,y=sprite.get_sprite_pos(bullet)
    #     sprite.move_sprite_to(bullet,x,y-5)
    for bullet in bullets:
        x,y=sprite.get_sprite_pos(bullet)
        sprite.move_sprite_to(bullet,x,y-20)