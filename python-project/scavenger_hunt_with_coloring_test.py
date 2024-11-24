from scavenger_hunt_with_coloring import main_program
from timinator import CONGRATS

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))

if __name__ == "__main__":
    main_program()
    channel = f'{random.choice(CONGRATS)} 🌟'
    
    message = 'Possible Message here.'
    send_msg(channel, message)
