import processing.serial.*;

Serial myPort;  // Create object from Serial class
float threshold = 370.0;  // Adjust this threshold according to your data

void setup() {
  size(800, 600);
  // Change "/dev/cu.usbmodemXXXX" to your Arduino's port
  myPort = new Serial(this, "/dev/cu.usbmodem1201", 9600);
}

void draw() {
  background(255);

  while (myPort.available() > 0) {
    // Read the serial data as a String
    String serialString = myPort.readStringUntil('\n');

    if (serialString != null) {
      // Trim the string and convert to float
      float sensorValue = float(trim(serialString));

      // Check the sensor value against the threshold
      if (sensorValue > threshold) {
        drawLetterA();
      } else {
        drawLetterB();
      }
    }
  }
}

void drawLetterA() {
  fill(255, 0, 0);  // Red color for "A"
  ellipse(width / 2 - 50, height / 2, 80, 80);
}

void drawLetterB() {
  fill(0, 0, 255);  // Blue color for "B"
  rectMode(CENTER);
  rect(width / 2 + 50, height / 2, 80, 80);
}
