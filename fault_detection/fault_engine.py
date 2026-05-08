def detect_faults(ecu_data):

    faults = []

    # OVERHEAT CHECK
    if ecu_data["temperature"] > 110:

        faults.append({
            "severity": "CRITICAL",
            "message": "ENGINE OVERHEAT DETECTED"
        })

    # LOW VOLTAGE CHECK
    if ecu_data["voltage"] < 11.5:

        faults.append({
            "severity": "WARNING",
            "message": "LOW BATTERY VOLTAGE"
        })

    # LOW RPM CHECK
    if ecu_data["rpm"] < 800:

        faults.append({
            "severity": "WARNING",
            "message": "ENGINE STALL RISK"
        })

    return faults