function game_end () {
    music.startMelody(music.builtInMelody(Melodies.PowerDown), MelodyOptions.Once)
    game_start = 0
    basic.clearScreen()
    music.startMelody(music.builtInMelody(Melodies.Chase), MelodyOptions.ForeverInBackground)
    while (true) {
        basic.showString("score:")
        basic.pause(100)
        basic.showNumber(user_score)
        basic.pause(500)
        basic.clearScreen()
    }
}
input.onButtonPressed(Button.A, function () {
    if (game_start == 1) {
        led.unplot(user_bit_posx, 4)
        music.playTone(988, music.beat(BeatFraction.Sixteenth))
        user_bit_posx += -1
        if (user_bit_posx <= -1) {
            user_bit_posx = 0
        }
        led.plotBrightness(user_bit_posx, 4, 20)
    }
})
function block_check () {
    check_pos_y = 4
    for (let index = 0; index < 4; index++) {
        check_pos_x = 5
        check_pos_y += -1
        for (let index = 0; index < 5; index++) {
            check_pos_x += -1
            if (led.point(check_pos_x, check_pos_y)) {
                led.unplot(check_pos_x, check_pos_y)
                if (check_pos_y == 3) {
                    if (check_pos_x == user_bit_posx) {
                        game_end()
                    } else {
                        user_score += 2
                    }
                } else {
                    led.plot(check_pos_x, check_pos_y + 1)
                }
            }
        }
    }
}
input.onButtonPressed(Button.B, function () {
    if (game_start == 1) {
        led.unplot(user_bit_posx, 4)
        music.playTone(988, music.beat(BeatFraction.Sixteenth))
        user_bit_posx += 1
        if (user_bit_posx >= 5) {
            user_bit_posx = 4
        }
        led.plotBrightness(user_bit_posx, 4, 20)
    }
})
function block_set () {
    while (true) {
        music.playTone(988, music.beat(BeatFraction.Whole))
        basic.pause(1000)
        led.plot(randint(3, 4), 0)
        led.plot(randint(0, 2), 0)
        block_check()
    }
}
let check_pos_x = 0
let check_pos_y = 0
let game_start = 0
let user_bit_posx = 0
let user_score = 0
while (!(input.logoIsPressed())) {
    basic.showLeds(`
        . # . # .
        . . # . .
        # . # . #
        . . # . .
        . # . # .
        `)
    basic.showLeds(`
        . . # . .
        # . . . #
        . # # # .
        # . . . #
        . . # . .
        `)
}
basic.clearScreen()
user_score = 0
music.setBuiltInSpeakerEnabled(true)
if (!(input.buttonIsPressed(Button.A))) {
    music.startMelody(music.builtInMelody(Melodies.Nyan), MelodyOptions.Once)
    basic.showString("Micro:b Invader v2")
}
user_bit_posx = 2
music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.Once)
game_start = 1
block_set()
