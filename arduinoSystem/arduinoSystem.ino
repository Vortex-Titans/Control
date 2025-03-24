#include <SPI.h>
#include <Ethernet.h>
#include <Wire.h>
#include <Servo.h>

// Create a Servo object to control the ESC
Servo thruster1;
Servo thruster2;

#define PH_pin A0
#define W5500_RESET_PIN 8  // Define a reset pin for the W5500

// Pin Definitions
const int bilgePwmPins[6] = {2, 3, 4, 5, 6, 7};
const int bilgeControlPins[6] = {22, 23, 24, 25, 26, 27};
const int gripper1Pin = 28;
const int gripper2Pin = 29;

// Ethernet settings
byte mac[] = {0x02, 0xAB, 0xCD, 0xEF, 0x12, 0x34};
IPAddress ip(192, 168, 33, 100);
IPAddress server(192, 168, 33, 1);
EthernetClient client;
const int serverPort = 1222;

void setup() {
    thruster1.attach(9);
    thruster2.attach(10);
    Serial.begin(9600);

    pinMode(W5500_RESET_PIN, OUTPUT);
    digitalWrite(W5500_RESET_PIN, HIGH); // Ensure it's not resetting initially

    // Initialize pins
    for (int i = 0; i < 6; i++) {
        pinMode(bilgePwmPins[i], OUTPUT);
        pinMode(bilgeControlPins[i], OUTPUT);
    }
    pinMode(gripper1Pin, OUTPUT);
    pinMode(gripper2Pin, OUTPUT);

    Wire.begin();
    resetEthernet(); // Reset the W5500 before starting
    connectToServer();
}

void loop() {

    Ethernet.maintain(); 
    if (!client.connected() || Ethernet.linkStatus() == 2) {
        Serial.println("Lost connection to server. Reconnecting...");
        // resetEthernet();
        reconnectToServer();
        // Serial.println("Done");
    }

    while (client.available()) {
        String receivedData = client.readStringUntil('\n');
        sendPHData();
        Serial.print("Received from server: ");
        Serial.println(receivedData);
        moveAll(receivedData);
        delay(50);
    }
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

// Function to send pH sensor data
void sendPHData() {
    int analogValue = analogRead(PH_pin);
    float voltage = analogValue * (5.0 / 1023.0);
    float PH = (3.5 * voltage);
    String Sph = String(PH, 2);
    client.println(Sph);
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
    moveThrusters(message);
    moveBilges(message);
    moveGrippers(message);
}
