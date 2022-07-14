#include <FastLED.h>

class FlashMode: public Mode {
  public:

    FlashMode(int numPoints) {
      this->numPoints = numPoints;
    }
    
    int writeColor(CRGB color, CRGB* leds, int numLeds) {
      for (int i = 0; i < numPoints; i++) {
        CRGB led = leds[i * numLeds/numPoints];
        if (led.r < 20 && led.g < 20 && led.b < 20) {
          leds[i * numLeds/numPoints] = color;
        }
        fadeToBlackBy(&leds[i*numLeds/numPoints], 1,random8(5, 20));
      }

      return delay;
    }

  private:
    int numPoints;

    int delay = 60000;
};
