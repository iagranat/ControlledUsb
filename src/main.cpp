#include <Arduino.h>
#include <Adafruit_NeoPixel.h>

// ================= Pin Definitions =================
#define PIN_RGB_LED    16  // Onboard WS2812 on RP2040-Zero
#define PIN_PWR_EN     14  // TPS22918 Enable (Active HIGH: 1 = 5V ON, 0 = 0V OFF)
#define PIN_DATA_OE    15  // CH440G Enable   (Active LOW:  0 = Data ON, 1 = Hi-Z Cut)
#define PIN_BUTTON     26  // Tactile push button to GND (moved to GP26 on active row)

// NeoPixel Configuration (1 on-board pixel)
Adafruit_NeoPixel rgb(1, PIN_RGB_LED, NEO_GRB + NEO_KHZ800);

// ================= State Machine =================
enum PortState {
  STATE_CONNECTED,
  STATE_DISCONNECTED,
  STATE_CHARGE_ONLY,
  STATE_CYCLING
};

PortState currentState = STATE_CONNECTED;

// Timing & Blinking
unsigned long cycleStartTime = 0;
unsigned long cycleDurationMs = 1000;
unsigned long lastBlinkTime = 0;
bool blinkState = false;

// Button Debouncing & Long-Press Detection
int lastButtonReading = HIGH;
int buttonState = HIGH;
unsigned long lastDebounceTime = 0;
unsigned long buttonPressStartTime = 0;
const unsigned long debounceDelay = 50;
const unsigned long longPressThreshold = 1200; // 1.2s triggers power cycle

// ================= LED Color Helper =================

void setRgb(uint8_t r, uint8_t g, uint8_t b) {
  rgb.setPixelColor(0, rgb.Color(r, g, b));
  rgb.show();
}

void updateLedState() {
  switch (currentState) {
    case STATE_CONNECTED:
      setRgb(0, 45, 0);     // 🟢 Solid Green
      break;

    case STATE_DISCONNECTED:
      setRgb(45, 0, 0);     // 🔴 Solid Red
      break;

    case STATE_CHARGE_ONLY:
      setRgb(0, 0, 45);     // 🔵 Solid Blue
      break;

    case STATE_CYCLING:
      // 🟡 Blinking Yellow during reboot
      if (millis() - lastBlinkTime > 120) {
        lastBlinkTime = millis();
        blinkState = !blinkState;
        if (blinkState) {
          setRgb(45, 35, 0); // Yellow ON
        } else {
          setRgb(0, 0, 0);   // OFF
        }
      }
      break;
  }
}

// ================= Switching Logic =================

// Safe Reconnect: Turn on Power first, then connect Data lines
void connectPort() {
  digitalWrite(PIN_PWR_EN, HIGH); // 1. Turn on 5V VBUS
  delay(30);                      // 2. Wait 30ms for downstream caps to charge
  digitalWrite(PIN_DATA_OE, LOW); // 3. Connect D+/D- data lines (Active LOW)
  currentState = STATE_CONNECTED;
  updateLedState();
  Serial.println("OK: CONNECTED (VBUS=ON, DATA=ON)");
}

// Safe Disconnect: Cut Data lines first, then cut Power
void disconnectPort() {
  digitalWrite(PIN_DATA_OE, HIGH); // 1. Tri-state D+/D- first to prevent back-powering!
  delay(5);                        // 2. Micro-gap
  digitalWrite(PIN_PWR_EN, LOW);   // 3. Cut VBUS to 0V (TPS22918 quick discharge bleeds rail)
  currentState = STATE_DISCONNECTED;
  updateLedState();
  Serial.println("OK: DISCONNECTED (VBUS=OFF, DATA=OFF)");
}

// Charge Only: Power ON, Data lines cut
void chargeOnlyPort() {
  digitalWrite(PIN_DATA_OE, HIGH); // Cut data
  digitalWrite(PIN_PWR_EN, HIGH);  // Keep 5V active
  currentState = STATE_CHARGE_ONLY;
  updateLedState();
  Serial.println("OK: CHARGE_ONLY (VBUS=ON, DATA=OFF)");
}

// Automated Cycle (Reboot)
void startCycle(unsigned long durationMs) {
  cycleDurationMs = durationMs;
  cycleStartTime = millis();

  // Cut both lines safely
  digitalWrite(PIN_DATA_OE, HIGH);
  delay(5);
  digitalWrite(PIN_PWR_EN, LOW);

  currentState = STATE_CYCLING;
  updateLedState();
  Serial.printf("OK: CYCLING (Rebooting port for %lu ms)...\n", durationMs);
}

