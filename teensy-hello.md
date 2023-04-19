```
#include <paensy.h>
#include <Keyboard.h>

void setup() {
  // put your setup code here, to run once:
   // allow controlling LED
  pinMode(LED_PIN, OUTPUT);
  // turn the LED on while running
  digitalWrite(LED_PIN, HIGH);

  delay(5000);
    
  Keyboard.set_modifier(MODIFIERKEY_RIGHT_GUI);
  Keyboard.set_key1(KEY_R);
  Keyboard.send_now();
    
  delay(500);
  Keyboard.set_modifier(0);
  Keyboard.set_key1(0);
  Keyboard.send_now();
  Keyboard.print("notepad.exe");
  Keyboard.set_key1(KEY_ENTER);
  Keyboard.send_now();
  Keyboard.set_key1(0);
  Keyboard.send_now();


  delay(300);
  Keyboard.print(" Hello World !!");
  Keyboard.set_key1(KEY_ENTER);   
  Keyboard.send_now();
  Keyboard.set_key1(0);
  Keyboard.send_now();

}

void loop() {
  // put your main code here, to run repeatedly:

}
```
