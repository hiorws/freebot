from mbot_lib.mBot import *

def generate_bot():
    bot = mBot()
    bot.startWithSerial("/dev/ttyUSB0")
    # bot.startWithSerial("/dev/rfcomm0")
    return bot


def move_forward(bot, left, right):
    bot.doMove(left, right)
    print("Run Forward!")
