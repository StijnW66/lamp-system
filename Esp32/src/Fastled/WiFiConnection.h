#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>



const char* ssid     = "vdwater";
const char* password = "Edna2014";

HTTPClient http;

String date;


String httpRequest(String path) {
    //Serial.print("connecting to ");
    //Serial.println(path);

    http.begin(path);
    http.addHeader("Date", date);

 
    int httpCode = http.GET();
    //Serial.println(httpCode);

    String json = http.getString();
    Serial.println(json);
    return json;
}

std::vector<int> transformToArray(String values) {
    std::vector<int> vector;
    values = values.substring(1, values.length() - 1);

    for(int i = 0; i < 3; i++) {
      int pos = values.indexOf(",");
      vector.push_back(values.substring(0, pos).toInt());

      values = values.substring(pos + 1, values.length());
    }
    vector.push_back(values.toInt());
    return vector;
}


std::vector<std::vector<int>> initializePattern() {

    String path = "https://cryptic-earth-79580.herokuapp.com/rgb_values/1?output=full";

    String json = httpRequest(path);

    StaticJsonDocument<2000> doc;
    DeserializationError error = deserializeJson(doc, json);

//    if (error) {
//    Serial.print(F("deserializeJson() failed: "));
//    Serial.println(error.f_str());
//    return;
//    }

    date = doc["lastUpdated"].as<String>();

    JsonArray arr = doc["pattern"]["patternContents"];

    std::vector<std::vector<int>> vector;

    for(String v : arr) {
      std::vector<int> vector_rgb = transformToArray(v);
      vector.push_back(vector_rgb);
    }

    return vector;
}


std::vector<std::vector<int>> setupNetwork() {
    delay(1000);

    // We start by connecting to a WiFi network

    Serial.println();
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(ssid);

    WiFi.mode(WIFI_STA);  
    WiFi.begin(ssid, password);

    int attempts = 0;
    while (WiFi.status() != WL_CONNECTED) {
        Serial.print(WiFi.status());
        delay(500);
        Serial.print(".");

        if (attempts++ > 25) {
          ESP.restart();
        }
    }

    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());

    http.setTimeout(30000);
    return initializePattern();
}


std::vector<std::vector<int>> updateLoop() {
    String path = "https://cryptic-earth-79580.herokuapp.com/rgb_values/update/1";
    String json = httpRequest(path);

    std::vector<std::vector<int>> vector;

    if(json.length() == 0) {
      return vector;
    }

    StaticJsonDocument<2000> doc;
    DeserializationError error = deserializeJson(doc, json);
    if (error) {
    Serial.print(F("deserializeJson() failed: "));
    Serial.println(error.f_str());
    return vector;
    }

    date = doc["lastUpdated"].as<String>();
    JsonArray arr = doc["pattern"]["patternContents"];
    
    for(String v : arr) {
      std::vector<int> vector_rgb = transformToArray(v);
      vector.push_back(vector_rgb);
    }

    return vector;
}
