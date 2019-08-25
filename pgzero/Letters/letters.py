import pgzrun

WIDTH = 600
HEIGHT = 500

class LetterGame: pass

lg = LetterGame()
lg.words = [
    "Kodklubben!",
    "kodare",
    "hacka",
    "dator",
    "game"
]
lg.index = 0
lg.total_time = 0.0
lg.time_step = 0.10
lg.game_started = False
lg.letters_typed = 0
lg.score = 0

def get_word():
    return lg.words[lg.index]

def next_word():
    lg.index = lg.index + 1
    if lg.index >= len(lg.words):
        lg.index = 0
    return get_word()

def increase_time():
    lg.total_time = lg.total_time + lg.time_step

word_pos = (WIDTH / 2, HEIGHT / 4)
word_speed = 1
typed_word_pos = (WIDTH / 2, HEIGHT / 2)
score_pos = (WIDTH / 2, HEIGHT * 3 / 4)

def on_key_down(key, unicode, mod):
    # Use this for printing the key values
    print(key, unicode, mod)

    if key in [ keys.LSHIFT, keys.RSHIFT ]:
        # user presses a SHIFT key, this could be ok, so ignore for now
        pass
    elif key == keys.ESCAPE:
        exit()
    elif key == keys.RETURN:
        next_word()
        lg.letters_typed = 0
        lg.total_time = 0.0
    else:
        word = get_word()
        if lg.letters_typed < len(word):
            if unicode == word[lg.letters_typed]:
                # User pressed right key!
                lg.letters_typed += 1
                if lg.letters_typed == len(word):
                    lg.score += 1
            else:
                # User pressed a wrong key, start from the beginning
                lg.letters_typed = 0

def update():

    global word_pos
    global word_speed

    if lg.letters_typed == 0 and not lg.game_started:
        lg.game_started = True
        clock.schedule_interval(increase_time, lg.time_step)

    elif lg.letters_typed >= len(get_word()):
        clock.unschedule(increase_time)
        lg.game_started = False

    word_pos = (word_pos[0] + word_speed, word_pos[1])
    if word_pos[0] < 0:
        word_speed = 1
    elif word_pos[0] >= WIDTH:
        word_speed = -1

def draw():
    screen.fill((0,0,0))
    word = get_word()
    screen.draw.text(word, midbottom=word_pos, fontsize=32)
    if lg.letters_typed > 0:
        screen.draw.text(word[:lg.letters_typed], midbottom=typed_word_pos, fontsize=32)
    screen.draw.text("letters to type: " + str(len(word) - lg.letters_typed), midbottom=score_pos, fontsize=32)
    screen.draw.text("Time: {:6g}".format(lg.total_time), topright=(WIDTH-2, 2), fontsize = 24)
    screen.draw.text("SCORE: {:d}".format(lg.score), topleft=(2,2), fontsize=24)
