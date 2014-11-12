void setup()
{
	Serial.begin(9600);
	pinMode(A0,INPUT);
	pinMode(A1,INPUT);
	pinMode(A2,INPUT);
	pinMode(A3,INPUT);
	pinMode(A4,INPUT);
	pinMode(A5,INPUT);
}

void loop()
{
	analogWrite(A0,0);
        analogWrite(A1,0); 
        analogWrite(A2,0); 
        analogWrite(A3,0); 
        analogWrite(A4,0); 
        analogWrite(A5,0); 
} 

