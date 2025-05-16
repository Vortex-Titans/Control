#include <SPI.h>
#include <Ethernet.h>
#include <Wire.h>
#include <Servo.h>
#include <MPU6050_tockn.h>                                                                    //added this library
#include "MS5837.h"

                                                                                              //remove that library


MS5837 sensor;

//MPU6050 mpu6050(Wire);
// Create a Servo object to control the ESC
Servo thruster1;
Servo thruster2;
Servo thruster3;
Servo thruster4;
#define PH_pin A10   // ph sensor pin define                                                   
#define LEAK_pin 48  //lesk sensor pin define

//#define DE_RE 23
MPU6050 mpu6050(Wire);                                                                         //mpu6050 initialised

#define W5500_RESET_PIN 44  // Define a reset pin for the W5500

// Pin Definitions
const int bilgePwmPins[4] = { 7, 8, 9, 11 };
const int bilgeControlPins[4] = { 25, 23, 20, 21 };
const int gripper1Pin = 39;
const int gripper2Pin = 45;
const int suctionTool = 35;

// Ethernet settings
byte mac[] = { 0x02, 0xAB, 0xCD, 0xEF, 0x12, 0x34 };
IPAddress ip(192, 168, 33, 100);
IPAddress server(192, 168, 33, 1);
EthernetClient client;
const int serverPort = 1222;

unsigned long lastSendTime = 0;          // Store the last send time
const unsigned long sendInterval = 500;  // Send data every 500ms

void setup() {
  Serial.begin(115200);
//  pinMode(DE_RE, OUTPUT);
//  digitalWrite(DE_RE, LOW); // Receive mode
    Wire.begin();
   
                                                                                                        //remove this comments
 
   

  mpu6050.begin();        
  mpu6050.calcGyroOffsets(true);                                                                     //added this function
  thruster1.attach(2);
  thruster2.attach(3);
  thruster3.attach(4);
  thruster4.attach(22);
  
  pinMode(W5500_RESET_PIN, OUTPUT);
  digitalWrite(W5500_RESET_PIN, HIGH);  // Ensure it's not resetting initially

  // Initialize pins
  for (int i = 0; i < 4; i++) {
    pinMode(bilgePwmPins[i], OUTPUT);
    pinMode(bilgeControlPins[i], OUTPUT);
  }
  pinMode(gripper1Pin, OUTPUT);
  pinMode(gripper2Pin, OUTPUT);
  pinMode(suctionTool, OUTPUT);

  // IMU INTIALIZATION
//  mpu6050.begin();
  Serial.println("hello");

//  Serial.println("hello");
  // mpu6050.calcGyroOffsets(true);

  resetEthernet();  // Reset the W5500 before starting
  connectToServer();
}

void loop() {
  Ethernet.maintain();

  // delay(500);
  if (!client.connected() || Ethernet.linkStatus() == 2) {
    Serial.println("Lost connection to server. Reconnecting...");
     resetEthernet();
    reconnectToServer();
    // Serial.println("Done");
  }

  while (client.available()) {
    String receivedData = client.readStringUntil('\n');
    // Serial.print("Received from server: ");
     Serial.println(receivedData);
    if (receivedData.length() != 35) continue;
    moveAll(receivedData);
    delay(50);
    // delay(1000);
  }
  sendSensorsData();
  delay(50);
  // Serial.println("Im out");
}

// Function to reset the W5500 module
void resetEthernet() {
  Serial.println("Resetting W5500...");
  digitalWrite(W5500_RESET_PIN, LOW);
  delay(500);
  digitalWrite(W5500_RESET_PIN, HIGH);
  delay(500);
  Ethernet.begin(mac, ip);
  Serial.print("New IP: ");
  Serial.println(Ethernet.localIP());
}

