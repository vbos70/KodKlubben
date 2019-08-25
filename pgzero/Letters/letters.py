import pgzrun

WIDTH = 600
HEIGHT = 500

class LetterGame:

    def __init__(self):
        self.words = [
            "Kodklubben!",
            "kodare",
            "hacka",
            "dator",
            "game"
        ]
        self.index = 0
        self.total_time = 0.0
        self.time_step = 0.10
        self.game_started = False
        self.letters_typed = 0
        self.score = 0

    def get_word(self):
        return self.words[self.index]

    def next_word(self):
        self.index = self.index + 1
        if self.index >= len(self.words):
            self.index = 0
        return self.get_word()

    def increase_time(self):
        self.total_time = self.total_time + self.time_step

word_pos = (WIDTH / 2, HEIGHT / 4)
typed_word_pos = (WIDTH / 2, HEIGHT / 2)
score_pos = (WIDTH / 2, HEIGHT * 3 / 4)

lg = LetterGame()

def on_key_down(key, unicode, mod):
    # Use this for printing the key values
    print(key, unicode, mod)

    if key in [ keys.LSHIFT, keys.RSHIFT ]:
        # user presses a SHIFT key, this could be ok, so ignore for now
        pass
    elif key == keys.ESCAPE:
        exit()
    elif key == keys.RETURN:
        lg.next_word()
        lg.letters_typed = 0
        lg.total_time = 0.0
    else:
        word = lg.get_word()
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
    if lg.letters_typed == 0 and not lg.game_started:
        lg.game_started = True
        clock.schedule_interval(lg.increase_time, lg.time_step)

    elif lg.letters_typed >= len(lg.get_word()):
        clock.unschedule(lg.increase_time)
        lg.game_started = False

def draw():
    screen.fill((0,0,0))
    word = lg.get_word()
    screen.draw.text(word, midbottom=word_pos, fontsize=32)
    if lg.letters_typed > 0:
        screen.draw.text(word[:lg.letters_typed], midbottom=typed_word_pos, fontsize=32)
    screen.draw.text("letters to type: " + str(len(word) - lg.letters_typed), midbottom=score_pos, fontsize=32)
    screen.draw.text("Time: {:6g}".format(lg.total_time), topright=(WIDTH-2, 2), fontsize = 24)
    screen.draw.text("SCORE: {:d}".format(lg.score), topleft=(2,2), fontsize=24)