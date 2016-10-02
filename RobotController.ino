#include <Servo.h>

Servo myservo;
Servo gripper;  // create servo object to control a servo

// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
int posGripper = 0;
int stopingContinous = 95.5;




void setup() {
  myservo.attach(9);// attaches the servo on pin 9 to the servo object
  Serial.begin(9600);
}
void open1(){
    for (pos = 60; pos <= 85; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
        myservo.write(pos);
        delay(15);

    }  
  }
void close1()
{
     for (pos = 85; pos >= 60; pos -= 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
        myservo.write(pos);
        delay(15);

    } 
  }
void downCont(){
  myservo.write(0);
  delay(50);
  myservo.write(95.5);
  pos -=1;
}

void loop() {
  //Serial.println("Hello world from Ardunio!"); // write a string

  if (Serial.available())
  {
    int inpu = Serial.read();
    Serial.println("current number");
    Serial.println(inpu);
    int input = int(inpu);
    
    if (input == 49)
    {
      open1();
      delay(5000);
      close1();
    }

  }
                          // waits for the servo to get there
}
