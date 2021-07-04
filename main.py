def snake_head_move():
    global snake_head_y, snake_head_x
    if snake_direction == 0:
        snake_head_y += -1
    elif snake_direction == 1:
        snake_head_x += 1
    elif snake_direction == 2:
        snake_head_y += 1
    elif snake_direction == 3:
        snake_head_x += -1
def did_snake_eat_apple():
    global speed
    if snake_head_x == apple_x and snake_head_y == apple_y:
        apple_spawn()
        snake_body_x.append(snake_body_x[len(snake_body_x) - 1])
        snake_body_y.append(snake_body_y[len(snake_body_y) - 1])
        speed += speed / 15
def snake_head_teleport():
    global snake_head_x, snake_head_y
    if snake_head_x < 0:
        snake_head_x = 4
    elif snake_head_x > 4:
        snake_head_x = 0
    elif snake_head_y < 0:
        snake_head_y = 4
    elif snake_head_y > 4:
        snake_head_y = 0
def snake_spin():
    global snake_direction
    if snake_rotate > 0:
        snake_direction += 1
    if snake_rotate < 0:
        snake_direction += -1
    if snake_direction > 3:
        snake_direction = 0
    if snake_direction < 0:
        snake_direction = 3

def on_button_pressed_a():
    global snake_rotate
    snake_rotate += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

# Tato funkce udělá 2 seznamy do kterých se uloží volná místa na hracím poli. Jeden seznam skladuje x-pozice, druhý y-pozice. Stejný index u obou seznamů společně tvoří souřadnici volného místa. Po vytvoření těchto seznamů, se udělá proměnná jablko_volny_misto do kterého se uloží náhodně vybrané číslo, které není delší než počet indexů. Toto náhodné číslo slouží jako index který určí jaký volný místo na hernim poli bude použito pro umístění jablka
def apple_spawn():
    global apple_available_x, apple_available_y, apple_available_space, apple_x, apple_y
    apple_available_x = []
    apple_available_y = []
    for order in range(25):
        if not (led.point(order % 5, Math.floor(order / 5))):
            apple_available_x.append(order % 5)
            apple_available_y.append(Math.floor(order / 5))
    if len(apple_available_x) > 0:
        apple_available_space = randint(0, len(apple_available_x) - 1)
        apple_x = apple_available_x[apple_available_space]
        apple_y = apple_available_y[apple_available_space]
    else:
        basic.pause(500)
        basic.show_string("VYHRA!")
        reset()
def snake_death():
    order2 = 0
    while order2 <= len(snake_body_x) - 2:
        if snake_head_x == snake_body_x[order2 + 1] and snake_head_y == snake_body_y[order2 + 1]:
            basic.show_number(len(snake_body_x))
            basic.clear_screen()
            basic.pause(500)
            basic.show_string("KONEC")
            reset()
        order2 += 1

def on_button_pressed_b():
    global snake_rotate
    snake_rotate += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

# Posouvá předposlední hodnotu na poslední, předpředposledním na předposlední atd. První pozice je nastavena na pozici hlavy hada.
def snake_body_move():
    order3 = 0
    while order3 <= len(snake_body_x) - 2:
        snake_body_x[len(snake_body_x) - (order3 + 1)] = snake_body_x[len(snake_body_x) - (order3 + 2)]
        snake_body_y[len(snake_body_y) - (order3 + 1)] = snake_body_y[len(snake_body_y) - (order3 + 2)]
        order3 += 1
    snake_body_x[0] = snake_head_x
    snake_body_y[0] = snake_head_y
def reset():
    global speed, snake_head_x, snake_head_y, snake_body_x, snake_body_y, snake_direction
    speed = 300
    snake_head_x = 2
    snake_head_y = 2
    snake_body_x = [snake_head_x]
    snake_body_y = [snake_head_y]
    snake_direction = 0
    led.plot_brightness(apple_x, apple_y, 255)
    led.plot_brightness(snake_head_x, snake_head_y, 50)
    basic.pause(speed)
apple_available_space = 0
apple_available_y: List[number] = []
apple_available_x: List[number] = []
snake_rotate = 0
speed = 0
snake_body_y: List[number] = []
snake_body_x: List[number] = []
apple_y = 0
apple_x = 0
snake_head_x = 0
snake_head_y = 0
snake_direction = 0
basic.show_string("SNAKE")
reset()

def on_forever():
    global snake_rotate
    basic.clear_screen()
    snake_spin()
    snake_head_move()
    snake_head_teleport()
    snake_body_move()
    snake_death()
    order4 = 0
    while order4 <= len(snake_body_x) - 1:
        led.plot_brightness(snake_body_x[order4], snake_body_y[order4], 5)
        order4 += 1
    did_snake_eat_apple()
    led.plot_brightness(snake_head_x, snake_head_y, 50)
    led.plot_brightness(apple_x, apple_y, 255)
    snake_rotate = 0
    basic.pause(speed)
basic.forever(on_forever)
