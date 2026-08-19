# arduino-keyboard

4x4 Keyboard Matrix build on an Arduino Uno, with a Python bridge script that
turns keypad presses into keyboard shortcuts on your desktop.

![Keyboard Matrix Layout](hardware/wiring/matrixMap.svg)

## Repo structure

```
arduino-keyboard/
├── firmware/
│   └── matrixCode/        # Arduino sketch (.ino) that scans the matrix and
│                           # writes the pressed key over Serial — NEEDS RE-UPLOAD
├── hardware/
│   ├── printed-base/      # 3D-print files for the enclosure — NEEDS RE-UPLOAD
│   └── wiring/
│       └── matrixMap.svg  # matrix layout / wiring diagram
├── software/
│   └── ArduinoIDE_to_Desktop.py  # reads Serial from the Arduino and maps
│                                   # keypad presses to keystrokes via PyAutoGUI
├── .gitattributes
├── .gitignore
└── README.md
```

## How it works

1. The Arduino Uno (running the sketch in `firmware/matrixCode/`) scans the
   4x4 matrix keypad and prints the pressed character over Serial.
2. `software/ArduinoIDE_to_Desktop.py` listens on that Serial port and maps
   each key to a keyboard action (numbers, arrow keys, backspace, enter) via
   PyAutoGUI.

## Setup

1. Flash the Arduino with the sketch from `firmware/matrixCode/`.
2. Close the Arduino IDE's Serial Monitor (it will lock the port).
3. Install dependencies: `pip install pyserial pyautogui`
4. Edit `SERIAL_PORT` in `software/ArduinoIDE_to_Desktop.py` to match your
   Arduino's port (e.g. `COM4` on Windows, `/dev/cu.usbmodemXXXX` on Mac).
5. Run: `python software/ArduinoIDE_to_Desktop.py`

## ⚠️ Missing content

Three items from the original upload came through as empty (0-byte) files —
this happens when folders are dragged in but only individual files transfer.
Placeholders with notes were added at:

- `firmware/matrixCode/PLACEHOLDER.md`
- `hardware/printed-base/PLACEHOLDER.md`
- `hardware/wiring/PLACEHOLDER.md`

Re-add the real files from your local machine into those folders, then
delete the placeholder notes.
