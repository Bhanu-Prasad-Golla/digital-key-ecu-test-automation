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