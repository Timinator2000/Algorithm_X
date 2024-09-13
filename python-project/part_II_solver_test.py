from part_II_solver import main_program
from timinator import CONGRATS
import random

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

if __name__ == "__main__":
    main_program()
    send_msg(f"{random.choice(CONGRATS)} 🌟", "Algorithm X can handle as much responsibility as you can give it!")
