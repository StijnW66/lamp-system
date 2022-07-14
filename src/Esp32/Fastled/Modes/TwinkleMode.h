#include <FastLED.h>

class TwinkleMode: public Mode {
  public:

    int writeColor(CRGB color, CRGB* leds, int numLeds) {
      if (timeOut == 0) {
        uint16_t pos = random16(0, numLeds);

        uint8_t width = random8(0, 3);

        for (int i = -width / 2; i < width / 2; i++) {
          if (!((pos + i) > (numLeds-1) || (pos + i) < 0)) {
            leds[pos + i] = color;
          }
        }
        timeOut = random8(1, 3);
      }

      blur1d(leds, numLeds, random8(15, 40));
      timeOut--;

      return delay;
    }

  private:
    int delay = 60000;
    uint8_t timeOut = 0;
};
