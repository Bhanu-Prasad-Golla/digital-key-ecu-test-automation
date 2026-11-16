import sys
from ecu_simulator import start_ecu, sleep_ecu, wake_ecu, power_off_ecu
from ecu_simulator import process_command
def check_result(test_name, actual, expected):
    if actual == expected:
        print(f"PASS: {test_name}")
        return True
    else:
        print(
            f"FAIL: {test_name} | "
            f"Expected: {expected} | Actual: {actual}"
        )
        return False
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

if check_result("Sleep from AWAKE", actual_state, "SLEEP"):
    passed += 1
else:
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

# Test 9: Power off an awake ECU
actual_state = power_off_ecu("AWAKE")

if actual_state == "OFF":
    print("PASS: Awake ECU powers off")
    passed += 1
else:
    print("FAIL: Awake ECU did not power off")
    failed += 1

# Test 10: Simulated power cycle
ecu_state = start_ecu()
startup_state = ecu_state

ecu_state = power_off_ecu(ecu_state)
off_state = ecu_state

ecu_state = start_ecu()

if startup_state == "AWAKE" and off_state == "OFF" and ecu_state == "AWAKE":
    print("PASS: ECU restarts after power off")
    passed += 1
else:
    print("FAIL: ECU power-cycle sequence")
    failed += 1

# Test 11: Power off a sleeping ECU
actual_state = power_off_ecu("SLEEP")

if actual_state == "OFF":
    print("PASS: Sleeping ECU powers off")
    passed += 1
else:
    print("FAIL: Sleeping ECU did not power off")
    failed += 1

# Test 12: Process a sleep command
actual_state = process_command("AWAKE", "SLEEP")

if actual_state == "SLEEP":
    print("PASS: Sleep command processed")
    passed += 1
else:
    print("FAIL: Sleep command processing")
    failed += 1


# Test 13: Unknown command keeps state unchanged
actual_state = process_command("AWAKE", "INVALID")

if actual_state == "AWAKE":
    print("PASS: Unknown command keeps state unchanged")
    passed += 1
else:
    print("FAIL: Unknown command changed state")
    failed += 1

# Test 14: Command sequence
commands = ["START", "SLEEP", "WAKE", "OFF"]
expected_states = ["AWAKE", "SLEEP", "AWAKE", "OFF"]

ecu_state = "OFF"
sequence_passed = True

for index in range(len(commands)):
    command = commands[index]
    expected_state = expected_states[index]

    ecu_state = process_command(ecu_state, command)

    print(
        f"Command: {command} | "
        f"Expected: {expected_state} | Actual: {ecu_state}"
    )

    if ecu_state != expected_state:
        sequence_passed = False

if sequence_passed:
    print("PASS: Command sequence")
    passed += 1
else:
    print("FAIL: Command sequence")
    failed += 1

# Test 15: Repeat the command sequence five times
commands = ["START", "SLEEP", "WAKE", "OFF"]
expected_states = ["AWAKE", "SLEEP", "AWAKE", "OFF"]

ecu_state = "OFF"
repeat_passed = True

for cycle in range(1, 6):
    print(f"Cycle {cycle}")

    for index in range(len(commands)):
        command = commands[index]
        expected_state = expected_states[index]

        ecu_state = process_command(ecu_state, command)

        if ecu_state != expected_state:
            print(
                f"FAIL: Cycle {cycle}, command {command}, "
                f"expected {expected_state}, actual {ecu_state}"
            )
            repeat_passed = False

if repeat_passed:
    print("PASS: All five command cycles")
    passed += 1
else:
    print("FAIL: Repeated command cycles")
    failed += 1

# Summary
total = passed + failed

print("\n--- TEST SUMMARY ---")
print("Total tests:", total)
print("Passed:", passed)
print("Failed:", failed)

# Save the summary to a report file
with open("test_report.txt", "w") as report:
    report.write("--- ECU TEST SUMMARY ---\n")
    report.write(f"Total tests: {total}\n")
    report.write(f"Passed: {passed}\n")
    report.write(f"Failed: {failed}\n")

print("Report saved to test_report.txt")

if failed > 0:
    sys.exit(1)
else:
    sys.exit(0)