PulseDet = 0
basic.show_string("\"Puls__\"")

def on_forever():
    pulse_out = 0
    basic.show_number(pulse_out)
    basic.show_icon(IconNames.HEART)
basic.forever(on_forever)

def on_forever2():
    global PulseDet
    PulseDet = pins.analog_read_pin(AnalogPin.P2)
basic.forever(on_forever2)

def on_forever3():
    serial.write_value("Pulse diagram", PulseDet)
basic.forever(on_forever3)
