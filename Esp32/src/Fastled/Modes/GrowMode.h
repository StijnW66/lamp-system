#include <FastLED.h>
#include "Utilities.h"

class GrowMode: public Mode {
  public:

    GrowMode(int duplicates, int minWidth, bool retract, int numLeds) {
      this->duplicates = duplicates;
      this->maxWidth = (((numLeds/duplicates)/2) - 3);
      this->minWidth = minWidth;
      this->retract = retract;

      this->growing = true;
      this->currentWidth = minWidth;
    }
    
    int writeColor(CRGB color, CRGB* leds, int numLeds) {

      if (currentWidth == minWidth || !retract) {
        for (int i = -minWidth; i <= minWidth; i++) {
          duplicate(color, leds, numLeds, numLeds/duplicates + i, duplicates);
        }
      }
      
      if (growing) {
        currentWidth++;

        duplicate(color, leds, numLeds, numLeds/duplicates + currentWidth, duplicates);
        duplicate(color, leds, numLeds, numLeds/duplicates - currentWidth, duplicates);
        
      } else {
        if (retract) {
        duplicate(CRGB::Black, leds, numLeds, numLeds/duplicates + currentWidth, duplicates);
        duplicate(CRGB::Black, leds, numLeds, numLeds/duplicates - currentWidth, duplicates);
        } else {
          fadeToBlackBy(leds, numLeds, 20);
        }
        currentWidth--;
      }



      if (currentWidth == maxWidth || currentWidth == minWidth) {
        growing = !growing;
      }

      return delay;
    }


  private:
    int duplicates;
    int maxWidth;
    int minWidth;
    bool retract;

    bool growing;
    int currentWidth;

    bool timeOut = true;
    int delay = 120000;
};
