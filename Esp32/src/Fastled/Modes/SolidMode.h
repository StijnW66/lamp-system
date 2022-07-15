#include <FastLED.h>

class SolidMode: public Mode {
  public:
    
    int writeColor(CRGB color, CRGB* leds, int numLeds) {
      fill_solid(leds, numLeds, color);

      return delay;
    }

  private:
    int delay = 60000;
};
