import wrap_py, wrap_py.ru
from wrap_py import world, sprite

world.create_world(600, 600)
sprite.add_sprite("rocket_man", 300, 300, costume="rocket")
world.set_world_background_color_rgb(180, 45, 255)
pushka_UwU = sprite.add_sprite("X_X_pushka", 80, 600)
sprite.set_bottom_to(pushka_UwU, 600)
sprite.set_left_to(pushka_UwU, 0)
ball = sprite.add_sprite("spring", 300, 0)
ballhp = sprite.add_text(300, 0, "3",text_color=[255,255,255],font_size=25)
scorost = 0
bullet = None
bullets = []
balls = []
d = {"number": ball, "scorost": 0, "scorostx": 5, "ballhp": ballhp}
balls.append(d)

ball2 = sprite.add_sprite("spring", 200, 400)
ballhp2=sprite.add_text(200,400,"5",text_color=[255,255,255],font_size=25)
b = {"number": ball2, "scorost": 0, "scorostx": -8,"ballhp":ballhp2}
balls.append(b)


@wrap_py.always(50)
def beskonechnoe_dvijenie_karika():
    global scorost
    for ball in balls:
        sprite.move_sprite_by(ball["number"], ball["scorostx"], ball["scorost"])
        ball["scorost"] += 1
        # print(ball["scorost"])
        # отбивка от низа
        niz = sprite.get_bottom(ball["number"])
        if niz >= 600:
            sprite.set_bottom_to(ball["number"], 600)
            ball["scorost"] = - ball["scorost"] * 0.9
            # if scorost < 9:
            if ball["scorost"] > -20:
                ball["scorost"] = - 20
            #     ball["scorost"]=-20
            print(ball["scorost"])
        # отбивка от правой границы
        right = sprite.get_right(ball["number"])
        if right >= 600:
            sprite.set_right_to(ball["number"], 600)
            ball["scorostx"] = - ball["scorostx"]

        left = sprite.get_left(ball["number"])
        if left <= 0:
            sprite.set_left_to(ball["number"], 0)
            ball["scorostx"] = -ball["scorostx"]
        sprite.move_sprite_to(ball["ballhp"],sprite.get_sprite_x(ball["number"]),sprite.get_sprite_y(ball["number"]))

@wrap_py.on_mouse_move
def mouse_move(pos):
    y = sprite.get_sprite_y(pushka_UwU)
    sprite.move_sprite_to(pushka_UwU, pos[0], y)
    left = sprite.get_left(pushka_UwU)
    right = sprite.get_right(pushka_UwU)
    if left <= 0:
        sprite.set_left_to(pushka_UwU, 0)
    if right >= 600:
        sprite.set_right_to(pushka_UwU, 600)


@wrap_py.on_mouse_down()
def shooting():
    global bullet
    y = sprite.get_top(pushka_UwU)
    x = sprite.get_sprite_x(pushka_UwU)
    bullet = sprite.add_sprite("bullet", x, y)
    bullets.append(bullet)
    sprite.set_bottom_to(bullet, y)


@wrap_py.always
def flight():
    # if bullet is not None:
    #     x,y=sprite.get_sprite_pos(bullet)
    #     sprite.move_sprite_to(bullet,x,y-5)
    for bullet in bullets:
        x, y = sprite.get_sprite_pos(bullet)
        sprite.move_sprite_to(bullet, x, y - 20)
