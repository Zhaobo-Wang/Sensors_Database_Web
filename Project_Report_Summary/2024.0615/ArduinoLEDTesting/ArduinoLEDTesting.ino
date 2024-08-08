const int ledPin = 13; //创建一个常量，表示LED连接到引脚7
void setup() {
  //setup函数，用于初始化设置
  pinMode(ledPin, OUTPUT); //设置引脚7为输出端

}

void loop() {
  //loop函数 循环
  digitalWrite(ledPin, HIGH); //数字写入的过程，写入HIGH(相当于正电压)，信号进入点亮LED
  delay(500); //点亮时间0.5秒，500 = 0.5秒

  digitalWrite(ledPin, LOW); //数字写入的过程，写入LOW，熄灭LED
  delay(2000); //等待时间2秒，2000 = 2秒

}
