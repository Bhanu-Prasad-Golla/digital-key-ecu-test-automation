from ecu_simulator import start_ecu, sleep_ecu, wake_ecu


# Test 1: Start the ECU
actual_state = start_ecu()

if actual_state == "AWAKE":
    print("PASS: ECU startup")
else:
    print("FAIL: ECU startup")


# Test 2: Put an awake ECU to sleep
actual_state = sleep_ecu("AWAKE")

if actual_state == "SLEEP":
    print("PASS: Awake ECU enters sleep")
else:
    print("FAIL: Awake ECU did not enter sleep")


# Test 3: Wake a sleeping ECU
actual_state = wake_ecu("SLEEP")

if actual_state == "AWAKE":
    print("PASS: Sleeping ECU wakes up")
else:
    print("FAIL: Sleeping ECU did not wake up")


# Test 4: Sleep command must keep an OFF ECU OFF
actual_state = sleep_ecu("OFF")

if actual_state == "OFF":
    print("PASS: Sleep command keeps OFF ECU OFF")
else:
    print("FAIL: Sleep command changed OFF ECU")


# Test 5: Wakeup command must keep an OFF ECU OFF
actual_state = wake_ecu("OFF")

if actual_state == "OFF":
    print("PASS: Wakeup command keeps OFF ECU OFF")
else:
    print("FAIL: Wakeup command changed OFF ECU")