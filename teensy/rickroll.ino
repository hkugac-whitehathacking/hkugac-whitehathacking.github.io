#include <paensy.h>
#include <Keyboard.h>

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);

  delay(2000);
  
  winR();
  keyRelease();

  delay(1000);
  
  // Command
  Keyboard.print("powershell.exe \"Start-BitsTransfer -Source 'https://media.tenor.com/x8v1oNUOmg4AAAAd/rickroll-roll.gif' -Destination \"$HOME\\Downloads\\rickroll-roll.gif\"\"");
  Keyboard.set_key1(KEY_ENTER);
  Keyboard.send_now();

  keyRelease();

  delay(5000);

  // Win + R
  Keyboard.set_modifier(MODIFIERKEY_RIGHT_GUI);
  Keyboard.set_key1(KEY_R);
  Keyboard.send_now();
  
  keyRelease();

  delay(1000);
  
  // Command
  Keyboard.print("powershell.exe \"start \"$HOME\\Downloads\\rickroll-roll.gif\"\"");
  Keyboard.set_key1(KEY_ENTER);
  Keyboard.send_now();

  keyRelease();
  
  delay(1000);

  // Choose if Only once
  Keyboard.set_key1(KEY_ENTER);
  Keyboard.send_now();

  keyRelease();

  delay(5000);
  
  // Alt + F4
  Keyboard.set_modifier(MODIFIERKEY_ALT);
  Keyboard.set_key1(KEY_F4);
  Keyboard.send_now();

  keyRelease();

  delay(1000);

  winR();

  keyRelease();

  delay(1000);
  
  // Command
  Keyboard.print("powershell.exe \"Start-Process https://www.youtube.com/watch?v=9OSBrvAJYC4\"");
  Keyboard.set_key1(KEY_ENTER);
  Keyboard.send_now();

  keyRelease();

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
  delay(1000);     
}

void keyRelease() {
  Keyboard.set_modifier(0);
  Keyboard.set_key1(0);
  Keyboard.send_now();
}

void winR() {
  Keyboard.set_modifier(MODIFIERKEY_RIGHT_GUI);
  Keyboard.set_key1(KEY_R);
  Keyboard.send_now();
}
