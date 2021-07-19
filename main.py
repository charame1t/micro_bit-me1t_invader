def touch_true_check():
    global user_bit
    user_bit.delete()
    if led.point(user_bit_pos, 4):
        game_end()
    user_bit = game.create_sprite(user_bit_pos, 5)
def game_end():
    global game_start
    music.start_melody(music.built_in_melody(Melodies.POWER_DOWN),
        MelodyOptions.ONCE)
    game_start = 0
    basic.clear_screen()
    music.start_melody(music.built_in_melody(Melodies.CHASE),
        MelodyOptions.FOREVER_IN_BACKGROUND)
    while True:
        basic.show_string("score:")
        basic.pause(100)
        basic.show_number(user_score)
        basic.pause(500)
        basic.clear_screen()

def on_button_pressed_a():
    global user_bit_pos, user_bit
    if game_start == 1:
        music.play_tone(988, music.beat(BeatFraction.SIXTEENTH))
        user_bit_pos += -1
        if user_bit_pos <= -1:
            user_bit_pos = 0
        user_bit.delete()
        user_bit = game.create_sprite(user_bit_pos, 5)
        touch_true_check()
input.on_button_pressed(Button.A, on_button_pressed_a)

def block_check():
    global check_pos_y, check_pos_x
    check_pos_y = 4
    for index in range(4):
        check_pos_x = 5
        check_pos_y += -1
        for index2 in range(5):
            check_pos_x += -1
            if led.point(check_pos_x, check_pos_y):
                music.play_tone(262, music.beat(BeatFraction.WHOLE))

def on_button_pressed_b():
    global user_bit_pos, user_bit
    if game_start == 1:
        music.play_tone(988, music.beat(BeatFraction.SIXTEENTH))
        user_bit_pos += 1
        if user_bit_pos >= 6:
            user_bit_pos = 5
        user_bit.delete()
        user_bit = game.create_sprite(user_bit_pos, 5)
        touch_true_check()
input.on_button_pressed(Button.B, on_button_pressed_b)

def block_set():
    while True:
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        basic.pause(1000)
        led.plot(randint(3, 4), 0)
        led.plot(randint(0, 2), 0)
        block_check()
        touch_true_check()
check_pos_x = 0
check_pos_y = 0
game_start = 0
user_bit_pos = 0
user_bit: game.LedSprite = None
user_score = 0
while not (input.logo_is_pressed()):
    basic.show_leds("""
        . # . # .
                . . # . .
                # . # . #
                . . # . .
                . # . # .
    """)
    basic.show_leds("""
        . . # . .
                # . . . #
                . # # # .
                # . . . #
                . . # . .
    """)
basic.clear_screen()
user_score = 173
music.set_built_in_speaker_enabled(True)
music.start_melody(music.built_in_melody(Melodies.NYAN), MelodyOptions.ONCE)
basic.show_string("Micro:b Invader v2")
user_bit = game.create_sprite(2, 5)
user_bit_pos = 2
music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
    MelodyOptions.ONCE)
game_start = 1
block_set()