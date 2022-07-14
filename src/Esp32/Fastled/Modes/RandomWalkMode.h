#include <FastLED.h>

class RandomWalkMode: public Mode {
  public:
    
    int writeColor(CRGB color, CRGB* leds, int numLeds) {
      bool Ldir = random8(0, 3);

      pos = Ldir ? ++pos : --pos;

      pos = pos % numLeds;
      pos = (pos < 0) ? numLeds : pos;

      pos = beatsin16(10, 0, numLeds/10)+beatsin16(5, 0, numLeds/10);
      duplicate(color, leds, numLeds, pos, 10);
      //leds[pos] = color;
      fadeToBlackBy(leds, numLeds, 125);

      return delay;
    }

  private:
    int pos = 0;
    int delay = 60000;


    void duplicate(CRGB color, CRGB* leds, int numLeds, int pos, int numDuplicates) {
      int spacing = numLeds/numDuplicates;
      for (int i = 0; i < numDuplicates; i++) {
        if (pos + (spacing * i) > 0) {
          leds[(pos + (spacing * i)) % numLeds] = color;
        }
      }
    }
};
