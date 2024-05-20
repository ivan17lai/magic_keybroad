#include <Wire.h>
#include "Adafruit_MPR121.h"

#define MPR121_ADDR 0x5A

#define SLAVE_ADD 0x70 //tca9548a的id
#define VOLTADE_ADD 0x5A //後面那顆ic的id

Adafruit_MPR121 cap = Adafruit_MPR121();

int baseValue[12];



void PCA9548A(uint8_t bus){
  Wire.beginTransmission(0x70);  // TCA9548A address is 0x70
  Wire.write(1 << bus);          // send byte to select bus
  Wire.endTransmission();
}



void setup() {
  
  Wire.begin();

  Serial.begin(115200);
  while (!Serial);
  
  Serial.println("MPR121 test!");

  if (!cap.begin(MPR121_ADDR)) {
    Serial.println("MPR121 not found, check wiring?");
    while (1);
  }
  Serial.println("MPR121 found!");
  Serial.println("setup...");


  delay(1000);

  for (uint8_t i = 0; i < 12; i++) {
    uint16_t touchVal = cap.filteredData(i);
    Serial.print("Channel ");
    Serial.print(i);
    Serial.print(": ");
    Serial.println(touchVal);
    baseValue[i] = touchVal;
  }

  Serial.println("done!");


}


int change_max =6;


void loop() {
  

  PCA9548A(0);
  Serial.print("c0");
  for (uint8_t i = 0; i < 12; i++) {
    uint16_t touchVal = cap.filteredData(i);
    if (abs(touchVal-baseValue[i]) > change_max){
      Serial.print("T");
    }else{
      Serial.print("/");
    }
    //Serial.print(touchVal);
    Serial.print(",");
  }
  Serial.print(" ");


  PCA9548A(5);
    Serial.print(" c1");

  for (uint8_t i = 0; i < 12; i++) {
    uint16_t touchVal = cap.filteredData(i);
    // if (abs(touchVal-baseValue[i]) > change_max){
    //   Serial.print("T");
    // }else{
    //   Serial.print("/");
    // }
    Serial.print(touchVal);

    Serial.print(",");
  }
  Serial.println(" ");



  // PCA9548A(2);
  //   Serial.print(" c2");

  // for (uint8_t i = 0; i < 12; i++) {
  //   uint16_t touchVal = cap.filteredData(i);
  //   if (abs(touchVal-baseValue[i]) > change_max){
  //     Serial.print("T");
  //   }else{
  //     Serial.print("/");
  //   }
  //   Serial.print(",");
  // }
  //     Serial.print(" ");


  // PCA9548A(3);
  //   Serial.print(" c3");

  // for (uint8_t i = 0; i < 12; i++) {
  //   uint16_t touchVal = cap.filteredData(i);
  //   if (abs(touchVal-baseValue[i]) > change_max){
  //     Serial.print("T");
  //   }else{
  //     Serial.print("/");
  //   }
  //   Serial.print(",");
  // }
  //     Serial.println(" ");



  delay(200);
  
}