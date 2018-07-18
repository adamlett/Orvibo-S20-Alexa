from orvibo.s20 import S20

def connect(ip, mac):
    try:
        s20 = S20(ip, mac) # Supply IP and MAC address
        return s20
    except:
        print("Connection could not be established: An error occurred")
        return False

def executeCommand(command, ip, mac):
    device = connect(ip, mac)
    # Check connection was formed
    if device:
        if command == 'on':
            on(device)
        elif command == 'off':
            off(device)
        elif command == 'toggle':
            toggle(device)
        else:
            print("Command not recognised")
            return False
        # Return success of command
        return True
    else:
        return False

# Switch commands
def on(device):
    device.on = True

def off(device):
    device.on = False

def toggle(device):
    device.on = not device.on
