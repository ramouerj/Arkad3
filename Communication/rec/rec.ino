void setup() 
{
Serial.begin(9600);

}
void loop() // run over and over
{
if (Serial.available())
  Serial.write(Serial.read());
}
