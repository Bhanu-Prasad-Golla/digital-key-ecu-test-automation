# ECU command functions
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

# Demonstrate the ECU state sequence
ecu_state = "OFF"
print("Initial state:", ecu_state)

ecu_state = start_ecu()
print("After startup:", ecu_state)

ecu_state = sleep_ecu(ecu_state)
print("After sleep command:", ecu_state)

ecu_state = wake_ecu(ecu_state)
print("After wakeup command:", ecu_state)


# Automated checks
print("\n--- ECU TEST RESULTS ---")

# Test 1: Sleep
actual_state = sleep_ecu(ecu_state)
expected_state = "SLEEP"

if actual_state == expected_state:
    print("PASS: ECU entered sleep state")
else:
    print("FAIL: ECU did not enter sleep state")

# Test 2: Startup
actual_state = start_ecu()
expected_state = "AWAKE"

if actual_state == expected_state:
    print("PASS: ECU startup")
else:
    print("FAIL: ECU startup")

# Test 3: Wakeup
actual_state = wake_ecu(ecu_state)
expected_state = "AWAKE"

if actual_state == expected_state:
    print("PASS: ECU wakeup")
else:
    print("FAIL: ECU wakeup")

actual_state = sleep_ecu("AWAKE")
expected_state = "SLEEP"

if actual_state == expected_state:
    print("PASS: Awake ECU enters sleep")
else:
    print("FAIL: Awake ECU did not enter sleep")

# An OFF ECU must stay OFF after a sleep command
actual_state = sleep_ecu("OFF")

if actual_state == "OFF":
    print("PASS: Sleep command keeps OFF ECU OFF")
else:
    print("FAIL: Sleep command changed OFF ECU")


# An OFF ECU must stay OFF after a wakeup command
actual_state = wake_ecu("OFF")

if actual_state == "OFF":
    print("PASS: Wakeup command keeps OFF ECU OFF")
else:
    print("FAIL: Wakeup command changed OFF ECU")