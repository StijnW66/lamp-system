class ModeManager {
  private:
    Mode* mode_;

  public:
    ModeManager(Mode* mode = nullptr): mode_(mode) {}
    ~ModeManager() {
      delete this->mode_;
    }

    void set_mode(Mode* mode_) {
      delete this->mode_;
      this->mode_ = mode_;
    }

    Mode *getModeType() {
      return this->mode_;
    }

    int writeColor(CRGB color, CRGB* leds, int numLeds) const {
      return this->mode_->writeColor(color, leds, numLeds);
    }

};
