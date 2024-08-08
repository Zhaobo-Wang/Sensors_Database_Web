#include <DHT.h> //包含DHT库，用于与DHT传感器通信

#define AMP_PIN A0 //定义DHT传感器连接的引脚为Analog A0
#define DHTTYPE DHT11 //定义DHT传感器的类型为DHT11

DHT dht(AMP_PIN, DHTTYPE); //创建DHT传感器对象，指定引脚和传感器类型

//光敏电阻

const int sensorPin = A0; //定义常量 sensorPin，连接输入引脚A0

void setup(){
	Serial.begin(9600); //初始化串行通信，波特率设为9600
}

void loop(){
	int ampValue = analogRead(sensorPin); // 从常量sensorPin读取模拟信号值并存储在ampValue中
  //analogRead函数返回一个从0到1023的整数值，代表从0到5V的电压。

	float voltage = ampValue * (5.0/1023.0); //将模拟值转换为实际电压值
	//模拟输入的范围是0到1023，对应的电压范围是0到5V，将模拟值ampValue转换为实际电压值

	Serial.print("Amplified Signal: "); //输出字符串 "Amplified Signal: " 
	Serial.print(ampValue); //输出 ampValue 的值
	Serial.print("\tVoltage: "); //输出字符串"Voltage: " 
	Serial.println(voltage); //输出 voltage 的值
	delay(1000); //等待1秒，然后继续循环
}