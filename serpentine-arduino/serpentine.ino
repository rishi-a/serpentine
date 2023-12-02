void setup() {
  Serial.begin(9600); // Initialize Serial communication
}

void loop() {
  int sensorValue = analogRead(A0); // Read analog input from A0
  Serial.println(sensorValue);     // Print the sensor value to the Serial Monitor
  delay(5);                    // 100 works
}
