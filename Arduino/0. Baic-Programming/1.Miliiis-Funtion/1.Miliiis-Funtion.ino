const unsigned long eventInterval = 1000;
unsigned long previousTime = 0;

void setup() {
  
  
}

void loop() {
  for (int i = 0; i < 10; i ++){
    digitalWrite(LED_eye_L, HIGH);
    digitalWrite(LED_eye_R, LOW);

    delay(100);

    digitalWrite(LED_eye_L, LOW);
    digitalWrite(LED_eye_R, HIGH);

    delay(100);
  }

  if(digitalRead(button_pin) == HIGH){
    digitalWrite(LED_3rd_eye, HIGH);
  }

  else{
    digitalWrite(LED_3rd_eye, LOW);
  }

}
