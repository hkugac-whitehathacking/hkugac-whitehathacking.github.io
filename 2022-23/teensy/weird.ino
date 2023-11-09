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
    
  delay(1500);
  Keyboard.set_modifier(0);
  Keyboard.set_key1(0);
  Keyboard.send_now();
  Keyboard.print("powershell.exe");
  Keyboard.set_key1(KEY_ENTER);
  Keyboard.send_now();
  Keyboard.set_key1(0);
  Keyboard.send_now();


  delay(1500);
  Keyboard.print("Start-BitsTransfer -Source 'https://media.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif' -Destination \"$HOME\\Downloads\\rickroll-roll.gif\"");
  delay(500);
  Keyboard.set_key1(KEY_ENTER);
  Keyboard.send_now();
  Keyboard.set_key1(0);
  Keyboard.send_now();

  delay(3000);
  Keyboard.print("start \"$HOME\\Downloads\\rickroll-roll.gif\"");
  delay(500);
  Keyboard.set_key1(KEY_ENTER);
  Keyboard.send_now();
  Keyboard.set_key1(0);
  Keyboard.send_now();

  delay(500);
  Keyboard.set_key1(KEY_ENTER);
  Keyboard.send_now();
  Keyboard.set_key1(0);
  Keyboard.send_now();

}

void loop() {
  // put your main code here, to run repeatedly:

}