# Lamp-System -- Android

:warning: OPEN THIS FOLDER IN ANDROID STUDIO, AND UPLOAD TO AN ANDROID DEVICE

- This is a simple android app. There are two buttons, one for incrementing and one for decrementing the currently active patter. When a button is clicked a PATCH request will be sent to change the currently active pattern. The app also automatically polls the server for changes, this is done threaded as the long polling otherwise blocks the main thread too much.