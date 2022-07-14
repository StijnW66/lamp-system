#include <FastLED.h>
#include "Utilities.h"

class SnakeMode: public Mode {
  public:

    SnakeMode(int snakeCount) {
      this->snakeCount = snakeCount;
    }
      
    int writeColor(CRGB color, CRGB* leds, int numLeds) {
      duplicate(color, leds, numLeds, pos, snakeCount);
      
      pos = (pos + 1) % (numLeds);
      fadeToBlackBy(leds, numLeds, 15 * snakeCount/2);

      return delay;
    }

  private:
    int pos = 0;
    int snakeCount = 0;

    int delay = 60000;
};
