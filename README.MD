# Lamp-System

This project aims to schynchronize multiple rgb lights, which are located in remote places. To achieve this a centralized [webserver](./Server/) is created. This webserver accepts HTTP requests from clients such as the lamp (Esp32/Raspberry Pi) or from a remote controller (Phone/Desktop app). Another usefull tool for interaction with the webserver is an API application like Postman.

## Lamp Implementations
Name | Image
--- | ---
[Esp32 + ws2812b LED strip](./Esp32/) | <img src="./Images/FlashMode.gif" width="300" />
[Raspberry Pi + rgb-LED](./RaspberryPi/) | <img src="./Images/RaspberryPi.png" width="300" />

## Controller Implementations
Name | Image
--- | ---
[Android App](./Android/) | <img src="./Images/AndroidApp.jpeg" width="200" />
[Desktop App](./Frontend/) | <img src="./Images/DesktopApp.png" width="400" />