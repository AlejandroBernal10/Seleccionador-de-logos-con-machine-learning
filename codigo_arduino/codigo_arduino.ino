#include<Servo.h>

Servo motor;
int led1 = 7;
int led2 = 8;
int dirD = 9;
int dirI = 10;
int velo = 11;
int option;



void setup() {
 
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  motor.attach(4);
  pinMode(dirD,OUTPUT);
  pinMode(dirI,OUTPUT);
  pinMode(velo,OUTPUT);

}
void loop() {
 
  //Prog. del motor

 
  //Condicional concatenado con python 
  if (Serial.available() > 0){
    option = Serial.read();
    Serial.println(option);
    //Comienza el codigo 
    if(option == 'S'){
      digitalWrite(dirD,1);
      digitalWrite(dirI,0);
      analogWrite(velo,50);
      motor.write(0);
     }
    //Gira mitad       JAVA  
    if(option == 'V'){
      motor.write(110);
      digitalWrite(dirD,1);
      digitalWrite(dirI,0);
      analogWrite(velo,50);
    
    }
    //Gira a la izquierda JAVASCRIPT
    if(option == 'J'){
      digitalWrite(led1, HIGH);
      digitalWrite(led2, LOW);
      motor.write(180);
      digitalWrite(dirD,1);
      digitalWrite(dirI,0);
      analogWrite(velo,100);
    }
    //Gira a la derecha PYTHON 
    if(option == 'P'){
      digitalWrite(led1, LOW);
      digitalWrite(led2, HIGH);
      motor.write(50);
      digitalWrite(dirD,1);
      digitalWrite(dirI,0);
      analogWrite(velo,100);
      digitalWrite(dirD,1);
      digitalWrite(dirI,0);
      analogWrite(velo,100);
    }
    //Se queda en el medio
  }
}
