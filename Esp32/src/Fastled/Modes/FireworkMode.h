#include <FastLED.h>
#include <vector>

class Firework {
  public:
    Firework(CRGB color, uint16_t targetPos, uint16_t currentPos, uint8_t explosionTimeout) {
      this->color = color;
      this->targetPos = targetPos;
      this->currentPos = currentPos;
      this->explosionTimeout = explosionTimeout;
    }

    ~Firework(){}

    CRGB getColor() { return this->color; }
    uint16_t getTargetPos() { return this->targetPos; }
    uint16_t getCurrentPos() { return this->currentPos; }
    uint8_t getExplosionTimeout() { return this->explosionTimeout; }

    void setCurrentPos(uint16_t updatedPos) { this->currentPos = updatedPos; }
    void setExplosionTimeout(uint8_t explosionTimeout) {this->explosionTimeout = explosionTimeout;}
    
  private:
    CRGB color;
    uint16_t targetPos;
    uint16_t currentPos;
    uint8_t explosionTimeout;
    
};

class FireworkMode: public Mode {
  public:

    FireworkMode() {
      std::vector<Firework*> vector;
      fireworks = vector;
    }

    ~FireworkMode() {
      while(fireworks.size() > 0) {
        Firework* current = fireworks.at(0);
        fireworks.erase(fireworks.begin());
        delete current;
      }      
    }
    
    int writeColor(CRGB color, CRGB* leds, int numLeds) {
      fadeToBlackBy(leds, numLeds, 80);
      if (timeout == 0) {
        fireworks.push_back((new Firework(color, random16(numLeds - 50, numLeds-1), 0, random8(8, 13))));
        timeout = random8(20, 30);
      }      

      for (int i = 0; i < fireworks.size(); i++) {
        Firework* current = fireworks.at(i);
        uint16_t currentPos = current->getCurrentPos();
      
        if (currentPos != current->getTargetPos()) {
          current->setCurrentPos((currentPos + 1) % (numLeds - 1));
          leds[currentPos] = current->getColor();

        } else {
          uint8_t explosionTimeout = current->getExplosionTimeout();
          if (explosionTimeout != 0) {
            current->setExplosionTimeout(explosionTimeout - 1);
          } else {

            for (int e = -6; e <= 4; e++) {
              if (!(currentPos + e> (numLeds - 1) || currentPos + e < 0)) {
                if((currentPos + e) % 2 == 0) {
                  leds[currentPos + e] = current->getColor();
                } else {
                  leds[currentPos + e] = color;
                }
              }
            }
            fireworks.erase(fireworks.begin()+i);
            delete current;
          }
        }
      }
      timeout--;
      return delay;
    }

  private:
    std::vector<Firework*> fireworks;
    uint8_t timeout = 0;

    int delay = 60000;
};
