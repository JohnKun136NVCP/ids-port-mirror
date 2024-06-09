
 int randomnum; //Declare de function random
 

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(14, OUTPUT); //Declare the GreenLed
  pinMode(26, OUTPUT); //Declare the YellowLed
  pinMode(27, OUTPUT); //Declare the RedLed
  pinMode(4, OUTPUT); //Declare the buzzer
  randomSeed (analogRead (0)); //generate a new sequence of random numbers
}

// the loop function runs over and over again forever
void loop() {
  randomnum = random (0,20);
  if (randomnum >0 && randomnum<5){    // give it a range to turn on
    digitalWrite(14, HIGH);   // turn on the Gren LED on (HIGH is the voltage level) 
    delay(1000);  // give it a little delay
    digitalWrite(14,LOW); // turn off de Green LED
  }else if (randomnum >5 && randomnum<10){     // give it a range to turn on another led
    digitalWrite(26, HIGH);    // turn on the Yellow LED on (HIGH is the voltage level) 
    delay(1000);               // give it a little delay
    digitalWrite(26, LOW);     // turn off the Yellow LED off by making the voltage LOW 
  }else if (randomnum>10){     // give it a range to turn off the Red LED
    digitalWrite(27,HIGH);     //turn on the Red LED on (HIGH is the voltage level) 
    delay(1000);               // turn off the Red LED off by making the voltage LOW 
    digitalWrite(27, LOW);     // turn the Red LED off by making the voltage LOW
      digitalWrite(4, HIGH);   // turn on the buzzer 
  delay(1000);                 // wait for a second
  digitalWrite(4 , LOW);       // turn off the buzzer
  delay(1000);                 // wait for a second
  }
}
