#include <FastLED.h>

class ShiftMode: public Mode {
  public:

    int writeColor(CRGB color, CRGB* leds, int numLeds) {
      shiftLeds(leds, numLeds);
      leds[0] = color;

      return delay;
    }

  private:
    int delay = 60000;

    void shiftLeds(CRGB* leds, int numLeds) {
      for(int i = (numLeds - 1); i > 0; i--) {
        leds[i] = leds[i - 1];
      }
    }
};
