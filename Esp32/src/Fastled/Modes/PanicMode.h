#include <FastLED.h>

bool p = false;
class PanicMode: public Mode {
  public:
      
    int writeColor(CRGB color, CRGB* leds, int numLeds) {
      if (p) {
        fill_solid(leds, 10, color);
      } else {
        FastLED.clear();
      }

      p = !p;

      //setup initial randomization
      randomize();

      return delay;
    }

  private:

    int delay = 40000;

    void randomize() {
      for (int i = random(1, 10); i > 0; i--) {
        random8();
        random16();
      }
      
    }
      
};
