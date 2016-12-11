from bot import Bot

BOT = Bot()

ACTION_METHODS = {
    'F' : BOT.fw_step,
    'B' : BOT.back_step,
    'L' : BOT.turn_left,
    'R' : BOT.turn_right,
    'S' : BOT.stop,
    'U' : BOT.axe_up,
    'D' : BOT.axe_down,
    'O' : BOT.open_claws,
    'C' : BOT.close_claws
    }

def run(sequence):
    """
    Input is a string where each characters
    represents an action. Each action is executed according
    to the defined action method mapping
    """
    for action in sequence:
        if action in ACTION_METHODS:
            ACTION_METHODS[action]()
