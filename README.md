# RPiSmartFan_HAT
This is Smart fan hat for pi4 , include gui program , and manual



#产品特点
* CPU风扇能自动调速
* 上位机python gui程序开源
* 可用硬件开关打开、重启、关闭树莓派
* 内含RTC。密闭树莓派没有RTC，导致时间不准困扰
* 可观察到实时CPU、内存的占用情况。
* 基本弥补pi4的所有不足。安装在pi4上。可以做到真真意义上的单机工作


# 协议   
* 树莓派发给HAT的协议
** $SmartFAN,cpu_usage,memory_usage,fan_speed,check_sum$
*** cpu_usage 为cpu的当前时刻的占用率 （0-100）
*** memory_usage 为内存的使用率 （0-100）
*** fan_speed 为树莓派通知MCU进行调速的目标值（0%，30-100%）
*** check_sum$ 之前3个数字相加mod 100

* MCU发送给树莓派的协议：
** $ECHO,fan_current_speed,op_code,check_sum$
*** fan_current_speed MCU当前跑的fan speed数值
*** op_code 是操作码， 0 = normal state , 1 = halt system , 2 = reboot system
*** check_sum$ 之前2个数字相加mod 100


