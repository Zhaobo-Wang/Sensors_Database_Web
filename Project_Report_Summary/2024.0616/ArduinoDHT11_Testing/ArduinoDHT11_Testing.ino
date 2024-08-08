#include <DHT.h> //包含DHT库，用于与DHT传感器通信

#define DHTPIN 2 //定义DHT传感器连接的引脚为2
#define DHTTYPE DHT11 //定义DHT传感器的类型为DHT11

DHT dht(DHTPIN, DHTTYPE); //创建DHT传感器对象，指定引脚和传感器类型

void setup() {
  Serial.begin(9600); //初始化串口通信，波特率为9600
  dht.begin(); //初始化DHT传感器
}

void loop() {
  delay(2000); //延迟2秒，读取传感器数据的间隔时间
  float humidity = dht.readHumidity(); //读取湿度值
  float temperatureC = dht.readTemperature(); //读取温度值（摄氏度）
  float temperatureF = dht.readTemperature(true); //读取温度值（true参数表示读取华氏温度）

  //if判断isnan()判断一个值是否是NaN
  if (isnan(humidity) || isnan(temperatureC) || isnan(temperatureF)){ //判断三个参数中是否有任何一个是NaN
    Serial.println("Failed to read from DHT sensor!"); //如果读取失败，打印错误信息
    return; //结束当前循环
  }

  Serial.print("Humidity: "); //打印湿度标签
  Serial.print(humidity);  //打印湿度值
  Serial.print(" %\t");  //打印百分号和制表符
  Serial.print("Temperature in Celsius: ");  //打印摄氏温度标签
  Serial.print(temperatureC);  //打印摄氏温度值
  Serial.print(" *C\t");  //打印摄氏度符号和制表符
  Serial.print("Temperature in Fahrenheit: ");  //打印华氏温度标签
  Serial.print(temperatureF);  //打印华氏温度值
  Serial.println(" *F");  //打印华氏度符号
}