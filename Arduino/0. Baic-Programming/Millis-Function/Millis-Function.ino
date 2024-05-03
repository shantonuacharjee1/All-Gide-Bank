unsigned long previousTime = 0;


void setup() {
  Serial.begin(9600);

}

void loop() {
  previousTime = millis();
  Serial.println(previousTime);

  if (millis() > 3000UL){
    Serial.println("Its party time");
  }

}
