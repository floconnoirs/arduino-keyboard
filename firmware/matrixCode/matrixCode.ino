const byte ROWS = 4;
const byte COLS = 4;

byte rowPins[ROWS] = {5, 4, 3, 2};
byte colPins[COLS] = {9, 10, 11, 12};

char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};

// Track key states to prevent spamming when held down
bool keyState[ROWS][COLS] = {false}; 

void setup() {
  Serial.begin(9600);

  for (byte r = 0; r < ROWS; r++) {
    pinMode(rowPins[r], OUTPUT);
    digitalWrite(rowPins[r], HIGH);
  }

  for (byte c = 0; c < COLS; c++) {
    pinMode(colPins[c], INPUT_PULLUP);
  }
}

void loop() {
  for (byte r = 0; r < ROWS; r++) {
    digitalWrite(rowPins[r], LOW);

    for (byte c = 0; c < COLS; c++) {
      bool isPressed = (digitalRead(colPins[c]) == LOW);

      // Trigger action only when first pressed down
      if (isPressed && !keyState[r][c]) {
        Serial.println(keys[r][c]); // Send key character to Python
        keyState[r][c] = true;
        delay(20); // Basic debounce
      } 
      else if (!isPressed && keyState[r][c]) {
        keyState[r][c] = false; // Reset state when released
      }
    }

    digitalWrite(rowPins[r], HIGH);
  }
}