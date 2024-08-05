from part_III_v1 import main_program
from timinator import CONGRATS
import random

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

if __name__ == "__main__":
    main_program()
    send_msg(f"{random.choice(CONGRATS)} 🌟", "Hopefully the actions printed!")
