import streamlit as st
import json
import time

st.set_page_config(
    page_title="ECU Monitoring Dashboard",
    layout="wide"
)

st.title("🚗 ECU Monitoring Dashboard")

placeholder = st.empty()

while True:

    # LOAD ECU DATA
    try:

        with open("logs/live_ecu_data.json", "r") as file:
            data = json.load(file)

    except:

        data = {
            "rpm": 0,
            "temperature": 0,
            "voltage": 0
        }

    # LOAD FAULTS
    try:

        with open("logs/faults.json", "r") as file:
            faults = json.load(file)

    except:

        faults = []

    with placeholder.container():

        st.subheader("📡 Live ECU Data")

        col1, col2, col3 = st.columns(3)

        col1.metric("RPM", data["rpm"])
        col2.metric("Temperature", data["temperature"])
        col3.metric("Voltage", data["voltage"])

        st.divider()

        st.subheader("🚨 Fault Detection")

        if faults:

            for fault in faults:

                severity = fault["severity"]
                message = fault["message"]

                if severity == "CRITICAL":

                    st.error(f"{severity}: {message}")

                else:

                    st.warning(f"{severity}: {message}")

        else:

            st.success("✅ No Faults Detected")

    time.sleep(2)