#include <FastLED.h>
#include "Utilities.h"

class SweepMode: public Mode {
  public:

    SweepMode(int amount, int width) {
      this->duplicates = amount;
      this->width = width;
    }

    // NEED TO WATCHOUT FOR OVERFLOW OF POS!!!!!!!!!!!!!!!!!!!! IF THIS MODE RUNS FOREVER.
    int writeColor(CRGB color, CRGB* leds, int numLeds) {
      if (pos < (lineStart + width)) {
        duplicate(color, leds, numLeds, pos % numLeds, duplicates);

        pos = (pos + 1);

  	    return delay - (pos-lineStart) * (delay/100);
      } else {
        duplicate(CRGB::Black, leds, numLeds, (pos - width + deleteIndex) % numLeds, duplicates);

        deleteIndex++;

        if(width <= deleteIndex) {
          deleteIndex = 0;
          lineStart = pos;
        }
   	    return delay - deleteIndex * (delay/100);

      }
    }


  private:
    int pos = 0;
    int lineStart = 0;
    int deleteIndex = 0;
    int width = 30;
    int duplicates = 8;

    int delay = 60000;
};
