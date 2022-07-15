#include <FastLED.h>

class StepSweepMode: public Mode {
  public:

    StepSweepMode(int numSteps, int stepSize, int numDuplicates) {
      this->stepSize = stepSize;
      this->sweepSize = numSteps * stepSize;
      this->target = sweepSize;
      this->numDuplicates = numDuplicates;
    }
    
    int writeColor(CRGB color, CRGB* leds, int numLeds) {
      if (timeOut != 0) {
        timeOut--;
        return;
      }
      
      if (stepping) {
        pos = (pos + stepSize) % numLeds;
        timeOut = (stepSize);
      } else {
        pos = (pos + 1) % numLeds;
      }

      if (pos == target) {
        target = (target + sweepSize) % numLeds;
        timeOut = (stepping) ? 0 : (stepSize);
        stepping = !stepping;
      }
      
      //leds[pos] = color;
      duplicate(color, leds, numLeds, pos, numDuplicates);
      int k;
      int deletePos = ((k = pos - 2*sweepSize) >= 0) ? k : k + numLeds;
      //leds[deletePos] = CRGB::Black;
      duplicate(CRGB::Black, leds, numLeds, deletePos, numDuplicates);
      return delay;
    }


  private:
    int stepSize;
    int sweepSize;

    int target;
    int pos = 0;
    int timeOut = 0;
    bool stepping = false;

    int numDuplicates;

    int delay = 60000;

    void duplicate(CRGB color, CRGB* leds, int numLeds, int pos, int numDuplicates) {
      int spacing = numLeds/numDuplicates;
      for (int i = 0; i < numDuplicates; i++) {
        leds[(pos + (spacing * i)) % numLeds] = color;
      }
    }
};
