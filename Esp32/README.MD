:warning: This is an Arduino project. Open Fastled.ino in the Arduino IDE. Also add wifi credentials in [WiFiConnection.h](./src/Fastled/WiFiConnection.h)

- This code is meant to be run on an Esp32 microcontroller. The Esp32 is fast, resourcefull, cheap, and capable of WiFi and Bluetooth connections, it is therefore an excellent fit for this project.

- The Esp32 continuously polls the server and requests information regarding the color pattern. With the color pattern information the Esp32 is able to light up a WS2812b LED strip using the FastLed library.

- Lighting up the LED strip with a certain color pattern is nice, but gets boring relatively quickly. Therefore certain 'modes' have been created, which allows the Esp32 to display animations on the LED strip, whilst still honouring the original color pattern.


The Esp32 has two threads running. The first thead is responsible for establishing a WiFi connection and polling the webserver. The second thread is responsible for advancing the color pattern and running the animations on the LED strip.

## File structure
- [Fastled.ino](./src/Fastled/Fastled.ino) sets up two looping threads that handle WiFi connection and LED strip animation.
- [WiFiConnection.h](./src/Fastled/WiFiConnection.h) contains all code for server communication.
- [FastledRunner.h](./src/Fastled/FastledRunner.h) sets up the FastLed library and periodically swithces the active animation mode.
- [ModeManager.h](./src/Fastled/ModeManager.h) allows for memory efficient control over animation modes.
- [Modes/](./src/Fastled/Modes/) is a folder containing the implementation of animation modes.
- [OTA.h](./src/Fastled/OTA.h) allows for optional Over the Air Updates trough WiFi.