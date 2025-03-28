#include <SPI.h>
#include <Ethernet.h>
#include <Wire.h>
#include <Servo.h>
#include "MS5837.h"
#include <MPU6050_tockn.h>

MS5837 sensor;

MPU6050 mpu6050(Wire);
// Create a Servo object to control the ESC
Servo thruster1;
Servo thruster2;

#define PH_pin A10   // ph sensor pin define
#define LEAK_pin 48  //lesk sensor pin define

#define W5500_RESET_PIN 44  // Define a reset pin for the W5500

// Pin Definitions
const int bilgePwmPins[4] = { 7, 8, 9, 11 };
const int bilgeControlPins[4] = { 25, 23, 20, 21 };
const int gripper1Pin = 45;
const int gripper2Pin = 49;

// Ethernet settings
byte mac[] = { 0x02, 0xAB, 0xCD, 0xEF, 0x12, 0x34 };
IPAddress ip(192, 168, 33, 100);
IPAddress server(192, 168, 33, 1);
EthernetClient client;
const int serverPort = 1222;

unsigned long lastSendTime = 0;          // Store the last send time
const unsigned long sendInterval = 500;  // Send data every 500ms

void setup() {
  Wire.begin();
  // Initialize pressure sensor
  // Returns true if initialization was successful
  // We can't continue with the rest of the program unless we can initialize the sensor
  while (!sensor.init()) {
    Serial.println("Init failed!");
    Serial.println("Are SDA/SCL connected correctly?");
    Serial.println("Blue Robotics Bar30: White=SDA, Green=SCL");
    Serial.println("\n\n\n");
    delay(5000);
  }
  sensor.setFluidDensity(997);
  thruster1.attach(2);
  thruster2.attach(3);
  Serial.begin(9600);

  pinMode(W5500_RESET_PIN, OUTPUT);
  digitalWrite(W5500_RESET_PIN, HIGH);  // Ensure it's not resetting initially

  // Initialize pins
  for (int i = 0; i < 4; i++) {
    pinMode(bilgePwmPins[i], OUTPUT);
    pinMode(bilgeControlPins[i], OUTPUT);
  }
  pinMode(gripper1Pin, OUTPUT);
  pinMode(gripper2Pin, OUTPUT);

  Wire.begin();
  // IMU INTIALIZATION
  mpu6050.begin();
  // mpu6050.calcGyroOffsets(true);

  resetEthernet();  // Reset the W5500 before starting
  connectToServer();
}

void loop() {

  Ethernet.maintain();

  // delay(500);
  if (!client.connected() || Ethernet.linkStatus() == 2) {
    Serial.println("Lost connection to server. Reconnecting...");
    // resetEthernet();
    reconnectToServer();
    // Serial.println("Done");
  }

  while (client.available()) {
    String receivedData = client.readStringUntil('\n');
    // Serial.print("Received from server: ");
    // Serial.println(receivedData);
    if (receivedData.length() != 26) continue;
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
  if (client.connect(server, serverPort)) {
    Serial.println("Connected!");
  } else {
    Serial.println("Connection failed.");
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

  int analogValue = analogRead(PH_pin);
  float voltage = analogValue * (5.0 / 1023.0);
  float PH = (3.5 * voltage);

  // Read IMU data

  mpu6050.update();
  float angle_x = mpu6050.getAngleX();
  float angle_y = mpu6050.getAngleY();
  float angle_z = mpu6050.getAngleZ();

  //handeling chars of imu


  // Read Bar30 sensor data
  sensor.read();

  String readings;
  if (PH <= 9 && sensor.depth()<0) {
    readings = "0" + String(PH, 2) + String(sensor.depth(), 2) + String(angle_x, 0) + String(angle_y, 0) + String(angle_z, 0);
  } else if  (PH <= 9 && sensor.depth()>=0){
    readings ="0"+ String(PH, 2) +"0" +String(sensor.depth(), 2) + String(angle_x, 0) + String(angle_y, 0) + String(angle_z, 0);
  }else if (PH > 9 && sensor.depth()<0){
     readings = String(PH, 2) + String(sensor.depth(), 2) + String(angle_x, 0) + String(angle_y, 0) + String(angle_z, 0);
  }else if (PH > 9 && sensor.depth()>=0){
    readings = String(PH, 2) +"0"+ String(sensor.depth(), 2) + String(angle_x, 0) + String(angle_y, 0) + String(angle_z, 0);
  }

  // String readings;
  // // Get IMU values (Replace with actual function calls)
  // int anglex = mpu6050.getAngleX();
  // int angley = mpu6050.getAngleY();
  // int anglez = mpu6050.getAngleZ();

  // // Formatting PH and Depth
  // String phStr = (PH < 10) ? "0" + String(PH, 2) : String(PH, 2);
  // String depthStr = (sensor.depth() < 0) ? String(sensor.depth(), 2) : "0" + String(sensor.depth(), 2);

  // // Formatting IMU Angles (Each must be 4 chars with sign)
  // auto formatIMU = [](int angle) {
  //     String str = (angle < 0) ? String(angle) : "+" + String(angle);
  //     while (str.length() < 4) str = str[0] + String("0") + str.substring(1);
  //     return str;
  // };

  // String imuXStr = formatIMU(anglex);
  // String imuYStr = formatIMU(angley);
  // String imuZStr = formatIMU(anglez);

  // // Constructing final message
  // readings = phStr + depthStr + imuXStr + imuYStr + imuZStr ;
  Serial.println(readings);
  client.print(readings);
}

void moveThrusters(String message) {
  String thruster1Val = message.substring(0, 4);
  String thruster2Val = message.substring(4, 8);
  thruster1.writeMicroseconds(thruster1Val.toInt());
  thruster2.writeMicroseconds(thruster2Val.toInt());
}

void moveBilges(String message) {
  for (int i = 0; i < 4; i++) {
    String bilgePwmVal = message.substring(8 + i * 4, 11 + i * 4);
    String bilgeControlVal = message.substring(11 + i * 4, 12 + i * 4);
    analogWrite(bilgePwmPins[i], bilgePwmVal.toInt());
    digitalWrite(bilgeControlPins[i], bilgeControlVal.toInt());
  }
}

void moveGrippers(String message) {
  String gripper1Val = message.substring(24, 25);
  String gripper2Val = message.substring(25, 26);
  digitalWrite(gripper1Pin, gripper1Val.toInt());
  digitalWrite(gripper2Pin, gripper2Val.toInt());
}

void moveAll(String message) {
  if (message.length() != 26) return;
  moveThrusters(message);
  moveBilges(message);
  moveGrippers(message);
}