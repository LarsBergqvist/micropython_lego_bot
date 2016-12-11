from bot import Bot

robot = Bot()

action_methods = { 
    'F' : robot.fw_step,
    'B' : robot.back_step,
    'L' : robot.turn_left,
    'R' : robot.turn_right,
    'S' : robot.stop,
    'U' : robot.hammer_up,
    'D' : robot.hammer_down,
    'O' : robot.open_claws,
    'C' : robot.close_claws
    }

def run(sequence):
    for action in sequence:
        if action in action_methods:
            action_methods[action]()
