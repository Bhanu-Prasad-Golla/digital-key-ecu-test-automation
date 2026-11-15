# ECU command functions
def start_ecu():
    return "AWAKE"


def sleep_ecu():
    return "SLEEP"


def wake_ecu():
    return "AWAKE"


# Demonstrate the ECU state sequence
ecu_state = "OFF"
print("Initial state:", ecu_state)

ecu_state = start_ecu()
print("After startup:", ecu_state)

ecu_state = sleep_ecu()
print("After sleep command:", ecu_state)

ecu_state = wake_ecu()
print("After wakeup command:", ecu_state)


# Automated checks
print("\n--- ECU TEST RESULTS ---")

# Test 1: Sleep
actual_state = sleep_ecu()
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
actual_state = wake_ecu()
expected_state = "AWAKE"

if actual_state == expected_state:
    print("PASS: ECU wakeup")
else:
    print("FAIL: ECU wakeup")