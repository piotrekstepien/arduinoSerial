import PySimpleGUI as sg
import serial
import time


def create_window():
    layout = [
        [sg.Button("ON", key="-LED_ON-", enable_events=True), sg.Button("OFF", key="-LED_OFF-", enable_events=True),
         sg.Slider(key="-LED_VALUE-", range=(0, 255), enable_events=True, )]]
    return sg.Window("", layout, )


char = ""
ser = serial.Serial('/dev/ttyACM0', 9600)  # set port and boud rate
time.sleep(2)

window = create_window()

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    else:

        if event == "-LED_ON-":
            char = str(int(values["-LED_VALUE-"])) # Read data from slider to char
            ser.write(char.encode()) #encode to bit and send to Arduino
        if event == "-LED_OFF-":
            char = "0"
            ser.write(char.encode())
        if event == "-LED_VALUE-" and event != "LED_ON" and event != "LED_ON":
            char = str(int(values["-LED_VALUE-"]))
            ser.write(char.encode())
            #print(char.encode())

window.close()
ser.close()
