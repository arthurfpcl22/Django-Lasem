
const int tmp36=A0;
int sensorvalue=0;
float voltage=0;
float tmp=0;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
    
        sensorvalue=analogRead(A0);
        voltage=(sensorvalue/1024.0)*5.0;
        tmp=(voltage-0.5)*100.0;
        Serial.println(tmp);
        delay(3000);
     
}
