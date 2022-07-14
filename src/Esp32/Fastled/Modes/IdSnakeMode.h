#include <FastLED.h>

class IdSnakeMode: public Mode {
  public:

    IdSnakeMode(int candySize, int numLeds) {      
      for (int i = 0; i < candySize; i++) {
        this->candyPos.push_back(random16(0, numLeds));
        this->candyColor.push_back(CRGB::Red);
      }
    }
    
    int writeColor(CRGB color, CRGB* leds, int numLeds) {
      snakePos = (snakePos + 1) % numLeds;

      std::vector<int>::iterator it = std::find(candyPos.begin(), candyPos.end(), snakePos);
      if (it != candyPos.end()) {
        int index = it - candyPos.begin();
        
        candyPos.erase(candyPos.begin() + index);
        candyColor.erase(candyColor.begin() + index);
        snakeSize++;

        candyPos.push_back((random16(10, numLeds - snakeSize - 10) + snakePos) % numLeds);
        candyColor.push_back(color);

        if (snakeSize > 100) {
          snakeSize = 10;
        }
      }

      for (int i = 0; i < candyPos.size(); i++) {
        leds[candyPos.at(i)] = candyColor.at(i);
      }

      
      leds[snakePos] = color;
      int snakeTail = snakePos - snakeSize;

      if (snakeTail < 0) {
        snakeTail = numLeds + snakeTail;
      }
      leds[snakeTail] = CRGB::Black;

      return delay;
    }


  private:
    int snakeSize = 0;
    int snakePos = -1;
    
    std::vector<int> candyPos;
    std::vector<CRGB> candyColor;

    int delay = 60000;
};
