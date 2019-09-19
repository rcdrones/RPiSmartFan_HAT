# RPiSmartFan_HAT
This is Smart fan hat for pi4/pi3(and 40GPIO) , include gui program , and manual



# 产品特点
* HAT板载双风扇能根据cpu的内部温度自动调速
* 提供Python3开发的上位机GUI调速程序
* 带有2颗实体按键，实现对RPi 关机、重启、冷启动。*摒弃直接拔插头关机方式*
* LED显示实时CPU、内存的占用率情况。
* 平衡Pi4发热，和风扇带来的噪音问题。实现自动化风扇的停止、静音运行、全速运行模式切换，大大延长风扇的寿命。市面上普通风扇无法实现智能调速。一旦开启就是最大风力，噪音就会非常大，长时间工作含油轴承提前下岗。而本产品则是按需调速，采集CPU的温度，有的放矢性的自动调速。
* 由于所有的软件协议栈全部采用Python进行源码级开源。玩家可在Pi4上二次开发上位机程序。从而实现LED可编程，显示不同的采集数据！
* 预留22P GPIO扩展排针，方便在HAT板之外进行扩展，*例如：接入其他的传感器和RPi GPIO进行互联*。


# 通讯协议栈   
* 树莓派发给HAT MCU的协议   
*$SmartFAN,cpu_usage,memory_usage,fan_speed,check_sum$*   
1)  cpu_usage 为cpu的当前时刻的占用率 （0-100）   
2)  memory_usage 为内存的使用率 （0-100）    
3)  fan_speed 为树莓派通知MCU进行调速的值。*0 = 停止 1 = 安静模式 2 = 增强模式*  
4)  check_sum$ 之前3个数字相加 mod 100    

* MCU发送给树莓派的协议：   
*$ECHO,fan_current_speed,op_code,check_sum$*   
1)  fan_current_speed MCU当前跑的fan speed数值反馈。*定义同上*   
2)  op_code 是操作码， 0 = normal state , 1 = halt system , 2 = reboot system   
3)  check_sum$ 之前2个数字相加mod 100   


# 软件安装教学
## 一键安装
```

```
## 一键卸载
```

```
## 二次开发下载源代码：
```
git clone https://github.com/rcdrones/RPiSmartFan_HAT
```
# GUI功能介绍
```
启动命令：sudo sf
```

TIPS：
```
install chinese 输入法：sudo apt-get install fcitx fcitx-googlepinyin fcitx-module-cloudpinyin fcitx-sunpinyin
```
