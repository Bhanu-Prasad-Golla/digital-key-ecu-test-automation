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