import sys
from ecu_simulator import start_ecu, sleep_ecu, wake_ecu

passed = 0
failed = 0

# Test 1: Startup
actual_state = start_ecu()

if actual_state == "AWAKE":
    print("PASS: ECU startup")
    passed += 1
else:
    print("FAIL: ECU startup")
    failed += 1

# Test 2: Sleep from AWAKE
actual_state = sleep_ecu("AWAKE")

if actual_state == "SLEEP":
    print("PASS: Awake ECU enters sleep")
    passed += 1
else:
    print("FAIL: Awake ECU did not enter sleep")
    failed += 1

# Test 3: Wakeup from SLEEP
actual_state = wake_ecu("SLEEP")

if actual_state == "AWAKE":
    print("PASS: Sleeping ECU wakes up")
    passed += 1
else:
    print("FAIL: Sleeping ECU did not wake up")
    failed += 1

# Test 4: Sleep while OFF
actual_state = sleep_ecu("OFF")

if actual_state == "OFF":
    print("PASS: Sleep command keeps OFF ECU OFF")
    passed += 1
else:
    print("FAIL: Sleep command changed OFF ECU")
    failed += 1

# Test 5: Wakeup while OFF
actual_state = wake_ecu("OFF")

if actual_state == "OFF":
    print("PASS: Wakeup command keeps OFF ECU OFF")
    passed += 1
else:
    print("FAIL: Wakeup command changed OFF ECU")
    failed += 1

# Test 6: Complete startup, sleep, and wakeup sequence
ecu_state = start_ecu()
print("Sequence - startup:", ecu_state)

ecu_state = sleep_ecu(ecu_state)
print("Sequence - sleep:", ecu_state)

sleep_state = ecu_state

ecu_state = wake_ecu(ecu_state)
print("Sequence - wakeup:", ecu_state)

if sleep_state == "SLEEP" and ecu_state == "AWAKE":
    print("PASS: Complete sleep and wakeup sequence")
    passed += 1
else:
    print("FAIL: Complete sleep and wakeup sequence")
    failed += 1
# Test 7: Sleep command while already sleeping
actual_state = sleep_ecu("SLEEP")

if actual_state == "SLEEP":
    print("PASS: Repeated sleep keeps ECU sleeping")
    passed += 1
else:
    print("FAIL: Repeated sleep changed ECU state")
    failed += 1


# Test 8: Wakeup command while already awake
actual_state = wake_ecu("AWAKE")

if actual_state == "AWAKE":
    print("PASS: Repeated wakeup keeps ECU awake")
    passed += 1
else:
    print("FAIL: Repeated wakeup changed ECU state")
    failed += 1

# Summary
total = passed + failed

print("\n--- TEST SUMMARY ---")
print("Total tests:", total)
print("Passed:", passed)
print("Failed:", failed)

if failed > 0:
    sys.exit(1)
else:
    sys.exit(0)