def start_ecu():
    return "AWAKE"


def sleep_ecu(current_state):
    if current_state == "AWAKE":
        return "SLEEP"
    else:
        return current_state 


def wake_ecu(current_state):
    if current_state == "SLEEP":
        return "AWAKE"
    else:
        return current_state

def power_off_ecu(current_state):
    return "OFF"

def process_command(current_state, command):
    if command == "START":
        return start_ecu()
    elif command == "SLEEP":
        return sleep_ecu(current_state)
    elif command == "WAKE":
        return wake_ecu(current_state)
    elif command == "OFF":
        return power_off_ecu(current_state)
    else:
        return current_state

def connect_ble(ecu_state):
    if ecu_state == "AWAKE":
        return "CONNECTED"
    else:
        return "DISCONNECTED"

def disconnect_ble(ble_status):
    return "DISCONNECTED"