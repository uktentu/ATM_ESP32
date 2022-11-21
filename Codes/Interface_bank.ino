#include "WiFi.h"
#include <HTTPClient.h>

// WiFi credentials
const char* ssid = "1234";            // change SSID
const char* w_password = "12345678";  // change password

// Google script ID and required credentials
String GOOGLE_SCRIPT_ID = "AKfycbxn4JkQ7yb8nCMQcn02Lc6-wowluU45zepWR7BOkCqFFOy8iAU_D8t08xlv59ybEeVu";

String payload;
String username;
String password;
String money;
String data;
String url_ext;
String name;
void setup() {
  delay(1000);
  Serial.begin(9600);
  delay(1000);
  pinMode(2, OUTPUT);
  // connect to WiFi
  Serial.println();
  Serial.print("Connecting to wifi: ");
  Serial.println(ssid);
  Serial.flush();
  WiFi.begin(ssid, w_password);
  while (WiFi.status() != WL_CONNECTED) {
    digitalWrite(2, LOW);
    Serial.print(".");
    delay(500);
    digitalWrite(2, HIGH);
    delay(500);
  }
  Serial.println("\nConnected\n");
}

void loop() {
  // Entering username
  if (WiFi.status() == WL_CONNECTED && Serial.available()) {
    char temp = Serial.read();
    if (temp == 'L') {
      while (Serial.available() <= 0) {};
      username = Serial.readString();
      while (Serial.available() <= 0) {};
      password = Serial.readString();
      delay(1000);
      url_ext = "username=" + String(username) + "&password=" + String(password) + "&login";
      data = receive_data();
      if (data != "n") {
        for (int i = 0; i < data.length(); i = i + 1) {
          Serial.write(data[i]);
        }
        Serial.write(":");
      } else {
        Serial.write("n");
      }
      /// Available Balance
    } else if (temp == 'b') {
      while (Serial.available() <= 0) {};
      String acc = Serial.readString();
      delay(500);
      url_ext = "acc_no=" + String(acc) + "&balance";
      data = receive_data();
      for (int i = 0; i < data.length(); i = i + 1) {
        Serial.write(data[i]);
      }
      Serial.write(":");
      // mini statement
    } else if (temp == 'm') {
      while (Serial.available() <= 0) {};
      String acc = Serial.readString();
      delay(500);
      url_ext = "acc_no=" + String(acc) + "&mini_sheet";
      data = receive_data();
      for (int i = 0; i < data.length(); i = i + 1) {
        Serial.write(data[i]);
      }
      Serial.write(":");
    }
    ///Credinting Money
    else if (temp == 'r') {
      while (Serial.available() <= 0) {};
      String acc = Serial.readString();
      while (Serial.available() <= 0) {};
      money = Serial.readString();
      delay(1000);
      url_ext = "credit=" + String(money) + "&acc_no=" + String(acc);
      data = receive_data();
      delay(1000);
      if (data == "y") {
        Serial.write("y");
      } else if (data == "n") {
        Serial.write("n");
      }
      ///Debiting Money
    } else if (temp == 'd') {
      while (Serial.available() <= 0) {};
      String acc = Serial.readString();
      while (Serial.available() <= 0) {};
      money = Serial.readString();
      delay(1000);
      url_ext = "debit=" + String(money) + "&acc_no=" + String(acc);
      data = receive_data();
      delay(1000);
      if (data == "y") {
        Serial.write("y");
      } else if (data == "n") {
        Serial.write("n");
      }
      /// Creating new User
    } else if (temp == 'c') {
      while (Serial.available() <= 0) {};
      username = Serial.readString();
      while (Serial.available() <= 0) {};
      password = Serial.readString();
      while (Serial.available() <= 0) {};
      name = Serial.readString();
      delay(1000);
      url_ext = "username=" + String(username) + "&password=" + String(password) + "&name=" + String(name) + "&create";
      data = receive_data();
      if (data == "y") {
        Serial.write("y");
      } else if (data == "n") {
        Serial.write("n");
      } else {
        Serial.write(".");
      }
    }
  }
}

String receive_data() {
  if (WiFi.status() == WL_CONNECTED) {
    digitalWrite(2, LOW);
    HTTPClient http;
    String urlFinal = "https://script.google.com/macros/s/" + GOOGLE_SCRIPT_ID + "/exec?" + String(url_ext);

    // Serial.println("Making a request");
    // Serial.println(urlFinal);
    http.begin(urlFinal.c_str());
    http.setFollowRedirects(HTTPC_STRICT_FOLLOW_REDIRECTS);
    int httpCode = http.GET();
    if (httpCode > 0) {
      // Serial.println(httpCode);
      payload = http.getString();
      digitalWrite(2, HIGH);
      return payload;
    } else {
      Serial.println("Error on http request");
    }
    http.end();
    delay(1000);
    digitalWrite(2, HIGH);
  }
}