// Function to connect to the server
void connectToServer() {
  Serial.print("Connecting to server... ");
  Ethernet.begin(mac, ip);
  delay(1000);
  while(1){
     if (client.connect(server, serverPort)) {
    Serial.println("Connected!");
    Serial.println(Ethernet.localIP());
    break;
  } else {
     Serial.println(Ethernet.localIP());
    Serial.println("Connection failed.");
  }
  }
 
}

// Function to reconnect if connection is lost
void reconnectToServer() {
  client.stop();
  delay(1000);  // Small delay to prevent rapid retries
  if (!client.connect(server, serverPort)) {
    Serial.println("Retrying connection...");
    resetEthernet();
    delay(500);
  }
  // Serial.println("Reconnected!");
}
  String formatIMU(int angle) {
    String str = String(angle);
    if (angle >= 0) str = "+" + str;                                 // Ensure positive numbers have '+'
    while (str.length() < 4) str = str[0] + "0" + str.substring(1);  // Ensure 4 chars
    return str;
  }

void sendSensorsData() {
  // if (millis() - lastSendTime < sendInterval) {
  //   return;  // Exit function if not enough time has passed
  // }
  // lastSendTime = millis();  // Update last send time

  int analogValue = analogRead(PH_pin);                                    //remove that variable
  float voltage = analogValue * (5.0 / 1023.0);
  float PH = (3.5 * voltage);

  // Read IMU data

  mpu6050.update();

 float angle_z = mpu6050.getAngleZ();
 String angleZ = formatIMU(int(angle_z));

  

  String readings;
  if (PH <= 9 && sensor.depth()<0) {
    readings = "0" + String(PH, 2) + String(sensor.depth(), 2) + String(angleZ, 0);
  } else if  (PH <= 9 && sensor.depth()>=0){
    readings ="0"+ String(PH, 2) +"0" +String(sensor.depth(), 2) + String(angleZ, 0);
  }else if (PH > 9 && sensor.depth()<0){
     readings = String(PH, 2) + String(sensor.depth(), 2) + String(angleZ, 0);
  }else if (PH > 9 && sensor.depth()>=0){
    readings = String(PH, 2) +"0"+ String(sensor.depth(), 2) + String(angleZ, 0);
  }                                                     //remove these comments

 
  Serial.println(readings);
  client.print(readings);
}

void moveThrusters(String message) {
  String thruster1Val = message.substring(0, 4);
  String thruster2Val = message.substring(4, 8);
  String thruster3Val = message.substring(8,12);
  String thruster4Val = message.substring(12,16);
  String servoToolVal = message.substring(26, 29);

  thruster1.writeMicroseconds(thruster1Val.toInt());
  thruster2.writeMicroseconds(thruster2Val.toInt());
  thruster3.writeMicroseconds(thruster3Val.toInt());
  thruster4.writeMicroseconds(thruster4Val.toInt());
}

void moveBilges(String message) {
  Serial.println(message);
  for (int i = 0; i < 4; i++) {
    String bilgePwmVal = message.substring(16 + i * 4, 19 + i * 4);
    String bilgeControlVal = message.substring(19 + i * 4, 20 + i * 4);
    analogWrite(bilgePwmPins[i], bilgePwmVal.toInt());
    digitalWrite(bilgeControlPins[i], bilgeControlVal.toInt());
  

  }
}

void moveGrippers(String message) {
  String gripper1Val = message.substring(32, 33);
  String gripper2Val = message.substring(33, 34);
  String suctionToolVal = message.substring(34,35);
  Serial.println(suctionToolVal);
//  String suctionToolVal = message.substring(30,31);
  digitalWrite(gripper1Pin, gripper1Val.toInt());
  digitalWrite(gripper2Pin, gripper2Val.toInt());
  digitalWrite(suctionTool, suctionToolVal.toInt());
  
}

void moveAll(String message) {
  if (message.length() != 35) return;
  Serial.println("wslt");
  moveThrusters(message);
  moveBilges(message);
  moveGrippers(message);
}