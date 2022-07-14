#include <FastLED.h>

class MiddleShiftMode: public Mode {
  public:

    MiddleShiftMode(int center, int spacing, int width) {
      this->center = center;
      this->spacing = spacing;
      this->width = width;
    }
    
    int writeColor(CRGB color, CRGB* leds, int numLeds) {
      shiftFromCenter(center, leds, numLeds);

      
      if (spacingTimeout == 0) {
        if (widthCount == 0) {
          widthCount = width;
          
          spacingTimeout = spacing - 1;
          leds[center] = CRGB::Black;

        } else {
          leds[center] = color;
          widthCount--;
        }
      } else {
        leds[center] = CRGB::Black;
        spacingTimeout--;
      }

      return delay;
    }

  private:

    int center = 0;
    int spacing = 0;
    int width = 0;

    int widthCount= 0;
    int spacingTimeout = 0;

    int delay = 60000;

    void shiftFromCenter(int center, CRGB* leds, int numLeds) {
      
      //shift right
      for (int i = 0; i < center; i++) {
          leds[i] = leds[i + 1];
      }

      //shift left
      for (int i = numLeds - 1; i > center; i--) {
        leds[i] = leds[i - 1];
      }
    }
};
