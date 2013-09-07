#include <AcceleroMMA7361.h>

AcceleroMMA7361 accelero;
int y1;
String out;

void setup()
{
 Serial.begin(9600);
 accelero.begin(13, 12, 11, 10, A0, A1, A2);
 accelero.setARefVoltage(5); //sets the AREF voltage to 3.3V
 accelero.setSensitivity(LOW); //sets the sensitivity to +/-6G
 accelero.calibrate();
}

void loop()
{
 y1 = accelero.getYAccel();
 
 out = "2 ";
 out.concat(y1);
 
 Serial.println(out);
 
 delay(50);
}
