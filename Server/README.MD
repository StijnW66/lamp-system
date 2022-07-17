# Lamp-System -- Server

- The server defines a RESTful API.
- The server uses the Spring Boot Framework and is hosted on Heroku.
- The webserver is connected to a postgresql database, which is also hosted on Heroku.
- Database updates should be communicated quickly, other applications should therefore poll continuously. This webserver implementation supports `long polling`, a request from a client is held and only receives a response when the database is updated (or when the timeout is reached). This minimizes the network usage of the lamp-system, without compromizing the responsiveness.
- The server can be run locally (port 8083) with gradle, using the `gradle bootrun` command from within the Server directory


In the code there are two Objects defined:
- [Pattern](src/main/java/com/lampsystem/lampsystem/Entities/Pattern.java), is an object for storing color patterns. The patterns are stored as an array of rgb values and duration.
- [RgbValuesPattern](src/main/java/com/lampsystem/lampsystem/Entities/RgbValuesPattern.java), which stores the currently active pattern and the timestamp of the latest update.


The following API endpoints are available:

From [Controllers/PatternController.java](src/main/java/com/lampsystem/lampsystem/Controllers/PatternController.java)

- GET /pattern ([Example](https://cryptic-earth-79580.herokuapp.com/pattern))
- GET /pattern/{id} ([Example](https://cryptic-earth-79580.herokuapp.com/pattern/6))
- GET /pattern/count ([Example](https://cryptic-earth-79580.herokuapp.com/pattern/count))
- POST /pattern
- PATCH /pattern/{id}
- DELETE /pattern/{id}

From [Controllers/RgbValuesPatternController.java](src/main/java/com/lampsystem/lampsystem/Controllers/RgbValuesPatternController.java)

- GET /rgb_values/{id} ([Example](https://cryptic-earth-79580.herokuapp.com/rgb_values/1))
- GET /rgb_values/update/{id} (Same as above, but holds the request for up to 30s, if there is no change in pattern)
- PATCH /rgb_values/{id}
- POST /rgb_values (Only used for initialization)