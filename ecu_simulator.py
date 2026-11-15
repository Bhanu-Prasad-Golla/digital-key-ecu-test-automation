def start_ecu():
    return "AWAKE"


def sleep_ecu():
    return "SLEEP"


def wake_ecu():
    return "AWAKE"


ecu_state = "OFF"
print("Initial state:", ecu_state)

ecu_state = start_ecu()
print("After startup:", ecu_state)

ecu_state = sleep_ecu()
print("After sleep command:", ecu_state)

ecu_state = wake_ecu()
print("After wakeup command:", ecu_state)

actual_state = sleep_ecu()
expected_state = "SLEEP"

if actual_state == expected_state:
    print("PASS: ECU entered sleep state")
else:
    print("FAIL: ECU did not enter sleep state")