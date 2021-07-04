function snake_head_move () {
    if (snake_direction == 0) {
        snake_head_y += -1
    } else if (snake_direction == 1) {
        snake_head_x += 1
    } else if (snake_direction == 2) {
        snake_head_y += 1
    } else if (snake_direction == 3) {
        snake_head_x += -1
    }
}
function did_snake_eat_apple () {
    if (snake_head_x == apple_x && snake_head_y == apple_y) {
        apple_spawn()
        snake_body_x.push(snake_body_x[snake_body_x.length - 1])
        snake_body_y.push(snake_body_y[snake_body_y.length - 1])
        speed += speed / 15
    }
}
function snake_head_teleport () {
    if (snake_head_x < 0) {
        snake_head_x = 4
    } else if (snake_head_x > 4) {
        snake_head_x = 0
    } else if (snake_head_y < 0) {
        snake_head_y = 4
    } else if (snake_head_y > 4) {
        snake_head_y = 0
    }
}
function snake_spin () {
    if (snake_rotate > 0) {
        snake_direction += 1
    }
    if (snake_rotate < 0) {
        snake_direction += -1
    }
    if (snake_direction > 3) {
        snake_direction = 0
    }
    if (snake_direction < 0) {
        snake_direction = 3
    }
}
input.onButtonPressed(Button.A, function () {
    snake_rotate += -1
})
// Tato funkce udělá 2 seznamy do kterých se uloží volná místa na hracím poli. Jeden seznam skladuje x-pozice, druhý y-pozice. Stejný index u obou seznamů společně tvoří souřadnici volného místa. Po vytvoření těchto seznamů, se udělá proměnná jablko_volny_misto do kterého se uloží náhodně vybrané číslo, které není delší než počet indexů. Toto náhodné číslo slouží jako index který určí jaký volný místo na hernim poli bude použito pro umístění jablka
function apple_spawn () {
    apple_available_x = []
    apple_available_y = []
    for (let order = 0; order <= 24; order++) {
        if (!(led.point(order % 5, Math.floor(order / 5)))) {
            apple_available_x.push(order % 5)
            apple_available_y.push(Math.floor(order / 5))
        }
    }
    if (apple_available_x.length > 0) {
        apple_available_space = randint(0, apple_available_x.length - 1)
        apple_x = apple_available_x[apple_available_space]
        apple_y = apple_available_y[apple_available_space]
    } else {
        basic.pause(500)
        basic.showString("VYHRA!")
        reset()
    }
}
function snake_death () {
    for (let order = 0; order <= snake_body_x.length - 2; order++) {
        if (snake_head_x == snake_body_x[order + 1] && snake_head_y == snake_body_y[order + 1]) {
            basic.showNumber(snake_body_x.length)
            basic.clearScreen()
            basic.pause(500)
            basic.showString("KONEC")
            reset()
        }
    }
}
input.onButtonPressed(Button.B, function () {
    snake_rotate += 1
})
// Posouvá předposlední hodnotu na poslední, předpředposledním na předposlední atd. První pozice je nastavena na pozici hlavy hada.
function snake_body_move () {
    for (let order = 0; order <= snake_body_x.length - 2; order++) {
        snake_body_x[snake_body_x.length - (order + 1)] = snake_body_x[snake_body_x.length - (order + 2)]
        snake_body_y[snake_body_y.length - (order + 1)] = snake_body_y[snake_body_y.length - (order + 2)]
    }
    snake_body_x[0] = snake_head_x
    snake_body_y[0] = snake_head_y
}
function reset () {
    speed = 300
    snake_head_x = 2
    snake_head_y = 2
    snake_body_x = [snake_head_x]
    snake_body_y = [snake_head_y]
    snake_direction = 0
    led.plotBrightness(apple_x, apple_y, 255)
    led.plotBrightness(snake_head_x, snake_head_y, 50)
    basic.pause(speed)
}
let apple_available_space = 0
let apple_available_y: number[] = []
let apple_available_x: number[] = []
let snake_rotate = 0
let speed = 0
let snake_body_y: number[] = []
let snake_body_x: number[] = []
let apple_y = 0
let apple_x = 0
let snake_head_x = 0
let snake_head_y = 0
let snake_direction = 0
basic.showString("SNAKE")
reset()
basic.forever(function () {
    basic.clearScreen()
    snake_spin()
    snake_head_move()
    snake_head_teleport()
    snake_body_move()
    snake_death()
    for (let order = 0; order <= snake_body_x.length - 1; order++) {
        led.plotBrightness(snake_body_x[order], snake_body_y[order], 5)
    }
    did_snake_eat_apple()
    led.plotBrightness(snake_head_x, snake_head_y, 50)
    led.plotBrightness(apple_x, apple_y, 255)
    snake_rotate = 0
    basic.pause(speed)
})
