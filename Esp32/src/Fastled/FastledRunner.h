#include <FastLED.h>
#include "Includer.h"

#define LED_PIN 13

const int numLeds = 300;
CRGB leds[numLeds];

ModeManager* modeManager = new ModeManager(new FlashMode(50));
int currentMode = 0;

void FastledSetup() {
  //Serial.begin(9600);
  FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, numLeds).setCorrection(TypicalLEDStrip);
  delay(0); // somehow ensures safe startup...
  
  FastLED.setBrightness(50);
  //set_max_power_in_volts_and_milliamps(5, 2000);

  FastLED.clear();
  FastLED.show();
}

int startHeap = 0;
int heap = 0;

bool first = true;
void switchMode() {
  FastLED.clear();
  currentMode = (currentMode + 1) % 10;
  switch(currentMode) {
    case 0 : modeManager->set_mode(new TwinkleMode); fadeToBlackBy(leds, numLeds, 200); break;
    case 1 : modeManager->set_mode(new SnakeMode(random8(3, 10))); break;
    case 2 : modeManager->set_mode(new FireworkMode); break;
    case 3 : {int spacing = random8(20, 60); modeManager->set_mode(new MiddleShiftMode(random16(50, numLeds - 50), spacing, spacing/random8(1, 5))); break;}
    case 4 : modeManager->set_mode(new DotShiftMode(random8(2, 9))); break;
    case 5 : {int amount = random8(4, 8); modeManager->set_mode(new SweepMode(amount, random8(20, numLeds/amount))); break;}
    case 6 : modeManager->set_mode(new IdSnakeMode(10, numLeds)); break;
    case 7 : modeManager->set_mode(new ShiftMode); break;
    case 8 : {bool retract = random8(0, 3); modeManager->set_mode(new GrowMode(random8(5, 15), random8(1, 4), retract, numLeds)); break;}
    case 9 : modeManager->set_mode(new FlashMode(random8(20, 200))); break;
    
    default : modeManager->set_mode(new FireworkMode()); break;
    
  }
  if(first == true) {
    startHeap = ESP.getFreeHeap();
    Serial.println( ESP.getFreeHeap());
    first = false;
  } else {
    heap = ESP.getFreeHeap();
    Serial.print(heap);
    Serial.print("  ");
    Serial.println((heap - startHeap));
  }
}

int FastledLoop(CRGB colorCRGB) {
  EVERY_N_MINUTES(1) {switchMode();}
  
  int delay = modeManager->writeColor(colorCRGB, leds, numLeds);
  FastLED.show();
  return delay;
 }

PanicMode panicMode;
void panic() {
  panicMode.writeColor(CRGB::Red, leds, numLeds);
  FastLED.show();
}
