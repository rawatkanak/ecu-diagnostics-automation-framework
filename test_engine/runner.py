import json
import csv
import time

from fault_detection.fault_engine import detect_faults


def evaluate(actual, operator, expected):

    if operator == "<":
        return actual < expected

    elif operator == ">":
        return actual > expected

    elif operator == ">=":
        return actual >= expected

    elif operator == "<=":
        return actual <= expected

    elif operator == "==":
        return actual == expected

    return False


def run_tests():

    while True:

        # LOAD TEST CASES
        with open("test_engine/test_cases.json") as file:
            test_cases = json.load(file)

        # LOAD LIVE ECU DATA
        with open("logs/live_ecu_data.json") as ecu_file:
            ecu_data = json.load(ecu_file)

        print("\n==============================")
        print("     LIVE ECU DATA")
        print("==============================")
        print(ecu_data)

        # DETECT FAULTS
        faults = detect_faults(ecu_data)

        # SAVE FAULTS
        with open("logs/faults.json", "w") as fault_file:
            json.dump(faults, fault_file, indent=4)

        print("\n==============================")
        print("      FAULT DETECTION")
        print("==============================")

        if faults:

            for fault in faults:

                print(f"[{fault['severity']}] {fault['message']}")

        else:

            print("NO FAULTS DETECTED")

        print("\n==============================")
        print("       TEST RESULTS")
        print("==============================\n")

        # SAVE LOGS
        with open("logs/system_logs.csv", "a", newline="") as logfile:

            writer = csv.writer(logfile)

            # WRITE HEADER
            if logfile.tell() == 0:

                writer.writerow([
                    "Test Name",
                    "Parameter",
                    "Actual Value",
                    "Operator",
                    "Expected Value",
                    "Status"
                ])

            # RUN TESTS
            for test in test_cases:

                parameter = test["parameter"]
                operator = test["operator"]
                expected = test["value"]

                actual = ecu_data[parameter]

                result = evaluate(actual, operator, expected)

                status = "PASS" if result else "FAIL"

                print(f"{test['name']} --> {status}")

                # SAVE CSV
                writer.writerow([
                    test["name"],
                    parameter,
                    actual,
                    operator,
                    expected,
                    status
                ])

        print("\n==============================")
        print("   LOGS SAVED SUCCESSFULLY")
        print("==============================")

        # WAIT 2 SECONDS
        time.sleep(2)


if __name__ == "__main__":
    run_tests()