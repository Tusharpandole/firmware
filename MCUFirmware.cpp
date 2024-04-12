#include <EEPROM.h>

#define BAUD_RATE 2400
#define EEPROM_SIZE 1000

void setup() {
  Serial.begin(BAUD_RATE);
}

void loop() {
  if (Serial.available() > 0) {
    // Data receiving from PC
    unsigned long startTime = millis();
    int dataIndex = 0;
    
    while (Serial.available() && dataIndex < EEPROM_SIZE) {
      char receivedChar = Serial.read();
      EEPROM.write(dataIndex, receivedChar);
      dataIndex++;
    }

    unsigned long endTime = millis();
    unsigned long duration = endTime - startTime;
    float bitsTransferred = dataIndex * 10; // Each character is 10 bits (8 data bits + 1 start bit + 1 stop bit)
    float transferSpeed = (bitsTransferred * 1000.0) / duration; // in bits per second

    Serial.print("Received ");
    Serial.print(dataIndex);
    Serial.print(" bytes in ");
    Serial.print(duration);
    Serial.print(" ms, Speed: ");
    Serial.print(transferSpeed);
    Serial.println(" bits/s");

    // Data sending back to PC
    for (int i = 0; i < dataIndex; i++) {
      char readChar = EEPROM.read(i);
      Serial.write(readChar);
    }
  }
}
