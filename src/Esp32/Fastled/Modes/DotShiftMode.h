#include <FastLED.h>

class DotShiftMode: public Mode {
  public:

    DotShiftMode(int space) {
      this->space = space;
    }
    
    int writeColor(CRGB color, CRGB* leds, int numLeds) {
      fadeToBlackBy(leds, numLeds, 3);
      leds[(pos + offset)%numLeds] = color;

      pos = (pos + space) %numLeds;

      if (pos < space) {
        offset = offset + 1;
      }

      return delay;
    }

  private:
    int space = 1;
    int offset = 0;
    int pos = 0;

    int delay = 60000;
};
