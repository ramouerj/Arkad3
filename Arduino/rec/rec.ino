void setup() 
{
Serial.begin(9600);
//Serial.println("XBEE Example!");
// set the data rate for the SoftwareSerial port

}
void loop() // run over and over
{
if (Serial.available())
  Serial.write(Serial.read());
}
