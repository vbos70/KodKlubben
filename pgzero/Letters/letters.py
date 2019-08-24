import pgzrun

WIDTH = 600
HEIGHT = 500

word = "Kodklubben!"
word_pos = (WIDTH / 2, HEIGHT / 4)
typed_word_pos = (WIDTH / 2, HEIGHT / 2)
letters_typed = 0
score_pos = (WIDTH / 2, HEIGHT * 3 / 4)

time_started = False
time = 0
delay = 0.25

def increase_time():
    global time
    time += delay


def on_key_down(key, unicode, mod):
    global letters_typed

    # Use this for printing the key values
    #print(key, unicode, mod)

    if key in [ keys.LSHIFT, keys.RSHIFT ]:
        # user presses a SHIFT key, this could be ok, so ignore for now
        pass
    else:
        if letters_typed < len(word):
            if unicode == word[letters_typed]:
                # User pressed right key!
                letters_typed += 1
            else:
                # User pressed a wrong key, start from the beginning
                letters_typed = 0
                
def update():
    global time_started
    if letters_typed == 0 and not time_started:
        time_started = True
        clock.schedule_interval(increase_time, delay)
        
    elif letters_typed >= len(word):
        clock.unschedule(increase_time)
        time_started = False

def draw():
    screen.fill((0,0,0))
    screen.draw.text(word, midbottom=word_pos, fontsize=32)
    if letters_typed > 0:
        screen.draw.text(word[:letters_typed], midbottom=typed_word_pos, fontsize=32)        
    screen.draw.text("letters to type: " + str(len(word) - letters_typed), midbottom=score_pos, fontsize=32)
    screen.draw.text("Time: " + str(time), bottomright=(WIDTH-2, HEIGHT-2), fontsize = 24)

