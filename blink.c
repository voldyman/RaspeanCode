#include <wiringPi.h>
#include <stdio.h>

int main(void) {
	printf ("Raspberry Pi Blinker\n");
	if (wiringPiSetup() == -1)
		return 1;
	pinMode(7, OUTPUT);
	for (;;) {
		digitalWrite(7 ,1);
		delay(500);
		digitalWrite(7,0);
		delay(500);
	}
	return 0;
}
