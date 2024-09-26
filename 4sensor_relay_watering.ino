"""version 1.1"""
#include <RTClib.h>

RTC_DS1307 rtc;

const int relayPin1 = 3;    // Relay 1 connected to digital pin 3
const int relayPin2 = 4;    // Relay 2 connected to digital pin 4
const int relayPin3 = 5;    // Relay 3 connected to digital pin 5
const int relayPin4 = 6;    // Relay 4 connected to digital pin 6
const int rtcPowerPin = 12; // RTC module power pin connected to digital pin 12

const int wateringDuration = 10000;  // Watering duration in milliseconds (10 seconds)
const int timePrintInterval = 1000;  // Time print interval in milliseconds (1 second)
const int schedulePrintInterval = 5000;  // Schedule print interval in milliseconds (5 seconds)

unsigned long previousTimePrintMillis = 0;
unsigned long previousSchedulePrintMillis = 0;
unsigned long wateringStartTime = 0;

int waterSetHour1 = 9;    // Set the watering hour for the first time
int waterSetMinute1 = 30;  // Set the watering minute for the first time
int waterSetSecond1 = 0;   // Set the watering second for the first time

int waterSetHour2 = 15;    // Set the watering hour for the second time
int waterSetMinute2 = 30;  // Set the watering minute for the second time
int waterSetSecond2 = 0;   // Set the watering second for the second time

bool manualWateringRequested = false;
int selectedPump = 0;

void setup() {
  Serial.begin(9600);

  pinMode(relayPin1, OUTPUT);
  pinMode(relayPin2, OUTPUT);
  pinMode(relayPin3, OUTPUT);
  pinMode(relayPin4, OUTPUT);

  pinMode(rtcPowerPin, OUTPUT);
  digitalWrite(rtcPowerPin, HIGH); // Power on the RTC module

  // Initialize the RTC
  rtc.begin();

  // Set the current date and time in the format: rtc.adjust(DateTime(year, month, day, hour, minute, second));
  // rtc.adjust(DateTime(2023, 6, 29, 19, 10, 30));

  // Turn off all pumps
  stopWatering();
}

void loop() {
  DateTime now = rtc.now();

  // Check if it's the scheduled watering time (first time)
  if (now.hour() == waterSetHour1 && now.minute() == waterSetMinute1 && now.second() == waterSetSecond1) {
    startWatering();
    Serial.println("Pumps on");
  }

  // Check if it's the scheduled watering time (second time)
  if (now.hour() == waterSetHour2 && now.minute() == waterSetMinute2 && now.second() == waterSetSecond2) {
    startWatering();
    Serial.println("Pumps on");
  }

  // Check if manual watering is requested
  if (manualWateringRequested) {
    if (selectedPump == 0) {
      startWatering();
      Serial.print("Pump ");
      Serial.print(selectedPump);
      Serial.println(" on");
    } else if (selectedPump == 1) {
      startWateringForPump(relayPin1);
      Serial.print("Pump ");
      Serial.print(selectedPump);
      Serial.println(" on");
    } else if (selectedPump == 2) {
      startWateringForPump(relayPin2);
      Serial.print("Pump ");
      Serial.print(selectedPump);
      Serial.println(" on");
    } else if (selectedPump == 3) {
      startWateringForPump(relayPin3);
      Serial.print("Pump ");
      Serial.print(selectedPump);
      Serial.println(" on");
    } else if (selectedPump == 4) {
      startWateringForPump(relayPin4);
      Serial.print("Pump ");
      Serial.print(selectedPump);
      Serial.println(" on");
    }

    manualWateringRequested = false;
    selectedPump = 0;
  }

  // Check if watering duration has elapsed
  if (wateringStartTime > 0 && millis() - wateringStartTime >= wateringDuration) {
    stopWatering();
    wateringStartTime = 0;
    Serial.println("Pumps off");
  }

  // Print time every 1 second
  if (millis() - previousTimePrintMillis >= timePrintInterval) {
    printTime();
    previousTimePrintMillis = millis();
  }

  // Print schedule every 5 seconds
  if (millis() - previousSchedulePrintMillis >= schedulePrintInterval) {
    printSchedule();
    previousSchedulePrintMillis = millis();
  }

  // Check for serial input
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    if (input == "time") {
      Serial.println("Updating");
      Serial.println("New Time: ");
      while (!Serial.available()) {
        // Wait for the user to input the new time in the format: "hours minutes seconds"
      }
      int newHour = Serial.parseInt();
      while (!Serial.available()) {
        // Wait for the user to input the new time in the format: "hours minutes seconds"
      }
      int newMinute = Serial.parseInt();
      while (!Serial.available()) {
        // Wait for the user to input the new time in the format: "hours minutes seconds"
      }
      int newSecond = Serial.parseInt();

      rtc.adjust(DateTime(now.year(), now.month(), now.day(), newHour, newMinute, newSecond));
      Serial.println("Time updated");
    } else if (input == "stop") {
      stopWatering();
      Serial.println("Pumps off");
    } else if (input.startsWith("water")) {
      if (input.length() > 5) {
        int pump = input.substring(5).toInt();
        if (pump >= 0 && pump <= 4) {
          selectedPump = pump;
          manualWateringRequested = true;
        }
      }
    }
  }

  // Add any additional code or functionality here

  // Wait for a second before checking the time again
  delay(1000);
}

void startWatering() {
  digitalWrite(relayPin1, LOW);
  digitalWrite(relayPin2, LOW);
  digitalWrite(relayPin3, LOW);
  digitalWrite(relayPin4, LOW);
  wateringStartTime = millis();
}

void startWateringForPump(int pumpPin) {
  digitalWrite(pumpPin, LOW);
  wateringStartTime = millis();
}

void stopWatering() {
  digitalWrite(relayPin1, HIGH);
  digitalWrite(relayPin2, HIGH);
  digitalWrite(relayPin3, HIGH);
  digitalWrite(relayPin4, HIGH);
  wateringStartTime = 0;
}

void printTime() {
  DateTime now = rtc.now();
  Serial.print("Current Time: ");
  Serial.print(now.hour());
  Serial.print(":");
  Serial.print(now.minute());
  Serial.print(":");
  Serial.print(now.second());
  Serial.println();
}

void printSchedule() {
  Serial.println("Scheduled Watering Times:");
  printWateringTime(waterSetHour1, waterSetMinute1, waterSetSecond1);
  printWateringTime(waterSetHour2, waterSetMinute2, waterSetSecond2);
  Serial.println();
}

void printWateringTime(int hour, int minute, int second) {
  Serial.print("Watering Time: ");
  Serial.print(hour);
  Serial.print(":");
  Serial.print(minute);
  Serial.print(":");
  Serial.print(second);
  Serial.println();
}