// ================= Serial CLI Parser =================

void processSerialCommand(String cmd) {
  cmd.trim();
  cmd.toUpperCase();

  if (cmd.length() == 0) return;

  if (cmd == "ON" || cmd == "CONNECT" || cmd == "1") {
    connectPort();
  } 
  else if (cmd == "OFF" || cmd == "DISCONNECT" || cmd == "0") {
    disconnectPort();
  } 
  else if (cmd == "CHARGE") {
    chargeOnlyPort();
  } 
  else if (cmd.startsWith("CYCLE")) {
    int spaceIndex = cmd.indexOf(' ');
    unsigned long duration = 1000;
    if (spaceIndex != -1) {
      long val = cmd.substring(spaceIndex + 1).toInt();
      if (val > 0) duration = (unsigned long)val;
    }
    startCycle(duration);
  } 
  else if (cmd == "STATUS" || cmd == "?") {
    Serial.print("STATUS: ");
    switch (currentState) {
      case STATE_CONNECTED:    Serial.println("CONNECTED [VBUS=1, DATA=1]"); break;
      case STATE_DISCONNECTED: Serial.println("DISCONNECTED [VBUS=0, DATA=0]"); break;
      case STATE_CHARGE_ONLY:  Serial.println("CHARGE_ONLY [VBUS=1, DATA=0]"); break;
      case STATE_CYCLING:      Serial.printf("CYCLING [Remaining: %lu ms]\n", 
                                  (millis() - cycleStartTime < cycleDurationMs) ? 
                                  (cycleDurationMs - (millis() - cycleStartTime)) : 0); break;
    }
  } 
  else if (cmd == "HELP") {
    Serial.println("==========================================");
    Serial.println("  Controlled USB Extension Commands:");
    Serial.println("    ON / CONNECT     - Enable Power & Data");
    Serial.println("    OFF / DISCONNECT - Cut Power & Data");
    Serial.println("    CHARGE           - Power ON, Data OFF");
    Serial.println("    CYCLE <ms>       - Power cycle (e.g. CYCLE 1000)");
    Serial.println("    STATUS / ?       - Query current state");
    Serial.println("==========================================");
  } 
  else {
    Serial.printf("ERR: Unknown command '%s'. Type HELP for command list.\n", cmd.c_str());
  }
}

// ================= Button Handler =================

void handleButton() {
  int reading = digitalRead(PIN_BUTTON);

  if (reading != lastButtonReading) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != buttonState) {
      buttonState = reading;

      // Button Pressed (LOW)
      if (buttonState == LOW) {
        buttonPressStartTime = millis();
      } 
      // Button Released (HIGH)
      else {
        unsigned long pressDuration = millis() - buttonPressStartTime;
        if (pressDuration >= longPressThreshold) {
          Serial.println("[Button] Long press -> Triggering 1s cycle");
          startCycle(1000);
        } else {
          // Short click -> Toggle between Connected and Disconnected
          if (currentState == STATE_CONNECTED) {
            Serial.println("[Button] Click -> Disconnecting");
            disconnectPort();
          } else {
            Serial.println("[Button] Click -> Connecting");
            connectPort();
          }
        }
      }
    }
  }
  lastButtonReading = reading;
}

// ================= Setup & Main Loop =================

void setup() {
  // Initialize Hardware Pins
  pinMode(PIN_PWR_EN, OUTPUT);
  pinMode(PIN_DATA_OE, OUTPUT);
  pinMode(PIN_BUTTON, INPUT_PULLUP);

  // Initialize Onboard WS2812 RGB LED
  rgb.begin();
  rgb.setBrightness(50); // Comfortable brightness

  // Default Boot State: CONNECTED
  connectPort();

  // Initialize Native USB CDC Serial
  Serial.begin(115200);

  // Wait up to 2 seconds for USB terminal to open
  unsigned long start = millis();
  while (!Serial && (millis() - start < 2000));

  Serial.println("\n==========================================");
  Serial.println("Controlled USB Extension Switch (RP2040)");
  Serial.println("Default State: CONNECTED");
  Serial.println("Type HELP for available commands.");
  Serial.println("==========================================");
}

void loop() {
  // 1. Process Serial CLI commands
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    processSerialCommand(input);
  }

  // 2. Non-blocking cycle completion
  if (currentState == STATE_CYCLING) {
    if (millis() - cycleStartTime >= cycleDurationMs) {
      connectPort();
    }
  }

  // 3. Physical button checks
  handleButton();

  // 4. Update RGB LED animations
  updateLedState();
}
