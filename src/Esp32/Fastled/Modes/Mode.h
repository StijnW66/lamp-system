class Mode {
  public:
    virtual int writeColor(CRGB color, CRGB* leds, int numLeds) = 0;
    virtual ~Mode() {
    }
};
