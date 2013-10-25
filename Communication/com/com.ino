#include <AcceleroMMA7361.h>

AcceleroMMA7361 accelero;
int x, y, z;
String out = "";
String sx, sy, sz;

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
 z = accelero.getZAccel();
 
 sx = String(x);
 sy = String(y);
 sz = String(z);
 
 out += "2 ";
 out += sx;
 out += " ";
 out += sy;
 out += " ";
 out += sz;
 
 Serial.println(out);
 
 out = "";
 delay(35);
}
