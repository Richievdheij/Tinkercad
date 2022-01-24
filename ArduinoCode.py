// load LCD library
#include <LiquidCrystal.h>

// set crystal pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

const int BTN = 9;
const int LED = 8;

void setup()
{
  Serial.begin(9600);
  pinMode ( BTN, INPUT);
  pinMode(LED, OUTPUT);
  
  // set LCD size
  lcd.begin(16,2);
  
  //set start
  lcd.setCursor(0,0);
  lcd.print ("Switch light on");
}

// Always loop this code
void loop() {
	int buttonStatus = digitalRead(BTN);
  
  	if (buttonStatus == HIGH){
    	int ledStatus = digitalRead(LED);
    
      	if(ledStatus == HIGH){
  		digitalWrite(LED,LOW); // Turn the light off
		Serial.println("Light is on");
    	lcd.clear(); // Clears the lcd text
    
    	// Top text
    	lcd.setCursor(0,0);
    	lcd.print("Press button to:");
  
  		// Bottom text
    	lcd.setCursor(0, 1);
    	lcd.print("Switch light on");    
	}
      
	else{
  		digitalWrite(LED,HIGH); // Turn the light on
  		Serial.println("Light is off");
  		lcd.clear(); // Clears the lcd text
 
  		// Top text
		lcd.setCursor(0,0);
    	lcd.print("Press button to:");
  
  		// Bottom text
    	lcd.setCursor(0, 1);
    	lcd.print("Switch light off");
    	}
        delay(50);
	}
    delay(50);
}
  