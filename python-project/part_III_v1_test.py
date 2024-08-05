from part_III_v1 import main_program
from timinator import CONGRATS
import random

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

if __name__ == "__main__":
    main_program()
    send_msg(f"{random.choice(CONGRATS)} 🌟", "I want you to know it is way harder to hard-code all those requirements and actions than it is to build them algorithmically with loops!")
    send_msg(f"{random.choice(CONGRATS)} 🌟", "I probably had to fix 20+ typos before it worked properly. Proof that algorithms are much more precise than us humans!")
