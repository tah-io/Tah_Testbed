int pin = 0;
int Min_pin = 2; // Lowest input pin
int Max_pin = 13; // Highest input pin
void setup()
{
   
   for(pin =Min_pin; pin<=Max_pin; pin++)
   {
     pinMode(pin, OUTPUT);			//SET all GPIO as OUTPUT
   }
   
   Serial.begin(9600);
}

void loop()
{
	
	for(int count =Min_pin; count<= Max_pin;count++)
	{
		digitalWrite(count,LOW);			//SET all GPIO to LOW
		delay(10);
	}
}
