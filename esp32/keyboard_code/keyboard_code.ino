#include <Wire.h>
#include "Adafruit_MPR121.h"

#define MPR121_ADDR 0x5A

Adafruit_MPR121 cap = Adafruit_MPR121();

int baseValue[6][12];

void PCA9548A(uint8_t bus){
  Wire.beginTransmission(0x70);  // TCA9548A address is 0x70
  Wire.write(1 << bus);          // send byte to select bus
  Wire.endTransmission();
}


void setup() {
  
  Wire.begin();
  PCA9548A(0);

  Serial.begin(115200);
  while (!Serial);
  
  Serial.println("MPR121 test!");




  for(int n=0;n<6;n++){

    PCA9548A(n);

    if (!cap.begin(MPR121_ADDR)) {
      Serial.println("MPR121 not found, check wiring?");
      while (1);
    }
    Serial.println("MPR121 found!");
    Serial.println("setup...");

    delay(200);

    for (uint8_t i = 0; i < 12; i++) {
      uint16_t touchVal = cap.filteredData(i);
      Serial.print("Channel ");
      Serial.print(i);
      Serial.print(": ");
      Serial.println(touchVal);
      baseValue[n][i] = touchVal;
    }
  }

  Serial.println("done!");

}


int change_max =7;
String bit_data;

void loop() {
  
  for(int n=0;n<6;n++){
    PCA9548A(n);
    //Serial.print("c");
    //Serial.print(n);
    //Serial.print(":");
    for (uint8_t i = 0; i < 12; i++) {
      uint16_t touchVal = cap.filteredData(i);
      if (abs(touchVal-baseValue[n][i]) > change_max){
        bit_data += '1';
        //Serial.print("T");
      }else{
        bit_data += '0';
        //Serial.print("/");
      }
      //Serial.print(touchVal);
      //Serial.print(",");
    }
    //bit_data += '/';
    //Serial.print(" ");

  }
  Serial.println( (bit_data) );
  bit_data = "";

}