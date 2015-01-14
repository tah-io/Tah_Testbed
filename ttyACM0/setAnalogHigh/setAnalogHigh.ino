void setup()
{
        Serial.begin(9600);
        pinMode(A0,OUTPUT);
        pinMode(A1,OUTPUT);
        pinMode(A2,OUTPUT);
        pinMode(A3,OUTPUT);
        pinMode(A4,OUTPUT);
        pinMode(A5,OUTPUT);

	for(int i=2;i<=13;i++)
	{
		pinMode(i,OUTPUT);
	}


}

void loop()
{
        analogWrite(A0,255);
        analogWrite(A1,255);
        analogWrite(A2,255);
        analogWrite(A3,255);
        analogWrite(A4,255);
        analogWrite(A5,255);
	
	for(int i=2;i<=13;i++)
	{
		digitalWrite(i,HIGH);
		delay(1);
	}

}



