import pgzrun


def on_key_up(key):
    if key == keys.ESCAPE:
        exit()


# The last line starts pgzero:
pgzrun.go()


