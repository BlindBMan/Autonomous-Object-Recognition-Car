#include "Arduino.h"
#include "SoftwareSerial.h"
#include <Smartcar.h>
#include <NewPing.h>

SoftwareSerial BTSerial(10, 11);

// left wheels
#define motor_a 2
#define forward_a 3
#define backward_a 4

BrushedMotor leftMotor(forward_a, backward_a, motor_a);

// right wheels
#define motor_b 7
#define forward_b 6
#define backward_b 5

BrushedMotor rightMotor(forward_b, backward_b, motor_b);

DifferentialControl control(leftMotor, rightMotor);
SimpleCar car(control);

#define motor_speed 20
#define motor_turning_speed 30
#define motor_angle 50

// command from bluetooth
char command;

// distance sensors
#define max_distance 30
#define max_side_dist 20

#define left_echo_pin 30
#define left_trig_pin 28
NewPing left_sensor(left_trig_pin, left_echo_pin, 300);

#define center_echo_pin 29
#define center_trig_pin 31
NewPing center_sensor(center_trig_pin, center_echo_pin, 300);

#define right_echo_pin 24
#define right_trig_pin 22
NewPing right_sensor(right_trig_pin, right_echo_pin, 300);


// leds
#define red_led 23
#define green_led 25
#define blue_led 27

unsigned int start = 0;
unsigned int found = 0;


void forward() {
  car.setSpeed(motor_speed);
  //delay(300);
  //car.setSpeed(0);
}

void backward() {
  car.setSpeed(-motor_speed);
  // delay(300);
  // car.setSpeed(0);
}

void left() {
  car.setAngle(motor_angle);
  car.setSpeed(motor_turning_speed);
  // delay(500);
  // car.setSpeed(0);
  // car.setAngle(0);
}

void right() {
  car.setAngle(-motor_angle);
  car.setSpeed(motor_turning_speed);
  // delay(500);
  // car.setSpeed(0);
  // car.setAngle(0);
}

void backward_left() {
  car.setAngle(motor_angle);
  car.setSpeed(-motor_turning_speed);
  // delay(500);
  // car.setAngle(0);
  // car.setSpeed(0);
}

void backward_right() {
  car.setAngle(-motor_angle);
  car.setSpeed(-motor_turning_speed);
  // delay(500);
  // car.setSpeed(0);
  // car.setAngle(0);
}


void found_movement() {
  car.setAngle(90);
  car.setSpeed(motor_turning_speed);
  delay(1000);
  car.setSpeed(0);
  car.setAngle(0);
}


void setup() {
  Serial.begin(115200);
  BTSerial.begin(9600);
}


void loop() {
  delay(20);
  unsigned long left_dist = left_sensor.ping_cm();
  delay(20);
  unsigned long center_dist = center_sensor.ping_cm();
  delay(20);
  unsigned long right_dist = right_sensor.ping_cm();

  if (BTSerial.available()) {
    command = BTSerial.read();

    if (command == 'S')
      start = 1;
    else if (command == 'T') {
      start = 0;
      car.setSpeed(0);
    }
    else if (command == 'X') {
      found = 1;
      found_movement();
    }
    
  }

  if (start == 1 && found == 0) {
    if (left_dist <= max_side_dist || center_dist <= max_distance || right_dist <= max_side_dist) {

      if (left_dist <= max_side_dist && center_dist <= max_distance && right_dist <= max_side_dist) {
        backward();
        delay(300);
      }
      else if (left_dist < right_dist) {
        backward_left();
        delay(400);
        right();
        delay(300);
      }
      else if (left_dist >= right_dist) {
        backward_right();
        delay(400);
        left();
        delay(300);
      }
      
      car.setAngle(0);
    }
    else {
      forward();
    }
  }
}