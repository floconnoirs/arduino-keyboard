import serial
import time
import pyautogui

# Set to your Arduino port (e.g., 'COM3' on Windows or '/dev/cu.usbmodem14101' on Mac)
SERIAL_PORT = 'COM4' 
BAUD_RATE = 9600

# Map keypad characters to PyAutoGUI key names or macros
KEY_MAP = {
    '1': '1', '2': '2', '3': '3', 'A': 'up',
    '4': '4', '5': '5', '6': '6', 'B': 'down',
    '7': '7', '8': '8', '9': '9', 'C': 'left',
    '*': 'backspace', '0': '0', '#': 'enter', 'D': 'right'
}

try:
    arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2) # Wait for serial connection to initialize
    print(f"Connected to Keypad on {SERIAL_PORT}! Press any key...")

    while True:
        if arduino.in_waiting > 0:
            # Read character sent from Arduino matrix scan
            pressed_key = arduino.readline().decode('utf-8').strip()
            
            if pressed_key in KEY_MAP:
                action = KEY_MAP[pressed_key]
                print(f"Keypad: '{pressed_key}' -> Keyboard: '{action}'")
                
                # Execute keypress
                pyautogui.press(action)

except serial.SerialException:
    print(f"Error: Could not open {SERIAL_PORT}. Ensure Serial Monitor in Arduino IDE is CLOSED.")
except KeyboardInterrupt:
    print("\nScript stopped.")
