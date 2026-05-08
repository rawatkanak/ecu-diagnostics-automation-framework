from flask import Flask, jsonify

from ecu_simulator.ecu import generate_ecu_data

app = Flask(__name__)


@app.route("/ecu-status")
def ecu_status():

    data = generate_ecu_data()

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)