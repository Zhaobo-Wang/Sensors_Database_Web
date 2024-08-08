#include <ESP8266WiFi.h>
 
#ifndef STASSID
#define STASSID "whyhd"     // 你的 WiFi 热点名称
#define STAPSK "eoeoeoeo"  // 你的 WiFi 密码
#endif
 
const char* ssid = STASSID;
const char* password = STAPSK;
 
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
 
  // 开始连接到 WiFi 网络
  Serial.println();
  Serial.println();
  Serial.print("连接到 ");
  Serial.println(ssid);
 
  /* 明确将 ESP8266 设置为 WiFi 客户端，否则，默认情况下，
     它会尝试充当客户端和接入点，可能会导致
     WiFi 网络上的其他 WiFi 设备出现网络问题。 */
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
 
  Serial.println("");
  Serial.println("WiFi 连接成功");
  Serial.println("IP 地址: ");
  Serial.println(WiFi.localIP());
}
 
void loop() {
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
  digitalWrite(LED_BUILTIN, HIGH);
  delay(2000);
}