#pragma once

void duplicate(CRGB color, CRGB* leds, int numLeds, int pos, int numDuplicates) {
      int spacing = numLeds/numDuplicates;

      for (int i = 0; i < numDuplicates; i++) {
        int dupPos = pos + (spacing * i);
        dupPos = (dupPos >= 0) ? dupPos : dupPos + numLeds;
        leds[(dupPos) % numLeds] = color;
      }
    }
