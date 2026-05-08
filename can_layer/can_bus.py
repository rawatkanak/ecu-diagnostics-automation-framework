import can

bus = can.interface.Bus(
    interface='virtual',
    channel='vcan0'
)


def send_can_message(rpm, temperature):

    message = can.Message(
        arbitration_id=0x101,
        data=[rpm % 256, temperature],
        is_extended_id=False
    )

    bus.send(message)

    print(f"Sent CAN Message: {message}")


def receive_can_message():

    message = bus.recv(timeout=1)

    if message:
        print(f"Received CAN Message: {message}")

    return message