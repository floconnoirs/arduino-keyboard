import serial
import time
import pyautogui

# Set your Arduino port name and baud rate
# Windows: 'COM3', 'COM4', etc.
# Mac/Linux: '/dev/cu.usbmodem14101' or '/dev/ttyUSB0'
SERIAL_PORT = 'COM3' 
BAUD_RATE = 9600

try:
    arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2) # Wait for serial connection to stabilize
    print(f"Connected to Arduino on {SERIAL_PORT}! Press your button...")

    while True:
        if arduino.in_waiting > 0:
            # Read line sent from Arduino and strip whitespace
            message = arduino.readline().decode('utf-8').strip()
            
            # Map Arduino messages to keypresses
            if message == "KEY_SPACE":
                print("Button Pressed -> Simulating SPACEBAR")
                pyautogui.press('space')
            
            elif message == "KEY_ENTER":
                pyautogui.press('enter')

except serial.SerialException:
    print(f"Could not open port {SERIAL_PORT}. Make sure the Arduino IDE Serial Monitor is closed!")
except KeyboardInterrupt:
    print("\nProgram stopped.")
