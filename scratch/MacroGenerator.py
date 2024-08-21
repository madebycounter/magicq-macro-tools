macro = []


def num(n, zfill=4):
    return "{:x}".format(n).zfill(zfill)


def keycode(key):
    if key in "abcdefghijklmnopqrstuvwxyz1234567890`-=[]\;',./":
        return num(ord(key))
    else:
        return "0000"


def make_macro(number, name, steps, step_timing="00000008"):
    return (
        'K,{number},"{name}",{steps},{step_timing},0000,0000,0000,0000,'.format(
            number=num(number),
            name=name,
            steps=num(len(steps)),
            step_timing=step_timing,
        )
        + "\r\n"
        + ",".join(steps)
        + ",00000000,{},0;".format(step_timing)
    )


def make_step(time, type, var1="0000", var2="00000000", var3="00000000"):
    return ",".join([num(time, zfill=8), type, var1, var2, var3])


def mq_key_pressed(time, key):
    return make_step(time, "0100", var2="0090" + keycode(key))


def mq_key_released(time, key):
    return make_step(time, "0100", var2="0010" + keycode(key))


print(
    make_macro(
        10,
        "Test Macro",
        [
            mq_key_pressed(1, "w"),
            mq_key_released(2, "w"),
            mq_key_pressed(3, "i"),
            mq_key_released(4, "i"),
            mq_key_pressed(5, "l"),
            mq_key_released(6, "l"),
            mq_key_pressed(7, "l"),
            mq_key_released(8, "l"),
            mq_key_pressed(9, "i"),
            mq_key_released(10, "i"),
            mq_key_pressed(11, "a"),
            mq_key_released(12, "a"),
            mq_key_pressed(13, "m"),
            mq_key_released(14, "m"),
        ],
    )
)
