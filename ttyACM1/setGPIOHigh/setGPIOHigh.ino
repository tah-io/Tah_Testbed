int pin = 0;
int Min_pin = 2; // Lowest input pin
int Max_pin = 13; // Highest input pin
void setup()
{
   
   for(pin =Min_pin; pin<=Max_pin; pin++)
   {
     pinMode(pin, OUTPUT);                      //SET all GPIO as OUTPUT
   }
/* pinMode(18,OUTPUT);
 pinMode(19,OUTPUT);
 pinMode(20,OUTPUT);
 pinMode(21,OUTPUT);
 pinMode(22,OUTPUT);
 pinMode(23,OUTPUT);
*/   
}

void loop()
{

	/*digitalWrite(18,HIGH);
	digitalWrite(19,HIGH);
	digitalWrite(20,HIGH);
 	digitalWrite(21,HIGH);
	digitalWrite(22,HIGH);
	digitalWrite(23,HIGH);
	*/
        for(int count =Min_pin; count<= Max_pin;count++)
        {
                digitalWrite(count,HIGH);                        //SET all GPIO to LOW
                delay(10);
        }
}



