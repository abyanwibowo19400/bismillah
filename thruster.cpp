#include <ros.h>
#include <Servo.h>
#include <std_msgs/Float32.h>
#include <std_msgs/Int16.h>
#include <Adafruit_BNO055.h>
#include <MS5837.h>

// Init Node
ros::NodeHandle node_arduino;

// Init Msgs
std_msgs::Float32 msg_roll; // x
std_msgs::Float32 msg_pitch; // y
std_msgs::Float32 msg_yaw; // z

// Init Publisher
ros::Publisher pub_roll("roll", &msg_roll);
ros::Publisher pub_pitch("pitch", &msg_pitch);
ros::Publisher pub_yaw("yaw", &msg_yaw);


Adafruit_BNO055 bno = Adafruit_BNO055();

MS5837 ms5837;

const int totalServo = 8;
byte thrusterPins[totalServo] = {3, 5, 6, 7, 8, 9, 10, 12};
Servo thrusters[totalServo];
//inisiasi thruster
//byte thrusterPin1 = 3;
//byte thrusterPin2 = 5;
//byte thrusterPin3 = 6;
//byte thrusterPin4 = 7;
//byte thrusterPin5 = 8;
//byte thrusterPin6 = 9;
//byte thrusterPin7 = 10;
//byte thrusterPin8 = 12;

//Servo thruster1;
//Servo thruster2;
//Servo thruster3;
//Servo thruster4;
//Servo thruster5;
//Servo thruster6;
//Servo thruster7;
//Servo thruster8;

void callbackPwmRoll(const std_msgs::Int16& pwmRoll){
  // Roll Movement
}

void callbackPwmPitch(const std_msgs::Int16& pwmPitch){
  // Pitch Movement
}

void callbackPwmYaw(const std_msgs::Int16& pwmYaw){
  // Yaw Movement
}

ros::Subscriber<std_msgs::Int16> subPwmRoll("pwm_roll", &callbackPwmRoll);
ros::Subscriber<std_msgs::Int16> subPwmPitch("pwm_pitch", &callbackPwmPitch);
ros::Subscriber<std_msgs::Int16> subPwmYaw("pwm_yaw", &callbackPwmYaw);

void setup() {
  if(!bno.begin())
  {
    Serial.println("Tidak dapat menemukan sensor BNO055, pastikan sensor terhubung dengan baik.");
    while(1);
  }

  ms5837.init();

  for (int i = 0; i < totalServo; i++) {
    thrusters[i].attach(thrusterPins[i]);
    thrusters[i].writeMicroseconds(1500);
  }
  
//  thruster1.attach(thrusterPin1);
//  thruster2.attach(thrusterPin2);
//  thruster3.attach(thrusterPin3);
//  thruster4.attach(thrusterPin4);
//  thruster5.attach(thrusterPin5);
//  thruster6.attach(thrusterPin6);
//  thruster7.attach(thrusterPin7);
//  thruster8.attach(thrusterPin8);


  //set pwm 1500
//  thruster1.writeMicroseconds(1500);
//  thruster2.writeMicroseconds(1500);
//  thruster3.writeMicroseconds(1500);
//  thruster4.writeMicroseconds(1500);
//  thruster5.writeMicroseconds(1500);
//  thruster6.writeMicroseconds(1500);
//  thruster7.writeMicroseconds(1500);
//  thruster8.writeMicroseconds(1500);

  node_arduino.initNode();
  node_arduino.advertise(pub_roll);
  node_arduino.advertise(pub_pitch);
  node_arduino.advertise(pub_yaw);
  node_arduino.subscribe(subPwmRoll);
  node_arduino.subscribe(subPwmPitch);
  node_arduino.subscribe(subPwmYaw);

  delay(10000);
}

void loop() {
  sensors_event_t event;
  bno.getEvent(&event);

  float roll = event.orientation.x;
  float pitch = event.orientation.y;
  float yaw = event.orientation.z;



  //nilai sinyal thruster
  int signals[totalServo];
//  int signal1; //= 1500 +- pwm
//  int signal2; //= 1500 +- pwm
//  int signal3; //= 1500 +- pwm
//  int signal4; //= 1500 +- pwm
//  int signal5; //= 1500 +- pwm
//  int signal6; //= 1500 +- pwm
//  int signal7; //= 1500 +- pwm
//  int signal8; //= 1500 +- pwm

  for (int i = 0; i < totalServo; i++) {
    thrusters[i].writeMicroseconds(signals[i]);
  }

  //Nilai Thruster
//  thruster1.writeMicroseconds(signal1);
//  thruster2.writeMicroseconds(signal2);
//  thruster3.writeMicroseconds(signal3);
//  thruster4.writeMicroseconds(signal4);
//  thruster5.writeMicroseconds(signal5);
//  thruster6.writeMicroseconds(signal6);
//  thruster7.writeMicroseconds(signal7);
//  thruster8.writeMicroseconds(signal8);

  ms5837.read();
  float depthInput = ms5837.depth();

  msg_roll.data = roll;
  msg_pitch.data = pitch;
  msg_yaw.data = yaw;
  
  pub_roll.publish(&msg_roll);
  pub_pitch.publish(&msg_pitch);
  pub_yaw.publish(&msg_yaw);

  node_arduino.spinOnce();
  delay(100);
}