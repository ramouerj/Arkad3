#include <AcceleroMMA7361.h>

AcceleroMMA7361 accelero;
int x, y, z;

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
 x = accelero.getXAccel();
 y = accelero.getYAccel();
 
 Serial.print(x);
 Serial.print(" ");
 Serial.println(y);
 
 delay(50); //make it readable
}
